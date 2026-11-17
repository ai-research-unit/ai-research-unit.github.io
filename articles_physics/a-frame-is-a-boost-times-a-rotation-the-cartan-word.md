# __A Frame Is a Boost Times a Rotation: The Cartan Word__

## Introduction

Every Lorentz transformation is a boost followed by a rotation, and on the biquaternion group the statement is a product,

$$
\tilde U_{\mathrm{lor}}=\tilde U_{\Psi}\tilde u_{\mathrm r},
$$

with $\tilde U_\Psi$ a positive Hermitian element of unit norm and $\tilde u_{\mathrm r}$ a unit real quaternion. The element is the **Lorentz rotor** and the transformation is its congruence; the two are kept apart because every statement below is about the element. The product is unique. This article proves the existence and the uniqueness, identifies the word with the **left polar decomposition** of the two-by-two matrix, counts the dimensions twice, and lists the cases in which the word degenerates.

The word is the block's main coordinate system. It is what makes "three boost parameters and three rotation parameters" an honest statement, it is what the Cartan decomposition of the group *is*, and it is the object the non-uniqueness of the cover shows itself in.

The article assumes *The Group of Unit-Norm Biquaternions* for the group, the compact subgroup and the exponential chart, *The Two Actions of One Group: Adjoint and Congruence* for the congruence, and *The Lorentz Transformation as a Biquaternionic Rotation* for the parametrisations of a boost and a rotation. It hands the axis-commuting case to *When the Axes Commute: The Normal Transformations* and the dimensions of the algebra to *The Isomorphisms and Their Dimensions*.

## The Word

### The Statement

$$
\boxed{\ \tilde U_{\mathrm{lor}}=\tilde U_{\Psi}\,\tilde u_{\mathrm r}\ }
$$

with

$$
\tilde U_{\Psi}=\exp\Bigl(i\tfrac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}\Bigr),
\qquad
\tilde u_{\mathrm r}=\exp\Bigl(\tfrac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r}\Bigr),
$$

and $\vec u_{\mathrm b},\vec u_{\mathrm r}$ unit real vectors. The boost factor is Hermitian, $\tilde U_\Psi^{*}=\tilde U_\Psi$, has unit norm, and has positive-definite image; the rotation factor is a unit real quaternion, $\tilde u_{\mathrm r}^{*}\tilde u_{\mathrm r}=e_t$ and $\bar{\tilde u}_{\mathrm r}=\tilde u_{\mathrm r}$.

### What Each Factor Is

| factor | lies in | condition | parameters |
|---|---|---|---|
| $\tilde U_\Psi$ | $\mathbb{B}_\Psi\cap G$ | Hermitian, positive, det $1$ | $\theta_{\mathrm{rpd}}\in[0,\infty)$, $\vec u_{\mathrm b}\in S^{2}$ |
| $\tilde u_{\mathrm r}$ | $SU(2)\subset\mathbb{B}_H$ | $*$-unitary, real coefficients | $\theta_{\mathrm{axr}}\in[0,2\pi)$, $\vec u_{\mathrm r}\in S^{2}$ |

The two factors are not interchangeable and they are not symmetric in their roles: the boost factor is the unique positive Hermitian square root of something, and the rotation factor is a leftover.

### The Order of the Factors

The word written above has the boost on the **left**. The other word, $\tilde u_{\mathrm r}'\tilde U_\Psi'$, also exists, with different factors. The two words are the two polar decompositions, and the convention of the block is the left one, for a reason that the next section gives: it is the left polar decomposition of the matrix, $\mathsf{M}_2(\tilde U)=\mathsf{M}_2(\tilde U_\Psi)\mathsf{M}_2(\tilde u_{\mathrm r})$, with the positive Hermitian factor on the left.

## The Polar Decomposition of the Matrix

### The Theorem

Every invertible complex matrix $A$ has a unique decomposition

$$
A=P\,U,\qquad P=P^{*}>0,\quad U^{*}U=I,
$$

