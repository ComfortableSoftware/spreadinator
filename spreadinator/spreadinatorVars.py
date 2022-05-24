

from CF.SUBM_D import (
    _00_OS as CF_OS,
    _00_OS_VARS as CF_OSV,
    _00_SHUTIL as CF_SHUTIL,
    _01_HASHES as CF_HASH,
    _01_OPTIONS as CF_OPT,
    _01_OPTIONS_KEYS as OK,
)


V = none


CURRENT_DIR_NUM = 0
DEFAULT_DEST_DIR_ERRS = "/storage/media/spreadDestErrs"
DEFAULT_DEST_DIR_OTHR = "/storage/media/spreadDestOthr"
DEFAULT_DEST_DIR_PICS = "/storage/media/spreadDestPics"
DEFAULT_DEST_DIR_VIDS = "/storage/media/spreadDestVids"
DEFAULT_SOURCE_DIR = "."
NUM_DEST_DIRS = 300
NUM_DIR_DIGITS_STR = "03d"
SOURCE_DIR_LIST = []
SOURCE_FILE_LIST = []



H_AUTO = f"""
Set mode to 'auto'.
'-a', '-auto' spreadinator will set copy if source is read only, move if it's read/write.
This is the default mode.
"""
O_AUTO = {
    V.OK.K_ARGS: [
        "-a",
        "-auto",
    ],
    V.OK.K_KWARGS: {
        V.OK.K_ACTION: "store_true",
        V.OK.K_HELP: H_AUTO,
    },
}


H_COPY = f"""
Set mode to 'copy'.
'-c', '-copy' spreadinator will set copy from source tree to destination tree.
"""
O_COPY = {
    V.OK.K_ARGS: [
        "-c",
        "-copy",
    ],
    V.OK.K_KWARGS: {
        V.OK.K_ACTION: "store_true",
        V.OK.K_HELP: H_COPY,
    },
}


H_MOVE = f"""
Set mode to 'move'.
'-m', '-move' spreadinator will set move from source tree to destination tree.
"""
O_MOVE = {
    V.OK.K_ARGS: [
        "-m",
        "-move",
    ],
    V.OK.K_KWARGS: {
        V.OK.K_ACTION: "store_true",
        V.OK.K_HELP: H_MOVE,
    },
}


H_RENAME_F = f"""
Randomly rename destination files while moving or copying them.
'-r', '-ren', "-rename" will not rename them.
{V.CF_V.INDENT_IN}Renaming is the default.
"""
O_RENAME_F = {
    V.OK.K_ARGS: [
        "-r",
        "-ren",
        "-rename",
    ],
    V.OK.K_KWARGS: {
        V.OK.K_ACTION: "store_true",
        V.OK.K_HELP: H_RENAME_F,
    }
}


H_RENAME_T = f"""
Randomly rename destination files while moving or copying them.
'-R', '-REN', '-RENAME' will rename them.
Renaming is the default.
"""
O_RENAME_T = {
    V.OK.K_ARGS: [
        "-R",
        "-REN",
        "-RENAME",
    ],
    V.OK.K_KWARGS: {
        V.OK.K_ACTION: "store_true",
        V.OK.K_HELP: H_RENAME_T,
    }
}


H_SOURCE_DIR = f"""
Set the root directory to source"""
O_SOURCE_DIR = {
    V.OK.K_ARGS: [
        "-s",
        "-source",
        "-sourceDir",
        "-src",
    ],
    V.OK.K_KWARGS: {
        V.OK.K_ACTION: "store_true",
        V.OK.K_DEST: "sourceDir",
        V.OK.K_HELP: H_SOURCE_DIR,
        V.OK.K_NARGS: "?",
        V.OK.K_REQUIRED: False,
        V.OK.K_TYPE: str,
    }
}



H_LOUD = f"""
Set loud mode (INFO_LEVEL = <-l=##>) where ## is how loud to be -1 == no messages, 0 == info, etc.
"""
O_LOUD = {
    V.OK.K_ARGS: [
        "-l",
        "-loud"
    ],
    _KWArgs_ = {
        V.OK.K_DEST: "loud",
        V.OK.K_HELP: _TStr_,
        V.OK.K_NARGS: 1,
        V.OK.K_TYPE: int,
        V.OK.K_REQUIRED: False,
    },
}












#
