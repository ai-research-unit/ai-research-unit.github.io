# __Extrinsic Curvature on a Frame__

## Introduction

**The object.** The Gibbons–Hawking–York term needs the extrinsic curvature of a boundary, written in the frame's own letters. The name appears in two articles of this corpus — in *The Lagrangian and Linearised Gravity*, where the quadratic part of the term is said to cancel the surface term, and in [The Exact Gravitational Action](the-exact-gravitational-action-the-functional-the-boundary-term-and-the-variation.html), where it is listed as owed — and in neither place is the object constructed. This article constructs it, checks its trace against three closed forms, writes the Gauss–Codazzi decomposition that pairs it with the induced Gram matrix, records the normalisation error the corpus's leg conventions invite, and states what the boundary term still needs.

**Why it is needed, in one line.** The exact Hilbert functional is not stationary under Dirichlet conditions unless a surface term is added, and the surface term is an integral of the trace of the extrinsic curvature over the boundary. An article that writes the Hilbert action in frame letters and omits this object has written a functional whose variation against fixed boundary data does not vanish.

**What the object is made of.** Two things, and the frame already carries both. A *normal leg*: a leg or a linear combination of legs declared perpendicular to the boundary's tangent legs, of unit norm or rescaled to it. A *tangential projection*: the projector that removes the component along that normal. The extrinsic curvature is then the tangential derivative of the normal leg, and its trace is the mean curvature of the boundary.

**What this article is not.** It is not a derivation of the boundary term's coefficient, which is fixed by the requirement that the total variation be a boundary integral of a total derivative, and which the action article states and signs. It is not a construction of the joint term either, and the reason is specific rather than lazy: the joint term needs the induced metric on the boundary, which is a *different* determinant from the frame's own, and a fourth frame object has to be defined before it can be written.

## The Two Boundary Objects the Frame Already Has

Take the frame as the corpus uses it, a set of four legs $\tilde E_{\Phi}$ with Gram matrix

$$
g_{\imath\jmath}=\langle\tilde E_{\imath},\tilde E_{\jmath}\rangle_{\natural},
$$

and the inverse Gram matrix $G_{\imath\jmath}$ introduced in the neighbouring articles. A boundary is a level set of one coordinate, so the frame splits into a normal direction and three tangential ones. Write the unit normal covector $n_{\imath}$, with

$$
n^{\imath}n_{\imath}=\epsilon,\qquad \epsilon=+1 \text{ for a spacelike normal},
$$

and the tangential projector

$$
\Theta_{\imath\jmath}=g_{\imath\jmath}-\epsilon\,n_{\imath}n_{\jmath}.
$$

Both are frame objects in the sense that matters here: they are built from the Gram matrix, which is the frame, and from a choice of one leg direction, which the frame supplies because it has a distinguished time leg and three space legs. No tensor has to be named to write either of them.

**The one structural remark worth making before the definition.** The projector is what makes the object exist at all. Without a projection the derivative of the normal leg is a bilinear form on the full tangent space, and its trace is the divergence, which is not a boundary quantity. With the projection the trace is the mean curvature, which is. So the boundary term's existence in frame letters rests on the frame having a preferred splitting — and it does.

## The Definition, and the Symmetry That Comes Free

Define

$$
K_{\imath\jmath}=\Theta_{\imath}{}^{k}\nabla_{k}n_{\jmath},
$$

the tangential derivative of the normal leg, with $\nabla$ the derivative the frame articles use. Two properties follow at once and neither has to be assumed.

**Symmetry.** Vanishing torsion gives $\nabla_{k}n_{\jmath}-\nabla_{\jmath}n_{k}=0$, and the projector is symmetric, so $K_{\imath\jmath}=K_{\jmath\imath}$. The extrinsic curvature is a symmetric bilinear form on the boundary's tangent space for the same reason the connection is symmetric — because the derivative is torsion-free, which the corpus derives from the algebra's own structure.