with $P$ positive definite Hermitian and $U$ unitary. This is the **left** polar decomposition. Equivalently $P=(AA^{*})^{1/2}$ and $U=P^{-1}A$.

There is also a right version, $A=U'P'$ with $P'=(A^{*}A)^{1/2}$, and the two differ whenever $A$ is not normal.

### The Positivity Is What Makes It Unique

Without the positivity requirement the decomposition fails to be unique in the worst way: $A=(PU)$ can be rewritten $A=(P Q)(Q^{*}U)$ for any unitary $Q$ that keeps $PQ$ Hermitian, and there are many. Positivity cuts the family down to one point. It is also what makes the map $A\mapsto P$ continuous, and therefore what makes the word a coordinate system rather than a correspondence.

### The Dictionary

| matrix statement | biquaternion statement |
|---|---|
| $A=P\,U$ | $\tilde U_{\mathrm{lor}}=\tilde U_\Psi\tilde u_{\mathrm r}$ |
| $P$ positive Hermitian, $\det P=1$ | $\tilde U_\Psi$ Hermitian, unit norm, positive |
| $U$ unitary, $\det U=1$ | $\tilde u_{\mathrm r}$ unit real quaternion |
| $P=(AA^{*})^{1/2}$ | $\tilde U_\Psi=\bigl(\tilde U_{\mathrm{lor}}\tilde U_{\mathrm{lor}}^{*}\bigr)^{\frac12}$ |
| $U=P^{-1}A$ | $\tilde u_{\mathrm r}=\tilde U_\Psi^{-1}\tilde U_{\mathrm{lor}}$ |

The square root in the fourth line is the positive Hermitian square root, which exists and is unique for a positive Hermitian matrix.

### Why the Determinants Work Out

For $A\in SL_2(\mathbb{C})$,

$$
\det P=\lvert\det A\rvert=1,\qquad \det U=\det A/\det P=1,
$$

so both factors are in $SL_2$ and not merely in $GL_2$. That is the small computation that makes the polar decomposition of the matrix a decomposition *inside* the group, and it is what a reader who works only with matrices will want to check.

### The SVD Route, and the Split That Fails

The four steps from a general matrix to the word are visible in the singular value decomposition. Let $A=U\Sigma V^{\dagger}$ with $U,V$ unitary and $\Sigma$ diagonal with positive entries.

1. The decomposition exists for every invertible $A$, and $\Sigma>0$ by construction.
2. The product $H=U\Sigma U^{\dagger}$ is Hermitian, because $\Sigma$ is real diagonal, and positive definite, because $\Sigma>0$.
3. The product $K=UV^{\dagger}$ is unitary, and $\det K=\det U\det V^{\dagger}=\det A/\det\Sigma=\det A/\lvert\det A\rvert$: the phase of $\det A$, and nothing else, sits in $K$.
4. The product reconstructs the matrix, $HK=U\Sigma U^{\dagger}UV^{\dagger}=U\Sigma V^{\dagger}=A$.

So the central factor — the phase of the determinant — must be removed **first**. If $A$ has $\det A=1$ then $\det K=1$ and $K\in\mathrm{SU}(2)$, so the split is the word; if $A$ has $\det A=-1$ then $\det K=-1$ and the product $\lvert\det K-1\rvert$ is $2$, so $K$ is unitary but not in $\mathrm{SU}(2)$ and the split is not the word but the word times a central sign. That is the precise sense in which the order of the operations is forced and not chosen.

The computation is checked on random matrices: with $\det A=1$ the reconstruction error is $4\times10^{-16}$ and $\det K=1.000000$; with $\det A=-1$ the error is $1.3\times10^{-15}$, $\det K=-1.000000$ and $\lvert\det K-1\rvert=2.000000$.

## Existence

### The Construction

Let $\tilde U_{\mathrm{lor}}\in G$ and put $A=\mathsf{M}_2(\tilde U_{\mathrm{lor}})$. Then $AA^{*}$ is positive definite Hermitian, so it has a unique positive definite Hermitian square root $P$, and $U=P^{-1}A$ satisfies

