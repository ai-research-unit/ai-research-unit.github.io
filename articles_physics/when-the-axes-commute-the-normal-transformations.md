# __When the Axes Commute: The Normal Transformations__

## Introduction

A boost and a rotation commute exactly when their axes are parallel, or when one of the two is the identity. The proof is one line of quaternion algebra, and it gives the exact criterion

$$
[\tilde U_\Psi,\tilde u_{\mathrm r}]=2i\sinh\tfrac{\theta_{\mathrm{rpd}}}{2}\sin\tfrac{\theta_{\mathrm{axr}}}{2}\,\bigl(\vec u_{\mathrm b}\times\vec u_{\mathrm r}\bigr).
$$

The elements of the group that can be written this way are exactly the **normal** elements, those satisfying $\tilde U\tilde U^{*}=\tilde U^{*}\tilde U$. They are the elements that a unitary matrix diagonalises, they form a four-dimensional submanifold rather than a subgroup, and their spectra are read off the two parameters.

This article proves the criterion, describes the normal class, counts its dimensions, computes the spectra, and treats the two exceptional cases: the identity and the half-turn, whose rotor is a pure real quaternion.

The article assumes *The Cartan Decomposition: Every Lorentz Transformation as a Boost and a Rotation* for the word and its uniqueness, *The Spectrum of a Lorentz Rotor: What Two Eigenvalues Leave Undetermined* for the spectral counting, and *The Two Commuting Complex Triples* for the split of the algebra. It feeds *The Four Kinds of Frame Transformation*, which classifies the words the block meets.

## The Commutation Condition

### The Two Factors

$$
\tilde U_\Psi=\cosh\tfrac{\theta_{\mathrm{rpd}}}{2}+i\sinh\tfrac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b},
\qquad
\tilde u_{\mathrm r}=\cos\tfrac{\theta_{\mathrm{axr}}}{2}+\sin\tfrac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r},
$$

with $\vec u_{\mathrm b},\vec u_{\mathrm r}$ real unit vectors, $\vec u^2=-e_t$ for each.

### The Computation

Write $a=\tfrac12\theta_{\mathrm{rpd}}$ and $b=\tfrac12\theta_{\mathrm{axr}}$ for the half-angles, so that

$$
\tilde U_\Psi\tilde u_{\mathrm r}=\cosh a\cos b+\cosh a\sin b\,\vec u_{\mathrm r}+i\sinh a\cos b\,\vec u_{\mathrm b}+i\sinh a\sin b\,\vec u_{\mathrm b}\vec u_{\mathrm r},
$$

and the reversed product differs only in the last term, which becomes $i\sinh a\sin b\,\vec u_{\mathrm r}\vec u_{\mathrm b}$. For two real pure quaternions,

$$
\vec u_{\mathrm b}\vec u_{\mathrm r}-\vec u_{\mathrm r}\vec u_{\mathrm b}=2\,\vec u_{\mathrm b}\times\vec u_{\mathrm r},
$$

so

$$
\tilde U_\Psi\tilde u_{\mathrm r}-\tilde u_{\mathrm r}\tilde U_\Psi
=2i\sinh a\,\sin b\,\bigl(\vec u_{\mathrm b}\times\vec u_{\mathrm r}\bigr).
$$

That is the whole proof, and it is checked numerically to machine precision on random axes and random angles.

### The Three Ways the Commutator Can Vanish

The product $\sinh a\,\sin b\,(\vec u_{\mathrm b}\times\vec u_{\mathrm r})$ vanishes in exactly three ways:

| condition | meaning | which family |
|---|---|---|
| $\vec u_{\mathrm b}\times\vec u_{\mathrm r}=0$ | the axes are parallel or antiparallel | the interesting case |
| $\sinh a=0$, i.e. $a=0$ | the boost is the identity | degenerate |
| $\sin b=0$, i.e. $\theta_{\mathrm{axr}}\in2\pi\mathbb{Z}$ | the rotation is $\pm e_t$ | degenerate |

