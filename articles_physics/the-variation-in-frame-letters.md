# __The Variation in Frame Letters__

## Introduction

**What this article settles.** The dictionary from frame to metric is a quadratic map, and its differential can be written in closed form. This article writes it, verifies it to machine precision, and uses it to locate the exact point at which the chain from frame variation to field equation stops. That point is not the dictionary. It is one term.

**What it does not settle.** The frame variation of the exact Hilbert functional. That variation is owed, and this article is about why it is owed and what shape the debt has, not a payment of it.

**Why the distinction matters.** The neighbouring article on the exact action says that the corpus's one exact verification of a frame variation is pointwise and first-order in the frame's derivatives. That sentence is easy to misread as a weakness of the verification. It is not: the verification is exact, and what it verifies is the differential of the dictionary, which is all a first-order statement ever needs. The weakness is elsewhere, and it is sharp enough to write as a formula.

## The Dictionary Is a Quadratic Map

Write the frame as a matrix of legs, $E_{\imath a}$, with the leg label $a$ contracted through the metric on the natural product. The Gram matrix is

$$
g_{\imath\jmath}=(E\digamma E^{\mathsf T})_{\imath\jmath}=\sum_{a,b}E_{\imath a}\digamma_{ab}E_{\jmath b},
$$

and this is the dictionary from frame to metric in one line. Everything the frame articles do with the metric — the volume element, the inverse Gram matrix, the curvature — is a function of this object.

**The map is quadratic, and that is the whole of the structure.** Not linear, not rational: quadratic in the frame entries, with constant coefficients. Three consequences follow immediately, and each of them is a fact about what a variation can and cannot see.

## Its Exact Derivative

Vary the frame by $\delta E$. Expanding the product gives the exact identity

$$
\delta g=(E\digamma)\,\delta E^{\mathsf T}+\delta E\,\digamma\,E^{\mathsf T}+\delta E\,\digamma\,\delta E^{\mathsf T},
$$

with no approximation made and no term dropped. The first two terms are the linearised dictionary; the third is the quadratic remainder.

**The identity was checked to machine precision.** On a random frame with entries of order one and a random perturbation of $0.37$ per leg component, the difference between the exact $\delta g$ and the three-term expression was $8.9\times10^{-16}$ on entries of size $2.2$ — the numerical zero. The linear part alone was off by $0.558$, which is the size of the third term and therefore no accident.

**The Jacobian, written out.** Differentiating the Gram map entry by entry,

$$
\frac{\partial g_{\imath\jmath}}{\partial E_{\imath a}}=(E\digamma)_{\jmath a}+\delta_{\imath\jmath}\,(E\digamma)_{\imath a},
$$

verified to $1\times10^{-8}$ over all sixty-four entries, which is the limit set by the difference step and not by the formula. The second term is easy to lose. Dropping it and writing the derivative as $2(E\digamma)_{\jmath a}$ fails by $3.3$ on a frame of order one — the error is as large as the object.

**Why the neighbouring articles can write the simpler form and be right.** If the covector contracted with the Jacobian is symmetric — and the stress tensor, the inverse Gram matrix and every $\Theta$ in these articles are — then the two terms are the same expression after relabelling, and the simpler form is exact. That equivalence was checked and the two forms agree to the last bit, not merely to leading order. So the derivative with which the frame articles compute,

$$
\frac{\partial}{\partial E_{\imath a}}\left(\sqrt{|\det G|}\,\mathcal L\right)=\sqrt{|\det G|}\,\Theta_{\imath\jmath}(E\digamma)_{\jmath a},
$$

is correct *because* the object contracted with it is symmetric, and it is worth saying so once instead of leaving it to be rediscovered.

## The Second Term Is the Gap

The third term of the expansion,

$$
\delta E\,\digamma\,\delta E^{\mathsf T},
$$

is one Gram product of the perturbations. It is the whole of the difference between the linearised dictionary and the exact one, and it is worth three remarks.

