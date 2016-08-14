Title: Using h264/multiview codec from Intel Media SDK
Author: SergeM
Date: 2013-10-11 12:37:00
Slug: using-h264multiview-codec-from-intel
Tags: c++,errors,dll,video

<div dir="ltr" style="text-align: left;" trbidi="on"><div class="tr_bq">I needed to launch multiview compression using codec from Intel MVC. Approximately a half a year ago I launched it normally. Yesterday it tried and I got such an error:</div>
<blockquote><b>$ ./sample_encode.exe h264 -i input.yuv -o output.h264 -w 1920 -h 1080
Return on error: error code -3, .\src\pipeline_encode.cpp &nbsp; &nbsp; &nbsp; 865

Return on error: error code 1, &nbsp;.\src\sample_encode.cpp 343
Frame number: 0</b></blockquote><div>I started debug and found out the error appears in&nbsp;</div><blockquote class="tr_bq"><b>MFXVideoSession::mfxStatus Init(mfxIMPL impl, mfxVersion *ver)
{
&nbsp; &nbsp; return MFXInit(impl, ver, &amp;m_session);
}</b></blockquote>Error code
<blockquote class="tr_bq">**&nbsp;MFX_ERR_UNSUPPORTED &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; = -3, &nbsp; /* undeveloped feature */**</blockquote>
Of course, the cause was in missing dll.
<blockquote class="tr_bq">**libmfxsw32.dll****libmfxsw64.dll**</blockquote>After I added it to console's directory everything became fine.


PS I could not build sample_encode with Visual Studio 2008. So use 2010 instead.</div>