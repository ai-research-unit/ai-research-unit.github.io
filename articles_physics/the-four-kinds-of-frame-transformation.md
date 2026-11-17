# __The Four Kinds of Frame Transformation__

## Introduction

Frames can be rotated, boosted, sheared, or screwed. The four words name the four conjugacy classes of the Lorentz group, and the classifier is one number: the trace. In this algebra the trace is $\operatorname{tr}\mathsf{M}_2(\tilde U)=2Q_t$, so the classifier is the complex number $Q_t$, and the four classes are the four ways $Q_t$ can sit relative to the real line and the interval $[-1,1]$.

This article states the classification, gives the eigenvalues of each kind, says what each kind does to a frame and to the light cone, writes the four in the algebra, and isolates the two exceptional cases at $\tau=\pm2$.

The article assumes *The Exponential Map from Algebra to Group* for the parametrisation, *When the Axes Commute: The Normal Transformations* for the normal class, *The Spectrum Does Not Determine the Frame* for what the spectrum does and does not fix, and *Why Boosts Are Not Additive: The Bracket Table* for the non-commutativity that produces the fourth kind.

## The Classifier

### The Trace

For $\tilde U\in G$,

$$
\tau:=\operatorname{tr}\mathsf{M}_2(\tilde U)=2Q_t .
$$

The trace is invariant under conjugation by any element of $GL_2(\mathbb{C})$, so $\tau$ is a conjugacy invariant. It is also the only continuous invariant of a two-by-two matrix apart from the determinant, which is fixed at one.

### The Discriminant

The eigenvalues are the roots of $\lambda^{2}-\tau\lambda+1=0$, so

$$
\lambda_\pm=\frac{\tau\pm\sqrt{\tau^{2}-4}}{2},
\qquad
\tau^{2}-4=(\lambda_+-\lambda_-)^{2}.
$$

The discriminant decides whether the eigenvalues are equal, real and distinct, or a complex pair, and that trichotomy plus the position of $\tau$ gives the four classes.

### The Rule

| condition on $\tau=2Q_t$ | class |
|---|---|
| $\tau$ real, $\lvert\tau\rvert<2$ | elliptic |
| $\tau$ real, $\lvert\tau\rvert>2$ | hyperbolic |
| $\tau=\pm2$ exactly | parabolic, unless the element is central |
| $\tau$ not real | loxodromic |

The four names are the classical names of the four kinds of Möbius transformation, and they are the corpus's names for the four kinds of frame transformation.

## The Four Kinds

### Elliptic

$\tau$ real with $\lvert\tau\rvert<2$. Then $\tau^{2}-4<0$ and the eigenvalues are

$$
\lambda_\pm=e^{\pm i\theta_{\mathrm{axr}}/2},\qquad \tau=2\cos\tfrac{\theta_{\mathrm{axr}}}{2},\qquad \theta_{\mathrm{axr}}\in(0,2\pi).
$$

The element is conjugate to a rotation. The whole rotation subgroup is elliptic, and conversely every elliptic element is a rotation in some frame.

### Hyperbolic

$\tau$ real with $\lvert\tau\rvert>2$. Then $\tau^{2}-4>0$ and the eigenvalues are real and distinct with product one:

$$
\lambda_\pm=\pm e^{\pm\theta_{\mathrm{rpd}}/2},\qquad \lvert\tau\rvert=2\cosh\tfrac{\theta_{\mathrm{rpd}}}{2},\qquad\theta_{\mathrm{rpd}}>0,
$$

with the sign $+$ when $\tau>2$ and $-$ when $\tau<-2$. The element is conjugate to a boost. Every boost is hyperbolic.

### Parabolic

$\tau=\pm2$ exactly. Then the discriminant vanishes and the two eigenvalues coincide at $\pm1$. An element with a double eigenvalue is either a multiple of the identity — and the only such elements in $G$ are $\pm e_t$ — or it is not diagonalisable, in which case it is conjugate to

$$
\pm\begin{pmatrix}1&1\\0&1\end{pmatrix},
$$

a **unipotent** element: the exponential of a null generator. This is the class the exponential chart of *The Exponential Map from Algebra to Group* reaches only in the limit, and it is the class the chart's cut locus separates.

### Loxodromic

$\tau$ not real. Then the eigenvalues are a complex pair $\mu,\mu^{-1}$ with $\mu$ neither real nor of unit modulus:

$$
\mu=re^{i\theta_{\mathrm{axr}}/2},\qquad r>0,\ r\neq1,\ \theta_{\mathrm{axr}}\notin\{0,2\pi\},
$$

and the element is conjugate to a boost times a rotation about the *same* axis, with both parameters nonzero. That is the normal element of *When the Axes Commute: The Normal Transformations* in its non-degenerate case, and the name is the classical one for a screw motion.

### Why These Are All