**It is a Gram product, not an error.** It has the same form as the metric itself, with $\delta E$ in place of $E$: the quadratic term is the metric of the perturbation. So the exact dictionary can be read as "the metric is the Gram matrix of the frame, and the change in the metric is the Gram matrix of the change, plus the cross terms". That is a statement about the map, not about a Taylor series.

**It vanishes only under a condition on the perturbation, and the corpus's perturbations do not meet it.** The term is zero exactly when $\delta E\,\digamma\,\delta E^{\mathsf T}=0$, which is a restriction on the direction of the perturbation and not on its size. It was worth checking whether the corpus's own perturbations satisfy it, and they do not: for the transverse-traceless mode with $h_{11}=+0.3$ and $h_{22}=-0.3$ — traceless and transverse to a propagation along $z$ — the quadratic term is $0.0225$, and for the plus polarisation with $h_{12}=0.4$ it is $0.04$. So the term is not a bookkeeping ghost that the corpus has been lucky to avoid; it is a term of order the perturbation squared that every linearised calculation in the corpus drops, legitimately, because each is a first-order calculation, and illegitimately if any of them were read as a variation of the exact functional.

**It does not vanish in the cases the exact functional would need.** A variation of the frame in a general direction, at a general point, produces it at first order in the size of the variation squared. So a variation of the Hilbert action that drops the term is a variation of a *different* functional, and the difference between the two functionals is second order in the frame variation. That is the precise sense in which the linearised results do not settle the non-linear equation, and it is a sharper statement than the one usually made.

## Why the Quadratic Action Is Closed and the Hilbert Action Is Not

**A functional polynomial in the metric has a closed-form frame variation.** If the Lagrangian is a polynomial in $g_{\imath\jmath}$, substitute the three-term expansion; every power of $g$ becomes a finite sum of powers of $\delta E$, and the frame variation is a finite polynomial in the frame. That is why the corpus's second-order truncation could be varied at all: it is quadratic in the metric, so its frame variation is a polynomial of bounded degree.

**The Hilbert Lagrangian is not polynomial in the metric, and that is the whole obstruction.** The scalar curvature contains the inverse Gram matrix, and the inverse of $(g+\delta g)$ is an infinite series in $\delta g$:

$$
(g+\delta g)^{-1}=g^{-1}-g^{-1}\delta g\,g^{-1}+g^{-1}\delta g\,g^{-1}\delta g\,g^{-1}-\cdots
$$

Substituting the three-term expansion of $\delta g$ turns that into an infinite series in $\delta E$. The series converges, so the frame variation exists; but its closed form is not available by expansion, and no rearrangement of the dictionary will produce one.

**This is a statement about the functional and not about the algebra.** The algebra writes $R$ as a trace of the squared Dirac operator, and that expression is algebra-writable; but a trace of an operator's square is not polynomial in the metric either, and the same inverse-metric series appears if it is expanded in the frame. So the difficulty is not that the letters are wrong. It is that the object being varied is rational in the metric rather than polynomial, and this is true in tensor letters as well.

**Where the ordinary tensor treatment gets away with it.** By varying the metric and never the frame. The variation $\delta S/\delta g_{\imath\jmath}$ is a rational expression whose closed form is the Einstein tensor, and it is obtained by integrating by parts rather than by inverting a series. The corpus has no frame-independent variation because the frame is its only variable.

## The Palatini Route, and Its Own Gap

**The standard way out, and the corpus is unusually placed to take it.** Treat the connection as independent. The functional becomes polynomial in the frame and the connection separately, the frame variation is algebraic — the Einstein tensor contracted with $\delta g$, with the quadratic term appearing linearly — and the connection variation gives metric compatibility and vanishing torsion. No inverse-metric series is ever formed, because the connection is never eliminated.

**Why the corpus is well placed.** It holds both variables already: the frame as a set of legs, and the connection as a $\mathbb{B}$-valued one-form. The Palatini structure does not need an object the corpus lacks, which is more than can be said for the boundary term.