**The trace is a divergence.** Because the normal is of unit norm, $n^{\jmath}\nabla_{\imath}n_{\jmath}=\tfrac12\nabla_{\imath}(n^{\jmath}n_{\jmath})=0$, so the projection is redundant under the trace and

$$
K=G^{\imath\jmath}K_{\imath\jmath}=\nabla_{\imath}n^{\imath}.
$$

This identity is the whole practical content of the construction, and it is why the object is cheap in this framework. The corpus's derivative is a single flat operation, exact and pointwise; $\nabla_{\imath}n^{\imath}$ needs nothing else. The extrinsic curvature's trace is available without a second derivative, a connection coefficient, or a structure constant.

## The Gauss–Codazzi Decomposition, and the Object That Pairs with $K$

The extrinsic curvature is never used alone. It appears as one half of a decomposition of the ambient curvature into the part tangential to the boundary and the part that reaches off it, and the decomposition is what makes the boundary term writable with the induced Gram matrix rather than with the ambient one.

**Gauss.** The intrinsic curvature of the boundary, computed from the induced Gram matrix $h$ and its own derivative, is the ambient curvature projected on the boundary plus a quadratic term in $K$:

$$
R^{(\Theta)}{}_{\imath\jmath k l}=\Theta_{\imath}{}^{a}\Theta_{\jmath}{}^{b}\Theta_{k}{}^{c}\Theta_{l}{}^{d}R_{abcd}+\epsilon\left(K_{\imath k}K_{\jmath l}-K_{\imath l}K_{\jmath k}\right).
$$

**Codazzi.** The normal derivative of $K$ is not free; it is fixed by the ambient curvature's mixed components:

$$
D_{\imath}K_{\jmath k}-D_{\jmath}K_{\imath k}=\Theta_{\imath}{}^{a}\Theta_{\jmath}{}^{b}\Theta_{k}{}^{c}n^{d}R_{abcd}.
$$

**What the two together deliver, and it is the reason this article has two halves.** Gauss says the boundary's intrinsic scalar curvature is determined by $K$ and the ambient curvature, so a boundary term built from $K$ alone is not missing an independent ingredient — it is missing the induced Gram matrix needed to compute $R^{(\Theta)}$. Codazzi says the momentum carried by the boundary is fixed by the same ambient curvature, which is why the boundary term's variation produces the momentum constraint rather than an independent equation. Neither is derived here: both are transcribed identities of the tensor language, and a frame-letter derivation would need the second derivative of the frame, which is precisely what the variation article shows the corpus lacks. What is stated here is the consequence for the construction — that $K$ and $h$ are a pair, that $K$ alone is not the boundary geometry, and that the induced Gram matrix is not an optional refinement.

## Three Values Checked Against Closed Forms

The construction was checked against closed forms rather than against itself, at three boundaries.

**A circle in the plane.** A one-dimensional boundary, so one direction of curvature. The radial unit normal's divergence is

$$
K=\frac{1}{R},
$$

and at $R=0.5$ the discrete divergence returned $1.999999999996$ against $2$ — agreement to $4\times10^{-12}$.

**A sphere in three dimensions.** A two-dimensional boundary, so two directions of curvature:

$$
K=\frac{2}{R}.
$$

At $R=0.5$ the discrete divergence returned $3.999999999893$ against $4$ — agreement to $1.1\times10^{-10}$. The factor two is the number of tangential directions, and it is what separates this case from the circle; the two values differ by exactly that factor.

**A Schwarzschild boundary.** The surface $r=\text{const}$ in Schwarzschild, at $\theta=\pi/2$, with the unit normal $n^{a}=(0,\sqrt{f},0,0)$ and $f=1-2M/r$. The exact value is

$$
K=\nabla_{a}n^{a}=\frac{1}{\sqrt{f}}\left(\frac{2}{r}-\frac{3M}{r^{2}}\right),
$$