A conjugacy class of $SL_2(\mathbb{C})$ is determined by its eigenvalues, which are determined by $\tau$ up to the discrete choice of which is which. The four boxes above exhaust the possible positions of a pair $\{\mu,\mu^{-1}\}$: on the unit circle, on the positive or negative real axis, at the double point $\pm1$, or elsewhere in the complex plane. So the classification is a partition and not a list of examples.

## The Eigenvalues of Each Type

### The Table

| class | $\tau$ | eigenvalues | representative |
|---|---|---|---|
| elliptic | $2\cos\tfrac{\theta_{\mathrm{axr}}}{2}$, $\lvert\tau\rvert<2$ | $e^{\pm i\theta_{\mathrm{axr}}/2}$ | rotation through $\theta_{\mathrm{axr}}$ |
| hyperbolic | $\pm2\cosh\tfrac{\theta_{\mathrm{rpd}}}{2}$, $\lvert\tau\rvert>2$ | $\pm e^{\pm\theta_{\mathrm{rpd}}/2}$ | boost of rapidity $\theta_{\mathrm{rpd}}$ |
| parabolic | $\pm2$ | $\pm1$ double | $e_t\pm\tilde X$, $\tilde X$ null |
| loxodromic | $2r\cos\tfrac{\theta_{\mathrm{axr}}}{2}+i(\ldots)$ | $re^{i\theta_{\mathrm{axr}}/2}$, $r^{-1}e^{-i\theta_{\mathrm{axr}}/2}$ | boost times rotation, same axis |

### What the Eigenvalues Say

Read the eigenvalues as data about the frame:

- a **phase** means rotation;
- a **real scale** means boost;
- a **double eigenvalue** means the two eigenspaces have collapsed, so the frame has lost a direction;
- a **spiral** means both at once, about one axis.

### A Warning About the Word

The class is a conjugacy-class label, not a label of the word. A product of a boost and a rotation about *different* axes can be hyperbolic: the example $\tilde B_x\tilde R_z$ with rapidity $0.9$ and angle $0.7$ has $\tau=2.072$ real, so it is hyperbolic, and its eigenvalues are real and positive, $1.3072$ and $0.7650$. It is not a boost in the frame it was written in, and it is one in another frame. So "hyperbolic" means "conjugate to a boost", not "a boost".

## What Each Does to a Frame

### The Elliptic Case

A rotation turns the spatial part of the frame about an axis and leaves the axis direction alone. On the light cone it fixes the two null directions along the axis, and it moves every other null direction around the axis.

So the elliptic transformation has **two fixed points on the celestial sphere**, and the sphere is rotated about them.

### The Hyperbolic Case

A boost stretches along the boost direction and squeezes the time axis, leaving the two null directions along the axis fixed and moving everything else. On the celestial sphere it flows from the repelling fixed point to the attracting one.

So the hyperbolic transformation also has **two fixed points**, but its action between them is a flow and not a rotation, and its orbits are the curves of constant aberration.

### The Parabolic Case

A null rotation fixes exactly **one** null direction and shears transversally to it. In the algebra it is $e_t+\tilde X$ with $\tilde X$ nilpotent: the exponential of a null generator, whose exponential series terminates after two terms.

It is the case in which the two fixed points have coalesced, which is why the two-dimensional family of frames collapses to a one-dimensional family of shears.

### The Loxodromic Case

A screw motion fixes the same **two** null directions as a boost along its axis, and spirals about them: the frame is boosted along the axis and rotated about it at the same time, and the two do not interfere because they share the axis.

### The Summary

| class | fixed null directions | what the frame does |
|---|---|---|
| elliptic | $2$ | rotates about an axis |
| hyperbolic | $2$ | boosts along an axis |
| parabolic | $1$ | shears along a null direction |
| loxodromic | $2$ | boosts and rotates about one axis |

The count of fixed points is the invariant that survives the abstraction, and it is the classification's geometric content: $2$, $2$, $1$, $2$ with the third case the degenerate one.

## The Four in the Algebra

### The Words

In the Cartan word $\tilde U=\tilde U_\Psi\tilde u_{\mathrm r}$:

| class | the word |
|---|---|
| elliptic | $\tilde U_\Psi=e_t$: the boost factor is the identity |
| hyperbolic | $\tilde u_{\mathrm r}=e_t$: the rotation factor is the identity |
| parabolic | neither factor is the identity, and the scalar part is $\pm1$ |
| loxodromic | both factors are nontrivial and their axes coincide |

The last two rows are the ones worth stating: the parabolic case is the one in which the word exists but the scalar part is at the boundary, and the loxodromic case is the one in which both factors are nontrivial and commute.

### The Generators

| class | generator |
|---|---|
| elliptic | a rotation generator $J_\eta$, real coefficients in the exponent |
| hyperbolic | a boost generator $K_\eta$, imaginary coefficients in the exponent |
| parabolic | a **null** linear combination, $\tilde X$ scalar-free and nilpotent |
| loxodromic | a sum of a rotation and a boost generator about the same axis |

