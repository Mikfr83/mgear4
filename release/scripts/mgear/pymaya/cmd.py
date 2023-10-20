from . import base
from . import exception
from maya import cmds
from maya import mel
from maya.api import OpenMaya
import functools
import inspect


__ALL__ = []
__DO_NOT_CAST_FUNCS = set()
__SCOPE_ATTR_FUNCS = {"listAttr"}


SCOPE_ATTR = 0
SCOPE_NODE = 1
Callback = functools.partial
displayError = OpenMaya.MGlobal.displayError
displayInfo = OpenMaya.MGlobal.displayInfo
displayWarning = OpenMaya.MGlobal.displayWarning


def exportSelected(*args, **kwargs):
    cmds.file(*args, es=True, **kwargs)


def hasAttr(obj, attr, checkShape=True):
    obj = _obj_to_name(obj)

    has = cmds.attributeQuery(attr, n=obj, ex=True)
    if not has and checkShape:
        shapes = cmds.listRelatives(obj, s=True) or []
        for s in shapes:
            has = cmds.attributeQuery(attr, n=s, ex=True)
            if has:
                break

    return has


def selected(**kwargs):
    return _name_to_obj(cmds.ls(sl=True, **kwargs))


class versions():
    def current():
        return cmds.about(api=True)


def importFile(filepath, **kwargs):
    return _name_to_obj(cmds.file(filepath, i=True, **kwargs))


__ALL__.append("Callback")
__ALL__.append("displayError")
__ALL__.append("displayInfo")
__ALL__.append("displayWarning")
__ALL__.append("exportSelected")
__ALL__.append("mel")
__ALL__.append("hasAttr")
__ALL__.append("selected")
__ALL__.append("versions")
__ALL__.append("importFile")


def _obj_to_name(arg):
    if isinstance(arg, (list, set, tuple)):
        return arg.__class__([_obj_to_name(x) for x in arg])
    elif isinstance(arg, base.Base):
        return arg.name()
    else:
        return arg


def _name_to_obj(arg, scope=SCOPE_NODE, known_node=None):
    # lazy importing
    from . import bind

    if isinstance(arg, (list, set, tuple)):
        return arg.__class__([_name_to_obj(x, scope=scope, known_node=known_node) for x in arg])

    elif isinstance(arg, str):
        if (scope == SCOPE_ATTR and known_node is not None):
            try:
                return bind.PyNode(f"{known_node}.{arg}")
            except:
                return arg
        else:
            try:
                return bind.PyNode(arg)
            except:
                return arg
    else:
        return arg


def _pymaya_cmd_wrap(func, wrap_object=True, scope=SCOPE_NODE):
    def wrapper(*args, **kwargs):
        nargs = _obj_to_name(args)
        nkwargs = {}
        for k, v in kwargs.items():
            nkwargs[k] = _obj_to_name(v)

        res = func(*nargs, **nkwargs)

        if wrap_object:
            known_node = None
            if scope == SCOPE_ATTR:
                candi = None

                if nargs:
                    known_node = nargs[0]
                else:
                    sel = cmds.ls(sl=True)
                    if sel:
                        known_node = sel[0]

                if known_node is not None:
                    if not isinstance(_name_to_obj(known_node), base.Base):
                        known_node = None

            return _name_to_obj(res, scope=scope, known_node=known_node)
        else:
            return res

    return wrapper


def getAttr(*args, **kwargs):
    args = _obj_to_name(args)
    kwargs = _obj_to_name(kwargs)

    try:
        return cmds.getAttr(*args, **kwargs)
    except Exception as e:
        raise exception.MayaAttributeError(*e.args)


def setAttr(*args, **kwargs):
    args = _obj_to_name(args)
    kwargs = _obj_to_name(kwargs)

    try:
        cmds.setAttr(*args, **kwargs)
    except Exception as e:
        raise exception.MayaAttributeError(*e.args)


local_dict = locals()

for n, func in inspect.getmembers(cmds, callable):
    if n in local_dict:
        continue

    local_dict[n] = _pymaya_cmd_wrap(func,
                                     wrap_object=(n not in __DO_NOT_CAST_FUNCS),
                                     scope=SCOPE_ATTR if n in __SCOPE_ATTR_FUNCS else SCOPE_NODE)
    __ALL__.append(n)