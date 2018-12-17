import ops
import iopc

pkg_path = ""
output_dir = ""
output_rootfs_dir = ""
sh_parted="Parted.sh"
storage_generator="gen_storage.py"

def set_global(args):
    global pkg_path
    global output_dir 
    global output_rootfs_dir
    global sh_parted
    global storage_generator
    pkg_path = args["pkg_path"]
    output_dir = args["output_path"]
    output_rootfs_dir = ops.path_join(iopc.getOutputRootDir(), "qemu")
    sh_parted=ops.path_join(pkg_path, sh_parted)

def MAIN_ENV(args):
    set_global(args)
    return False

def MAIN_EXTRACT(args):
    set_global(args)

    ops.mkdir(output_rootfs_dir)
    CMD = ['python2.7', storage_generator, ops.path_join(output_rootfs_dir, 'hda.img')] 
    ops.execCmd(CMD, pkg_path, False)

    CMD = ['python2.7', storage_generator, ops.path_join(output_rootfs_dir, 'vda.img')] 
    ops.execCmd(CMD, pkg_path, False)

    CMD = ['python2.7', storage_generator, ops.path_join(output_rootfs_dir, 'vdb.img')] 
    ops.execCmd(CMD, pkg_path, False)

    CMD = ['python2.7', storage_generator, ops.path_join(output_rootfs_dir, 'vdc.img')] 
    ops.execCmd(CMD, pkg_path, False)

    CMD = ['python2.7', storage_generator, ops.path_join(output_rootfs_dir, 'vdd.img')] 
    ops.execCmd(CMD, pkg_path, False)

    CMD = ['python2.7', storage_generator, ops.path_join(output_rootfs_dir, 'vde.img')] 
    ops.execCmd(CMD, pkg_path, False)

    return True

def MAIN_PATCH(args, patch_group_name):
    set_global(args)
    for patch in iopc.get_patch_list(pkg_path, patch_group_name):
        if iopc.apply_patch(output_dir, patch):
            continue
        else:
            sys.exit(1)

    return True

def MAIN_CONFIGURE(args):
    set_global(args)

    return False

def MAIN_BUILD(args):
    set_global(args)

    return False

def MAIN_INSTALL(args):
    set_global(args)

    return False

def MAIN_SDKENV(args):
    set_global(args)

    return False

def MAIN_CLEAN_BUILD(args):
    set_global(args)

    return False

def MAIN(args):
    set_global(args)
    print "image squashfs"