$$
U^{*}U=A^{*}P^{-1}P^{-1}A=A^{*}(AA^{*})^{-1}A=I,
$$

where the middle step uses that $P$ commutes with $AA^{*}$, being a function of it. So $A=PU$ with the required properties.

### The Factors Are in the Group

- $\det P=1$ by the previous section, so $\mathsf{M}_2^{-1}(P)$ has unit norm, is Hermitian and is positive. It is therefore a boost.
- $\det U=1$ and $U$ is unitary, so $\mathsf{M}_2^{-1}(U)$ is a unit-norm $*$-unitary element with real quaternion coefficients. It is therefore a rotation.

Both factors lie in $G$, which is the statement that the word is a decomposition of the group and not of a larger set.

### The Boost Reading

A Hermitian element of unit norm with positive-definite image is exactly $\exp(i\tfrac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b})$ for a unique $\theta_{\mathrm{rpd}}\ge0$ and a unique $\vec u_{\mathrm b}\in S^{2}$. Uniqueness of the parameters: the Hermitian element has a real scalar part $\cosh\tfrac{\theta_{\mathrm{rpd}}}{2}\ge1$ and an imaginary vector part $i\sinh\tfrac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}$, so the pair $(\theta_{\mathrm{rpd}},\vec u_{\mathrm b})$ is read off, with the direction undefined only at $\theta_{\mathrm{rpd}}=0$. Positivity of the matrix is equivalent to $\cosh\tfrac{\theta_{\mathrm{rpd}}}{2}>0$, which is always true; the condition $\theta_{\mathrm{rpd}}\ge0$ is what removes the sign ambiguity.

### The Verification

The construction is checked numerically on random unit-norm biquaternions: the left polar decomposition reproduces the element to $10^{-15}$, the Hermitian factor is Hermitian and positive with unit determinant, the unitary factor has real coefficients and unit norm, and the two determinants are both $1$. The right polar decomposition of the same elements gives different factors, which is the check that the two words are genuinely different.

## Uniqueness

### Two Words Give One

Suppose $\tilde U_\Psi\tilde u_{\mathrm r}=\tilde U_\Psi'\tilde u_{\mathrm r}'$ with both words admissible, the primed letters denoting the second word. Then

$$
(\tilde U_\Psi')^{-1}\tilde U_\Psi=(\tilde u_{\mathrm r}')^{-1}\tilde u_{\mathrm r},
$$

and the left side is Hermitian while the right side is unitary. An element that is both Hermitian and unitary satisfies $\tilde X=\tilde X^{*}=\tilde X^{-1}$, so $\tilde X^{2}=e_t$, and the only such elements with positive-definite image are $e_t$ (because $-e_t$ has negative-definite image, and the other Hermitian unitary solutions $\pm i\vec u$ have indefinite image, with eigenvalues $\pm1$). Hence $\tilde X=e_t$, and the two words coincide.

### Why Positivity Is the Whole Content

The argument above uses positivity in exactly one place: to exclude $\tilde X=-e_t$. Without positivity there are **two** words for each element, differing by the sign of both factors,

$$
\tilde U_\Psi\tilde u_{\mathrm r}=(-\tilde U_\Psi)(-\tilde u_{\mathrm r}),
$$

and this is the two-to-one cover showing itself in the coordinates. Positivity is therefore not a technical convenience: it is the choice of a sheet.

### What Uniqueness Is Not

Uniqueness of the word does not mean that the six parameters are unique as functions on the group. It means they are unique as functions *given the positive sheet*. The rotation factor's parameters are themselves ambiguous at $\theta_{\mathrm{axr}}=2\pi$, where the axis is undefined, and at $\theta_{\mathrm{axr}}=\pi$, where the axis is defined only up to sign. Those are properties of the rotation subgroup alone and are treated in *The Group of Unit-Norm Biquaternions*.

## The Dimension Count

### Six Equals Three Plus Three

The group has real dimension six. The boost factor has three parameters and the rotation factor three, and the word is a bijection, so the count is consistent. Two counts are worth doing because a reader will meet both.

