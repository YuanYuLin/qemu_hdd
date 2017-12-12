import ops
import iopc

pkg_path = ""
output_dir = ""
output_rootfs_dir = ""
src_hda="hda.img"
src_hdb="hdb.img"
src_hdc="hdc.img"
src_hdd="hdd.img"
sh_parted="Parted.sh"

def set_global(args):
    global pkg_path
    global output_dir 
    global output_rootfs_dir
    global src_hda
    global src_hdb
    global src_hdc
    global src_hdd
    global sh_parted
    pkg_path = args["pkg_path"]
    output_dir = args["output_path"]
    output_rootfs_dir = ops.path_join(iopc.getOutputRootDir(), "qemu")
    src_hda=ops.path_join(pkg_path, src_hda)
    src_hdb=ops.path_join(pkg_path, src_hdb)
    src_hdc=ops.path_join(pkg_path, src_hdc)
    src_hdd=ops.path_join(pkg_path, src_hdd)
    sh_parted=ops.path_join(pkg_path, sh_parted)

def MAIN_ENV(args):
    set_global(args)
    return False

def MAIN_EXTRACT(args):
    set_global(args)

    ops.mkdir(output_rootfs_dir)
    ops.copyto(src_hda, output_rootfs_dir)
    ops.copyto(src_hdb, output_rootfs_dir)
    ops.copyto(src_hdc, output_rootfs_dir)
    ops.copyto(src_hdd, output_rootfs_dir)

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

def MAIN_CLEAN_BUILD(args):
    set_global(args)

    return False

def MAIN(args):
    set_global(args)
    print "image squashfs"

