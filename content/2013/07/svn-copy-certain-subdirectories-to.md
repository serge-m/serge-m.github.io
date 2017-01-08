Title: SVN copy certain subdirectories to a branch 
Author: SergeM
Date: 2013-07-03 17:07:00
Slug: svn-copy-certain-subdirectories-to
Tags: 

<span style="font-family: Times, Times New Roman, serif;">There was always a problem for me to copy only certain directories from one branch to another.</span>
<span style="font-family: Times, Times New Roman, serif;">For example we have following directory structure:</span>
<pre style="background-color: #eeeeee; border: 0px; line-height: 18px; margin-bottom: 10px; max-height: 600px; overflow: auto; padding: 5px; vertical-align: baseline; width: auto;"><code style="border: 0px; margin: 0px; padding: 0px; vertical-align: baseline;"><span style="font-family: Courier New, Courier, monospace;">trunk
      - project1
      - project2
          -subdir1
          -subdir2
          -subdir3        </span></code></pre><div style="text-align: left;"><code style="border: 0px; margin: 0px; padding: 0px; vertical-align: baseline;"><span style="font-family: Times, Times New Roman, serif;">We want to copy only subdir2 to a branch /branches/branch1 with saving all the structure of projects.</span></code></div><div style="text-align: left;"><span style="font-family: Times, Times New Roman, serif;"><code style="border: 0px; margin: 0px; padding: 0px; vertical-align: baseline;"></code></span></div><pre style="background-color: #eeeeee; border: 0px; line-height: 18px; margin-bottom: 10px; max-height: 600px; overflow: auto; padding: 5px; vertical-align: baseline; width: auto;"><code style="border: 0px; margin: 0px; padding: 0px; vertical-align: baseline;"><span style="font-family: Courier New, Courier, monospace;"><span style="font-size: small; line-height: normal; white-space: normal;">branches/branch1</span>
      - project1
      - project2
          -subdir2</span><span style="font-family: Times, Times New Roman, serif; font-size: 14px;">
</span></code></pre><span style="font-family: Times, Times New Roman, serif;">We want to copy only subdir2 to a branch /branches/branch1 with saving all the structure of projects.</span>
<div><span style="font-family: Times, Times New Roman, serif;">Such a manipulation is required if you want to make a private branch for outsorcer and you don't wan him to see the other parts of the code. However you want to support reintegration of the branch back to the trunk.</span></div><div><span style="font-family: Times, Times New Roman, serif;">
</span></div><div><span style="font-family: Times, Times New Roman, serif;">The solution is&nbsp;</span></div><div><pre style="border: 0px; margin-bottom: 10px; max-height: 600px; overflow: auto; padding: 5px; vertical-align: baseline; width: auto;"><code><span style="background-color: #eeeeee; font-family: Courier New, Courier, monospace; line-height: 18px;">svn cp --parents ./project2/subdir2 http://repo.url/branches/branch1/project2/subdir2</span></code></pre><pre style="border: 0px; margin-bottom: 10px; max-height: 600px; overflow: auto; padding: 5px; vertical-align: baseline; width: auto;"><code><span style="background-color: #eeeeee; font-family: Courier New, Courier, monospace; line-height: 18px;">or</span></code></pre><pre style="border: 0px; margin-bottom: 10px; max-height: 600px; overflow: auto; padding: 5px; vertical-align: baseline; width: auto;"><code><span style="background-color: #eeeeee; font-family: Courier New, Courier, monospace;"><span style="color: #222222; white-space: normal;">svn cp --parents http://<svn_path>/trunk/project2</span><span style="color: #222222; white-space: normal;">/subdir2 <working copy path>/branches/branch1/project2/subdir2</span></span></code></pre><span style="font-family: Times, Times New Roman, serif;">Subversion creates all intermediate directories.</span></div>