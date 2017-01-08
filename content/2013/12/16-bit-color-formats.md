Title: 16 bit color formats
Author: SergeM
Date: 2013-12-11 12:11:00
Slug: 16-bit-color-formats
Tags: 

[http://forums.creativecow.net/thread/2/940078](http://forums.creativecow.net/thread/2/940078)

In adobe after effects:

    ::::
    #define PF_MAX_CHAN8			255
    #define PF_HALF_CHAN8			128
    #define PF_MAX_CHAN16			32768
    #define PF_HALF_CHAN16			16384
    #define CONVERT8TO16(A)		( (((long)(A) * PF_MAX_CHAN16) + PF_HALF_CHAN8) / PF_MAX_CHAN8 )
    
</div>