So "the axes commute" is the statement that the first row holds, and the other two rows are the cases in which one factor is central.

### Why the Sign of the Vector Product Does Not Matter

The commutator is a vector product, and a vector product vanishes for parallel as well as for antiparallel axes. So the condition is that the two axes lie on a common **line**, not that they point the same way. The distinction between parallel and antiparallel does not affect commutation; it affects the sign of the second factor's parameters, and it is the subject of the third section.

## The Parallel Case

### The Statement

If $\vec u_{\mathrm r}=\pm\vec u_{\mathrm b}=\pm\vec u$, both factors are polynomials in $\vec u$ and in $i\vec u$, hence both lie in the two-dimensional commutative subalgebra spanned by $e_t$ and $\vec u$ once complex coefficients are allowed:

$$
\tilde U_\Psi,\ \tilde u_{\mathrm r}\in\operatorname{span}_{\mathbb{C}}\{e_t,\vec u\}.
$$

Two elements of a commutative algebra commute, which is the structural reason the criterion has the form it has.

### The Product

With a common axis $\vec u$,

$$
\tilde U_\Psi\tilde u_{\mathrm r}=\cosh a\cos b+\cosh a\sin b\,\vec u+i\sinh a\cos b\,\vec u+i\sinh a\sin b\,\vec u^{2},
$$

and $\vec u^{2}=-e_t$, so

$$
\tilde U_\Psi\tilde u_{\mathrm r}=\bigl(\cosh a\cos b-i\sinh a\sin b\bigr)e_t+\bigl(\cosh a\sin b+i\sinh a\cos b\bigr)\vec u .
$$

The scalar part is $\cosh a\cos b-i\sinh a\sin b$ for a common axis and $\cosh a\cos b+i\sinh a\sin b$ when the rotation axis is reversed; it is complex, the imaginary part being the cross term the last factor contributes. The vector part mixes a real and an imaginary coefficient. The modulus $N$ is $1$, because both factors have unit modulus, so the two eigenvalues are reciprocals whatever the angles. The element is therefore determined by the two angles and the common axis: **three** parameters, not four.

### The One-Parameter Families

Holding the axis fixed, the family is two-dimensional: one parameter for the boost and one for the rotation. Adding the axis, which is a point of $S^{2}$, gives

$$
\dim\{\text{commuting words}\}=2+2=4,
$$

which is the dimension of the normal elements. The count is taken up in §*The Two-Parameter Family*.

## The Antiparallel Case

### What Changes

If $\vec u_{\mathrm r}=-\vec u_{\mathrm b}$, the rotation factor is $\cos b-\sin b\,\vec u_{\mathrm b}$, which is the rotation about $-\vec u_{\mathrm b}$ by the same angle. So the antiparallel case is the parallel case with the rotation angle measured from the opposite axis, and nothing else changes: the two families coincide as sets.

### The Sign Convention

The block fixes the axis of a rotation to be a unit vector with the angle in $[0,2\pi)$. Reversing the axis and negating the angle gives the same element, so the antiparallel case is a relabelling and not a new family. The one place where the relabelling is not innocuous is the half-turn, where $\sin b=1$ and the two descriptions are $\vec u$ and $-\vec u$; that is the subject of the last section.

### Why It Is Worth Naming

Because the standard statement in the literature is "the axes are parallel", and it is wrong: the correct statement is "the axes are collinear". A reader who takes the literature statement literally will exclude the boost along $+\vec e_z$ with the rotation about $-\vec e_z$, which does commute.

## Why Normal Elements Are the Diagonalisable Ones

### The Spectral Theorem

A complex matrix is unitarily diagonalisable if and only if it is normal. In the algebra the condition is

$$
\tilde U\tilde U^{*}=\tilde U^{*}\tilde U,
$$

and in the word it is exactly the commutation condition above. So:

$$
\tilde U_\Psi\tilde u_{\mathrm r}\ \text{is normal}\iff[\tilde U_\Psi,\tilde u_{\mathrm r}]=0 .
$$