Only the last row needs two generators, and only the third needs a generator outside the six: the six are a basis, but a null combination of them is not one of the six.

### Why the Fourth Kind Needs the Product

The exponential of a single element of $\mathfrak{sl}_2(\mathbb{C})$ is never loxodromic in the generic sense unless the element has both a real and an imaginary part along commuting directions: $\exp(K+\tfrac12\theta_{\mathrm{axr}}J)$ with $[K,J]=0$ gives a screw. For non-commuting generators the exponential is hyperbolic, elliptic or parabolic according to its trace, and the loxodromic examples are all normal. So the fourth kind is the normal class's non-degenerate case and is not a new phenomenon.

## The Exceptional Cases

### The Central Elements

$\tau=\pm2$ with the element central means $\tilde U=\pm e_t$. These are diagonalisable — they are scalar matrices — and they are neither parabolic nor any of the other three: they are the degenerate members of all four classes at once. A classification by trace must exclude them by hand, and the excluding condition is "not a multiple of the identity".

This is the one place where the trace classifier needs a patch, and it is the same patch that the exponential chart needs: $\pm e_t$ are the two elements on which every description degenerates.

### The Negative Hyperbolic Trace

$\tau<-2$ is hyperbolic with both eigenvalues negative. Its square has positive eigenvalues, so on the projective group it is a boost, and on the group it is a boost times $-e_t$. A reader who classifies the projective transformation will see only $\lvert\tau\rvert$, which is why the sign of the trace is presentational in the projective group and real in the group.

### The Boundary $\lvert\tau\rvert=2$ Away From the Centre

The parabolic class is not a measure-zero accident: each of the two parabolic classes, $\tau=2$ and $\tau=-2$, is a two-dimensional submanifold of the six-dimensional group, the conjugacy class of a unipotent matrix. So it is thin but not negligible, and the physical interpretation is a light-like boost: a boost whose rapidity has gone to infinity, conjugated into a finite shear.

### The Elliptic Boundary

$\lvert\tau\rvert\to2$ from below is a rotation whose angle tends to $0$ or $2\pi$; from above is a boost whose rapidity tends to $0$ with a sign of trace fixed by the sheet. So the same boundary is approached from two sides by two different one-parameter families, and the boundary point itself is a unipotent element and belongs to neither. Note also that infinite rapidity is *not* on this boundary: a boost of rapidity $\theta_{\mathrm{rpd}}$ has $\lvert\tau\rvert=2\cosh(\theta_{\mathrm{rpd}}/2)$, which runs to infinity, so the light-like limit is at infinity and not at $\lvert\tau\rvert=2$.

## Summary

The Lorentz group has four conjugacy classes, classified by the trace $\tau=2Q_t$: elliptic when $\tau$ is real with $\lvert\tau\rvert<2$ and the eigenvalues are invertible-modulus pair; hyperbolic when $\tau$ is real with $\lvert\tau\rvert>2$ and the eigenvalues are real and reciprocal; parabolic when $\tau=\pm2$ and the element is a nontrivial unipotent; loxodromic when $\tau$ is not real and the eigenvalues are a spiral pair. The four are the rotation, the boost, the null shear and the screw motion, they have two, two, one and two fixed null directions, and they are read off the scalar part of the element in the algebra. The two central elements $\pm e_t$ sit at the boundary and belong to none of the four.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tau=2Q_t$ | the trace of the matrix, the classifier |
| $\theta_{\mathrm{axr}}$ | the elliptic angle, i.e. the rotation angle of the elliptic class |
| $\theta_{\mathrm{rpd}}$ | the hyperbolic rapidity of the hyperbolic class |
| $\mu=re^{i\theta_{\mathrm{axr}}/2}$ | the loxodromic eigenvalue, $\theta_{\mathrm{axr}}$ its phase angle |
| unipotent | $e_t+\tilde X$ with $\tilde X^{2}=0$, $\tilde X\neq0$ |
| fixed null direction | a light-like direction preserved by the transformation |

## Further Reading

- J. Stillwell, *Geometry of Surfaces*, Springer, 1992, and any standard treatment of Möbius transformations — the elliptic, hyperbolic, parabolic and loxodromic classification and its fixed-point count.
- S. Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces*, Academic Press, 1978 — conjugacy classes of $SL(2,\mathbb{C})$ and their geometric meaning.
- R. Penrose and W. Rindler, *Spinors and Space-Time*, Vol. 1, Cambridge University Press, 1984 — the action of Lorentz transformations on the celestial sphere and the fixed null directions.
- *The Exponential Map from Algebra to Group* — the chart whose cut locus is the parabolic class.
- *When the Axes Commute: The Normal Transformations* — the normal class, of which the loxodromic case is the non-degenerate part.
- *The Spectrum Does Not Determine the Frame* — what the eigenvalues of these four classes do and do not fix.
