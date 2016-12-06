Title: Using h264/multiview codec from Intel Media SDK
Author: SergeM
Date: 2013-10-11 12:37:00
Slug: using-h264multiview-codec-from-intel
Tags: c++,errors,dll,video


I needed to launch multiview compression using codec from Intel MVC. Approximately a half a year ago I launched it normally. Yesterday it tried and I got such an error:

    $ ./sample_encode.exe h264 -i input.yuv -o output.h264 -w 1920 -h 1080
    Return on error: error code -3, .\src\pipeline_encode.cpp       865

    Return on error: error code 1,  .\src\sample_encode.cpp 343
    Frame number: 0

I started debug and found out the error appears in 

    MFXVideoSession::mfxStatus Init(mfxIMPL impl, mfxVersion *ver)
    {
        return MFXInit(impl, ver, &m_session);
    }

Error code

     MFX_ERR_UNSUPPORTED                 = -3,   /* undeveloped feature */


Of course, the cause was in missing dll.

    libmfxsw32.dlllibmfxsw64.dll

After I added it to console's directory everything became fine.


PS I could not build sample_encode with Visual Studio 2008. So use 2010 instead.