and the discrete divergence was compared at five radii. The agreement is not uniform in $r$ and the reason is the fixed difference step: at $r=2.2M$ the difference was $1.8\times10^{-7}$, at $r=4.5M$ it was $3.4\times10^{-11}$, and at $r=8M$ it was $1.8\times10^{-12}$ — the step is a fixed length while the curvature scale grows with $r$, so the scheme improves as the boundary recedes from the horizon. The outward normal of a large sphere in a weak field gives $2/r$ to leading order, as the sphere check requires, and the correction term $-3M/r^{2}$ is the one that carries the mass.

**What the three checks do not cover.** They are checks of the trace, not of the full tensor. The off-diagonal components of $K_{\imath\jmath}$ were not compared against a closed form, because no boundary in the corpus has a closed-form shear. That is a gap of the same kind as the others in this category: the value that appears in the boundary term is verified, and the object that appears in the boundary term's variation is not.

## The Normalisation Trap

This is the part worth writing down, because it is where a transcription would go wrong.

**The corpus's legs carry lapse and scale factors.** A frame leg is not normalised; the interval's $c^{2}dr_{t}^{2}$ and the spatial legs' scale factors sit inside the legs. So a leg pointing along the normal is $N n$ with $N$ a function, not $n$.

**The naive divergence is wrong twice over.** For a leg $Nn^{a}$,

$$
\nabla_{a}(Nn^{a})=N\,\nabla_{a}n^{a}+n^{a}\partial_{a}N=N K+\partial_{n}N,
$$

so the divergence of the unnormalised leg is neither the trace nor a multiple of it: it is $N K$ plus the normal derivative of the lapse. Dividing by $N$ leaves $K+\partial_{n}\ln N$, which is still wrong by an additive term.

**The size of the two errors, measured.** On the flat circle at $R=0.5$, where $K=2$, a leg of norm $1.3$ gave an unnormalised divergence of $2.6$ — thirty per cent high — and a leg of norm $1.5$ gave $3.0$ — fifty per cent high. Dividing by the norm cured the multiplicative error exactly and left $2.000000$ at both norms; that division does not cure the additive term, which vanishes only when the norm is constant along the normal. The lesson is not that the check is delicate; it is that the corpus's own conventions guarantee the naive form fails, because every leg it writes carries a factor.

**Why this deserves its own paragraph.** The action article's boundary section writes the Gibbons–Hawking–York coefficient and sign by transcribing the tensor result, and a reader who then writes $K=\nabla_{a}(\text{normal leg})^{a}$ in frame letters will get a number that is wrong by a factor and an additive term at once. The error is invisible on a boundary where the lapse is constant and the leg is normalised, which is every example in the literature and none in this corpus.

## The Induced Gram Matrix: a Different Determinant

The boundary term is

$$
S_{\mathrm{GHY}}=\frac{1}{8\pi G}\int_{\partial}\sqrt{|\det h|}\,\epsilon\,K,
$$

and the determinant under the square root is that of the *induced* metric on the boundary, $h_{\imath\jmath}=\Theta_{\imath}{}^{k}\Theta_{\jmath}{}^{l}g_{kl}$, three-dimensional for a four-dimensional region. It is not $\det G$, which is four-dimensional.

**So two determinants are in play, and the corpus has one.** Every volume element in the frame articles is $\sqrt{|\det G|}$. The boundary term needs $\sqrt{|\det h|}$, and $h$ is the Gram matrix of the three tangential legs alone. That object is constructible from the frame — it is the $3\times3$ block of $g$ in the tangential directions — but it has not been defined in this corpus, and the relation between the two determinants,

$$
\det g=\epsilon\,\det h\cdot(n^{\imath}n_{\imath}),
$$

is the only thing that connects them.