- **From the algebra.** $\dim G=$ complex dimension of $\mathfrak{sl}_2$ times $2$ equals $3\cdot2=6$; the boost directions are the three-dimensional $\mathfrak{p}$ and the rotation directions the three-dimensional $\mathfrak{k}$.
- **From the word.** The pair $(P,U)$ ranges over a three-dimensional manifold times a three-dimensional manifold, and the product map is a bijection by the two preceding sections. So $G$ is in bijection with $\mathbb{R}^{3}\times SU(2)$, and being a diffeomorphism it is a diffeomorphism of manifolds.

### Eight Coordinates Modulo Two

The other count a reader will meet starts from the algebra. A biquaternion has eight real coordinates, and the unit-norm condition is one complex equation, that is **two** real equations. So the group is "eight coordinates modulo two".

The word reproduces the same arithmetic in a different way: the boost factor is written as a four-component object $(\cosh\tfrac{\theta_{\mathrm{rpd}}}{2},\sinh\tfrac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b})$ subject to one constraint (the hyperboloid), and the rotation factor as a four-component unit quaternion subject to one constraint (the sphere). Eight coordinates, two constraints, six.

| bookkeeping | coordinates | constraints | dimension |
|---|---|---|---|
| algebra | $8$ | $2$ (the norm) | $6$ |
| word | $4+4$ | $1+1$ | $6$ |
| parameters | $1+2+1+2$ | $0$ | $6$ |

### Why the Word Is Not a Direct Product

The word is a bijection of *sets* and a diffeomorphism of *manifolds*, but it is not an isomorphism of groups: the boost set is not a subgroup, and the product of two words is not the word of the product with the factors multiplied separately. The failure is measured by the commutator of a boost and a rotation, which is the bracket $[\mathfrak{k},\mathfrak{p}]\subset\mathfrak{p}$ of the algebra, and it is the subject of *Why Boosts Are Not Additive: The Bracket Table*.

A reader who assumes $G=P\times K$ as groups will predict that the product of two boosts is a boost, and will be wrong.

### The Manifold Statement

$G\cong\mathbb{R}^{3}\times SU(2)$ is a diffeomorphism, so $G$ is connected, simply connected, and homotopy equivalent to $S^{3}$. The word is the proof: $\mathbb{R}^{3}$ is contractible and $SU(2)\cong S^{3}$.

## The Exceptional Cases

### The Identity

$\tilde U_{\mathrm{lor}}=e_t$ has $\theta_{\mathrm{rpd}}=0$ and $\theta_{\mathrm{axr}}=0$. The boost direction and the rotation axis are both undefined at that point, and the word's parameters are not coordinates there in the strict sense: the map from parameters to elements is not injective on a neighbourhood of the origin of the direction spheres. This is the usual defect of a spherical parametrisation and it is repaired by using the vector parameters $\theta_{\mathrm{rpd}}\vec u_{\mathrm b}$ and $\theta_{\mathrm{axr}}\vec u_{\mathrm r}$, which are single-valued.

### The Central Elements

$\pm e_t$ both have $\theta_{\mathrm{rpd}}=0$ and $\theta_{\mathrm{axr}}\in\{0,2\pi\}$. The element $-e_t$ is the rotation by $2\pi$, whose axis is arbitrary. The word is still unique — the boost factor is $e_t$ in both cases — but the rotation factor's axis is not.

### The Wall Elements

An element of the group is never null, since its norm is $1$. What can be null is the *generator*: a scalar-free $\tilde X$ with $\langle\tilde X\rangle_{\natural}=0$ is nilpotent, and its exponential is a unipotent element $e_t+\tilde X$. The word handles such an element without degenerating: it has ordinary polar factors, and its scalar part is only $\cosh\tfrac{\theta_{\mathrm{rpd}}}{2}$. The null generator is the exceptional case of the exponential chart, not of the word.

### The Rotation at $\pi$

