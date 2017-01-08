Title: Graduated non convexity scheme (GNC)
Author: SergeM
Date: 2014-11-05 17:15:00
Slug: graduated-non-convexity-scheme-gnc
Tags: optical flow

<div dir="ltr" style="text-align: left;" trbidi="on">Optimization of energy terms can be difficult in OF, because of  non-convexity and local optima.
Construct a series of energy functions




<img alt="" height="16" src="data:image/png;base64,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" width="200" />
EQ is convex, quadratic
alpha changes from 1 to 0, so Energy Ec changes from quadratic to original.
for each alpha they find optimum through setting derivatives of Ec to 0.
Solution on each stage becomes initialization on the next one.


Proposed in: D. Sun, S. Roth, J. Lewis, and M. J. Black. Learning optical flow. In ECCV, volume 3, pages 83–97, 2008. [[pdf](http://cs.brown.edu/~dqsun/pubs/eccv2008.pdf" target="_blank)]
</div>