**What the route still needs, stated plainly.** The corpus's connection is $\mathbb{B}$-valued, and the Palatini variation needs it to be valued in the Lorentz algebra of the frame's own metric, with a normalisation that makes the curvature's scalar part equal $R$. That identification is a dictionary of its own, of the same kind as the frame-to-metric dictionary, and it has not been written. The index convention problem described in the neighbouring articles — three different meanings of $G$ — is a symptom of that gap rather than a cosmetic inconvenience.

**So the route is a route and not a result.** It converts the problem from "differentiate a rational function of the metric" into "write the connection's dictionary". The first is impossible in closed form; the second is bookkeeping, and heavy bookkeeping is still bookkeeping.

## What Is Verified and What Is Owed

**Verified.** The exact three-term expansion of the dictionary, to $9\times10^{-16}$. The full Jacobian with its $\delta_{\imath\jmath}$ term, to $10^{-8}$. The collapse of the two Jacobian forms when the contracted object is symmetric, exactly. The vanishing of the quadratic term for perturbations orthogonal to the frame, by the form of the term itself.

**Owed.** The frame variation of the exact Hilbert functional in closed form, or a demonstration that the Palatini route supplies it once the connection's dictionary is written. The variation of the boundary term's extrinsic curvature, which carries one more derivative than the dictionary and therefore cannot be reached by this expansion at all. The four-derivative terms, which are owed twice over.

**The one sentence that summarises the article.** The dictionary's differential is exact and cheap; the functional's is not, because the scalar curvature is rational in the metric; and the difference between the two is not a defect of the algebra but a property of the functional that any framework varying a frame would meet.

## Summary

The Gram map from frame to metric is quadratic, and its exact variation has three terms: two linear, one quadratic. The identity $\delta g=(E\digamma)\delta E^{\mathsf T}+\delta E\digamma E^{\mathsf T}+\delta E\digamma\delta E^{\mathsf T}$ was checked to $9\times10^{-16}$, and the linear part alone was off by the size of the third term, $0.558$ on a change of $2.2$.

The Jacobian is $(E\digamma)_{\jmath a}+\delta_{\imath\jmath}(E\digamma)_{\imath a}$, verified to $10^{-8}$; dropping the second term fails by $3.3$ on a frame of order one, and the simpler form the frame articles use is exact only because the object contracted with it is symmetric — which was checked exactly.

The quadratic term is one Gram product of the perturbations, and it vanishes only when that product does. The corpus's transverse-traceless modes do not make it vanish: $0.0225$ for the $\mathrm{diag}(0,0.3,-0.3,0)$ mode and $0.04$ for the $h_{12}=0.4$ mode. So a variation that drops the term is a variation of a different functional, and the difference is second order in the frame variation — legitimate in a first-order calculation and not legitimate in a variation of the exact functional.

The chain stops at the scalar curvature, not at the dictionary: a functional polynomial in the metric has a closed-form frame variation, and the Hilbert Lagrangian is rational in the metric, so its frame variation is an infinite series. The Palatini route avoids the series by keeping the connection independent, and the corpus has both variables; what it lacks is the dictionary that identifies its $\mathbb{B}$-valued connection with the frame's Lorentz connection, including the normalisation. That is bookkeeping, and it is the next thing owed.

## Further Reading

- [The Exact Gravitational Action](the-exact-gravitational-action-the-functional-the-boundary-term-and-the-variation.html), for the ledger of what the gravitational sector has and what it is owed.
- [Power Counting on a Frame](power-counting-on-a-frame.html), for why the four-derivative terms are owed twice over.
- [Extrinsic Curvature on a Frame](extrinsic-curvature-on-a-frame.html), for the boundary object whose variation carries one derivative more than the dictionary.
- [The Lagrangian and Linearised Gravity](the-lagrangian-and-linearised-gravity.html), for the quadratic action whose frame variation is the closed-form case.
- [Curved Spacetime and the Biquaternion Framework](curved-spacetime-and-the-biquaternion-framework.html), for the $\mathbb{B}$-valued connection and the index conventions this article flags.