The proof in one direction: a product of two commuting elements that are individually normal is normal. In the other: if the product is normal, the spectral theorem gives it an orthonormal eigenbasis, and the word's two factors are polynomials in the product, hence diagonal in the same basis, hence commuting.

### The Converse, Stated Honestly

The converse requires one extra fact: that the two factors are functions of the product. They are, because the boost factor is the positive Hermitian square root of $\tilde U\tilde U^{*}$ and the rotation factor is $\tilde U$ times its inverse; both depend on $\tilde U$ alone and neither involves a choice. So the spectral theorem applies to both.

### What Fails Without Normality

For a general element there is no orthonormal eigenbasis and no unitary diagonalisation, and the spectrum is not enough even to describe the element's action. *The Spectrum of a Lorentz Rotor: What Two Eigenvalues Leave Undetermined* gives the counting and exhibits the failure; the present article supplies the exact class in which the failure does not occur.

### The Class Is Not a Subgroup

The normal elements are closed under inverses and under conjugation by unitaries, but not under products: the product of two normal elements with different axes is generally not normal, and the failure is the commutator above. So the normal class is a union of conjugacy classes and not a subgroup, and this is why "the normal transformations" is a *kind of transformation* and not a group.

## The Two-Parameter Family

### The Parameters

A normal element with a fixed axis is described by two angles, the rapidity and the rotation angle, both measured in the plane spanned by $e_t$ and the axis. Adding the axis, a point of $S^{2}$, the total is four. That is one dimension fewer than the group's six, and the missing two are exactly the parameters that measure the failure of the two axes to be collinear.

### The Geometry

The normal elements with a given axis form a two-dimensional commutative surface inside the group. It is a cylinder-like surface: one direction is the boost, which is open, the other is the rotation, which is periodic. The whole normal class is the union of these surfaces over the axis sphere, with the surface depending only on the axis *line*, so the fibration is over $\mathbb{RP}^{2}$ and not over $S^{2}$.

### The Manifold

$$
\{\text{normal elements of }G\}\cong\mathbb{R}^{2}\times\mathbb{RP}^{2}
$$

up to the identifications at the degenerate points, of dimension four. The two open directions are the boost rapidity and the two parameters of the axis line, and the compact direction is the rotation angle.

## The Spectra

### The Spectrum of the Product

With a common axis, the element is diagonal in the basis of spin states along that axis, and its two eigenvalues are the products of the two factors' eigenvalues:

$$
\lambda_+=\mu,\qquad \lambda_-=\mu^{-1},\qquad
\mu=\exp\Bigl(\tfrac12\bigl(\theta_{\mathrm{rpd}}-i\theta_{\mathrm{axr}}\bigr)\Bigr),
$$

where the relative sign of the two angles is fixed by the relative sense of the two axes: if the rotation axis is $-\vec u_{\mathrm b}$ the phase is the complex conjugate. The two eigenvalues are then $\mu$ and $\mu^{-1}$, as for every element of determinant one.

### What the Spectrum Shows

The two spectral parameters are now the rapidity and the rotation angle, in an additive combination. So for the normal class the spectrum carries **both** of the physically named numbers, and the axis is the only thing it loses. This is the case in which the phrase "the spectrum of a Lorentz transformation" is nearly honest.

### The Degenerate Case

The eigenvalues coincide exactly when both parameters vanish modulo the periods: $\theta_{\mathrm{rpd}}=0$ and $\theta_{\mathrm{axr}}\in\{0,2\pi\}$, that is at $\pm e_t$. Those are the two central elements, and they are the only points at which the normal surface's spectrum degenerates.

## The Half-Turn

### The Rotation by $\pi$

A rotation by the physical angle $\pi$ has $b=\tfrac{\pi}{2}$, so

$$
\tilde u_{\mathrm r}=\cos\tfrac{\pi}{2}+\sin\tfrac{\pi}{2}\vec u_{\mathrm r}=\vec u_{\mathrm r},
$$