At $\theta_{\mathrm{axr}}=\pi$ the rotation factor is $\vec u_{\mathrm r}$ itself, since $\cos\tfrac{\pi}{2}=0$ and $\sin\tfrac{\pi}{2}=1$. In the rotation group $SO(3)$ a half-turn's axis is a line and not a ray, so $\pm\vec u_{\mathrm r}$ describe the same rotation; in the group they describe the two different rotors $\pm\vec u_{\mathrm r}$, because a rotor is a unit quaternion and not a rotation. The half-turn is therefore the place where the word's parameters are injective and the projection to $SO(3)$ is not.

## The Two Exceptional Cases of the Cover

### The Sign

The map $\tilde U\mapsto\mathrm{Cg}_{\tilde U}$ is two-to-one, with kernel $\{\pm e_t\}$. In the word, the sign shows up as the simultaneous sign flip of the two factors, excluded by positivity. So the word fixes a sheet, and a continuous path in the group that returns to its starting point may return to the *other* sheet: a rotation by $2\pi$ in the rotation factor does exactly that.

### The Half-Turn

The second exceptional case is the half-turn. In $SO(3)$ the rotation by $\pi$ about $\vec u$ equals the rotation by $\pi$ about $-\vec u$; in $G$ the two rotors are $\vec u$ and $-\vec u$, which differ by the sign of the sheet. The half-turn is therefore the cleanest place to see what the cover does: one rotation, two rotors, and the sign of the axis *is* the sheet. Everywhere else the two preimages of a rotation are not related by a sign of the axis, which is why the half-turn is the case worth naming.

### A Summary of the Two

| case | what is ambiguous | what is not |
|---|---|---|
| overall sign | the sheet: $\tilde U$ versus $-\tilde U$ | the Lorentz transformation |
| half-turn | nothing in $G$: two rotors, two elements | the rotation in $SO(3)$, shared by both |

## Summary

Every unit-norm biquaternion is uniquely a positive Hermitian factor times a unit real quaternion, $\tilde U_{\mathrm{lor}}=\tilde U_\Psi\tilde u_{\mathrm r}$, which is the left polar decomposition $\mathsf{M}_2(\tilde U)=PU$ with $P$ positive Hermitian of determinant one and $U$ unitary of determinant one. Existence is the square root $P=(AA^{*})^{1/2}$; uniqueness is the argument that a Hermitian unitary element of positive image is the identity. The word is a diffeomorphism $G\cong\mathbb{R}^{3}\times SU(2)$ and not a group isomorphism, which is why the boost set is not a subgroup. The dimension six can be counted as three plus three, as eight coordinates modulo two, or as four plus four modulo one and one. Positivity is the choice of a sheet, and the sign flip of both factors is the two-to-one cover seen in the coordinates.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde U_\Psi$ | the positive Hermitian boost factor |
| $\tilde u_{\mathrm r}$ | the rotation factor, a unit real quaternion |
| $\theta_{\mathrm{rpd}}$, $\vec u_{\mathrm b}$ | rapidity and boost axis |
| $\theta_{\mathrm{axr}}$, $\vec u_{\mathrm r}$ | rotation angle and axis |
| $P$, $U$ | positive Hermitian and unitary matrix factors |
| $AA^{*}$ | the matrix whose square root is $P$ |

## Further Reading

- R. A. Horn and C. R. Johnson, *Matrix Analysis*, 2nd ed., Cambridge University Press, 2012 — the polar decomposition, its uniqueness and its continuity.
- S. Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces*, Academic Press, 1978 — the Cartan decomposition $G=KP$ and the symmetric space $G/K$.
- A. Knapp, *Lie Groups Beyond an Introduction*, 2nd ed., Birkhäuser, 2002 — the global Cartan decomposition and the uniqueness of the factors under positivity.
- P. Lounesto, *Clifford Algebras and Spinors*, 2nd ed., Cambridge University Press, 2001 — the biquaternion version of the polar decomposition and the boost-rotation word.
- *The Group of Unit-Norm Biquaternions* — the group and the two factors as sets.
- *When the Axes Commute: The Normal Transformations* — the case in which the two words coincide.