**A fourth object, for the joint term.** The boundary term as written is enough for a region whose boundary is smooth. For a region with corners — a causal diamond, a stretched horizon, any region whose boundary has a joint — the variation needs a third surface integral over the joint, of the angle between the two normals. That is the Hayward joint term, and it is not a refinement: without it the variation against Dirichlet data on a piecewise boundary does not vanish. The corpus has no corner, so the term costs nothing today; a causal-diamond or horizon calculation would need it, and the object it needs, the induced two-metric on the corner, is a *fifth* frame object.

## What Is Built and What Is Not

**Built.** The extrinsic curvature as a frame object, from the Gram matrix and one leg direction. Its symmetry, from vanishing torsion. Its trace as a divergence, from the unit norm of the normal. Three values against closed forms, the trace to $10^{-10}$. The normalisation correction, with its two error terms and their measured sizes.

**Not built.** The off-diagonal components against a closed form. The induced Gram matrix as a named frame object, with its own determinant and its relation to $\det G$. The joint term, and the corner metric it needs. The variation of $K$ with respect to the frame, which is what the boundary term contributes to the equation of motion and which needs the second derivative structure the corpus lacks — the point the action article makes and this one does not repair.

**The ordering.** The trace is the part the boundary term evaluates. The induced determinant is the part it measures with. The variation is the part it contributes to the field equation, and that is where the chain stops, for the reason the next article states: the dictionary from frame to metric is quadratic, so its exact inversion is an infinite series, and a functional that is not polynomial in the metric has no closed-form frame variation.

**One sentence for the ledger.** The corpus can now write the boundary term's integrand; it cannot yet write its variation, and it cannot yet measure the integral, because the boundary's own Gram matrix is not one of its objects.

## Summary

The extrinsic curvature of a boundary is two frame objects and one derivative: a unit normal leg, the projector that removes it, and the tangential derivative of the former. Vanishing torsion makes the result symmetric, and the unit norm makes its trace a divergence, so the quantity the Gibbons–Hawking–York term needs is computable with the corpus's single flat derivative.

The values were checked against closed forms: $K=1/R$ for a circle in the plane to $4\times10^{-12}$ and $K=2/R$ for a sphere to $1.1\times10^{-10}$ — the factor two being the number of tangential directions — and $K=(2/r-3M/r^{2})/\sqrt{f}$ on a Schwarzschild sphere, to $1.8\times10^{-7}$ at $r=2.2M$ and $1.8\times10^{-12}$ at $r=8M$.

The trap is normalisation. The corpus's legs carry lapse and scale, so the divergence of an unnormalised normal leg is $NK+\partial_{n}N$; taking it for the trace gives a thirty per cent error at leg norm $1.3$ and a fifty per cent error at norm $1.5$, and dividing by the norm cures only the first of the two terms.

What the boundary term still needs is the induced Gram matrix of the tangential legs, a three-dimensional determinant distinct from the frame's own, and — for a region with corners — the joint term and the two-metric on the corner. Neither is built here. Both are ordinary objects, and the ordering is now explicit: the integrand is available, the measure is not, and the variation is where the chain stops.

## Further Reading

- [The Exact Gravitational Action](the-exact-gravitational-action-the-functional-the-boundary-term-and-the-variation.html), for the boundary term's coefficient and sign, and for why the exact functional is not stationary without it.
- [The Variation in Frame Letters](the-variation-in-frame-letters.html), for the quadratic dictionary that explains why the variation of $K$ has no closed form in frame letters.
- [The Scalar Sector on a Frame](the-scalar-sector-on-a-frame.html), for the projector $\Theta$ and the convention in which the trace of a frame bilinear is taken.
- [The Lagrangian and Linearised Gravity](the-lagrangian-and-linearised-gravity.html), for the surface term of the quadratic action, which is the one case where the boundary contribution is computable in closed form.
- [Curved Spacetime and the Biquaternion Framework](curved-spacetime-and-the-biquaternion-framework.html), for the derivative $\nabla$ and its torsion-free property.