**a pure real quaternion**. The rotor is then an element of the algebra's real vector subspace, of trace zero: it is at once a group element and a generator-shaped object. No other rotation has that property, and that is what makes the half-turn exceptional.

### What the Spectrum Does

The eigenvalues are $e^{\pm i\pi/2}=\pm i$, purely imaginary. So the half-turn is the rotation whose spectrum is as far from real as it can be, and whose rotor is scalar-free.

### What Commutes With It

Since $\sin b=\sin\tfrac{\pi}{2}=1$, a half-turn commutes with a boost only when the axes are collinear. So the half-turn is **not** an exception to the commutation criterion, and a reader who expects it to be should check the algebra rather than the geometry. What commutes with everything is the rotation by $2\pi$, which is $-e_t$ and central.

This is the one place where the menu's "exceptional case where a rotation is by $\pi$" needs a convention stated. In the half-angle convention of this corpus the central rotation is by $2\pi$; the rotation by $\pi$ is exceptional for a different and more useful reason, namely that its rotor is scalar-free and a pure real quaternion. Both statements are true; they are statements about different elements.

### The Reading

The half-turn's rotor being a generator means that a half-turn can be written as $\exp(\tfrac{\pi}{2}\vec u)$ with the exponent a real vector of length $\pi/2$ — the largest distance from the origin at which the rotation chart is still one-to-one along that axis. In the exponential chart of *The Exponential Map from Algebra to Group* the half-turn sits on the sphere where the chart begins to identify points, and that is why a naive logarithm of a half-turn returns an axis whose sign is arbitrary.

## Summary

A boost and a rotation commute exactly when their axes are collinear, or when one factor is the identity. The exact commutator is $2i\sinh\tfrac{\theta_{\mathrm{rpd}}}{2}\sin\tfrac{\theta_{\mathrm{axr}}}{2}(\vec u_{\mathrm b}\times\vec u_{\mathrm r})$. The elements that admit such a word are the normal elements, $\tilde U\tilde U^{*}=\tilde U^{*}\tilde U$, which are exactly the elements that a unitary diagonalises; they form a four-dimensional manifold, not a subgroup, fibred over the axis line. On a normal element the spectrum is $\{e^{(\theta_{\mathrm{rpd}}\pm i\theta_{\mathrm{axr}})/2}\}$ and carries both parameters, losing only the axis. The half-turn is exceptional because its rotor is a pure real quaternion, scalar-free, with spectrum $\pm i$; it is not an exception to the commutation criterion, and the element that commutes with everything is the rotation by $2\pi$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde U_\Psi=\exp(i\tfrac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b})$ | the boost factor, the positive Hermitian one |
| $\tilde u_{\mathrm r}=\exp(\tfrac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r})$ | the rotation factor |
| $a=\tfrac12\theta_{\mathrm{rpd}}$, $b=\tfrac12\theta_{\mathrm{axr}}$ | half-angles |
| $\vec u_{\mathrm b}\times\vec u_{\mathrm r}$ | the vector product that measures the failure of commutation |
| normal | $\tilde U\tilde U^{*}=\tilde U^{*}\tilde U$ |
| $\mathbb{RP}^{2}$ | the space of axis lines |

## Further Reading

- R. A. Horn and C. R. Johnson, *Matrix Analysis*, 2nd ed., Cambridge University Press, 2012 — normal matrices, the spectral theorem, and the unitary diagonalisation.
- S. Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces*, Academic Press, 1978 — the symmetric space of boosts and the role of commuting Cartan directions.
- S. Weinberg, *The Quantum Theory of Fields*, Vol. 1, Cambridge University Press, 1995, §2.4 — the special case of a boost and a rotation about a common axis, which is the case in which the Wigner rotation vanishes.
- *The Cartan Decomposition: Every Lorentz Transformation as a Boost and a Rotation* — the word whose factors are tested here.
- *The Spectrum of a Lorentz Rotor: What Two Eigenvalues Leave Undetermined* — what the spectrum of a normal element does and does not fix.
- *The Four Kinds of Frame Transformation* — the classification of the words into the four cases the block uses.
