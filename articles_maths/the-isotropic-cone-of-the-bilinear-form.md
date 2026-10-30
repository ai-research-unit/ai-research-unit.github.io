# __The Isotropic Cone of the Bilinear Form on $\mathbb{C}^2$__

## Introduction

The complex bilinear form
$$
B(Q_1,Q_2)=Q_{1\blacktriangle}Q_{2\blacktriangle}+Q_{1\blacktriangledown}Q_{2\blacktriangledown}
$$
is symmetric and nondegenerate, and it is indefinite: there are nonzero vectors $Q$ with $B(Q,Q)=0$. The set of those vectors is the **isotropic cone**
$$
\mathcal{N}=\{Q\in\mathbb{C}^2:B(Q,Q)=0\}=\{Q:Q_{\blacktriangle}^2+Q_{\blacktriangledown}^2=0\}.
$$
The equation factors over $\mathbb{C}$,
$$
Q_{\blacktriangle}^2+Q_{\blacktriangledown}^2=(Q_{\blacktriangle}+iQ_{\blacktriangledown})(Q_{\blacktriangle}-iQ_{\blacktriangledown}),
$$
so the cone is the union of two complex lines. **This is the first place where the complex bilinear form differs sharply from the Hermitian form**: the Hermitian form is definite and has no isotropic vectors, the symplectic form is nondegenerate and has many isotropic subspaces (every complex line is isotropic for it), while $B$ has exactly two isotropic lines.

This article treats the cone, its two lines, its real picture, its image in $\mathbb{CP}^1$, its Hopf link on $S^3$, and its comparison with the null quadric of the split-complex numbers. The forms are from *The Three Canonical Forms on $\mathbb{C}^2$*; the subspaces and the Lagrangian lines are from *The Subspaces of $\mathbb{C}^2$*; the sphere and the Hopf fibration are from *The Unit Sphere and the Hopf Fibration*; the split-complex numbers are from *Split-Complex Numbers*.

**The cone is a reducible quadric: two complex lines meeting at the origin.** Its real locus is only the origin, but its real picture is the union of two real two-planes in $\mathbb{R}^4$. Its projective image is two points of $\mathbb{CP}^1$, and its intersection with $S^3$ is a pair of great circles forming the Hopf link.

## The Bilinear Form and the Cone

**The form $B$ has signature $(2,2)$ over the reals, and its complex isotropic cone is the zero set of a reducible quadratic form.**

**Definition.** The **complex bilinear form** is
$$
B(Q_1,Q_2)=Q_{1\blacktriangle}Q_{2\blacktriangle}+Q_{1\blacktriangledown}Q_{2\blacktriangledown},
$$
and the **isotropic cone** is $\mathcal{N}=\{Q:B(Q,Q)=0\}$.

**Proposition (the signature).** As a real bilinear form on $\mathbb{C}^2\cong\mathbb{R}^4$, the real part
$$
\operatorname{Re}B(Q_1,Q_2)=q_{\blacktriangle}u_{\blacktriangle}-q'_{\blacktriangle}v_{\blacktriangle}+q_{\blacktriangledown}u_{\blacktriangledown}-q'_{\blacktriangledown}v_{\blacktriangledown}
$$
has signature $(2,2)$, and the imaginary part
$$
\operatorname{Im}B(Q_1,Q_2)=q_{\blacktriangle}v_{\blacktriangle}+q'_{\blacktriangle}u_{\blacktriangle}+q_{\blacktriangledown}v_{\blacktriangledown}+q'_{\blacktriangledown}u_{\blacktriangledown}
$$
also has signature $(2,2)$. The complex form $B$ is nondegenerate, symmetric and $\mathbb{C}$-bilinear.

*Proof.* In the real coordinates $(q_{\blacktriangle},q'_{\blacktriangle},q_{\blacktriangledown},q'_{\blacktriangledown})$ the matrix of $\operatorname{Re}B$ is $\operatorname{diag}(1,-1,1,-1)$, of signature $(2,2)$; the matrix of $\operatorname{Im}B$ is the symmetric matrix with blocks $\begin{pmatrix}0&1\\1&0\end{pmatrix}$, whose eigenvalues are $\pm1$. The complex form is nondegenerate because its matrix is the identity.

**Proposition (the factorization).** The cone is the union of the two complex lines
$$
L_+=\{Q:Q_{\blacktriangle}=iQ_{\blacktriangledown}\},\qquad L_-=\{Q:Q_{\blacktriangle}=-iQ_{\blacktriangledown}\}.
$$
The two lines are distinct, they meet only at the origin, and $\mathcal{N}=L_+\cup L_-$.

*Proof.* $Q_{\blacktriangle}^2+Q_{\blacktriangledown}^2=(Q_{\blacktriangle}+iQ_{\blacktriangledown})(Q_{\blacktriangle}-iQ_{\blacktriangledown})$, and $\mathbb{C}[Q_{\blacktriangle},Q_{\blacktriangledown}]$ is an integral domain, so the product vanishes exactly when one factor does. The lines $Q_{\blacktriangle}=iQ_{\blacktriangledown}$ and $Q_{\blacktriangle}=-iQ_{\blacktriangledown}$ are distinct and intersect at the origin.

**Remark (the cone is singular).** The cone is a complex algebraic hypersurface of degree $2$, and it is singular at the origin: the two lines meet there, and the Zariski tangent space at the origin is the whole of $\mathbb{C}^2$. **The cone is not a complex manifold at the origin**, and the two lines are its two irreducible components.

## The Two Isotropic Lines

**The two isotropic lines are complex lines, hence real two-planes; each is totally isotropic for $B$ and Lagrangian for the holomorphic symplectic form $\omega$.**

**Proposition (the lines are isotropic).** For $Q_1\in L_\pm$ and $Q_2\in L_\pm$, $B(Q_1,Q_2)=0$. Hence each line is totally isotropic for $B$.

*Proof.* On $L_+$, $Q_{1\blacktriangle}=iQ_{1\blacktriangledown}$ and $Q_{2\blacktriangle}=iQ_{2\blacktriangledown}$, so $B(Q_1,Q_2)=Q_{1\blacktriangle}Q_{2\blacktriangle}+Q_{1\blacktriangledown}Q_{2\blacktriangledown}=(i^2+1)Q_{1\blacktriangledown}Q_{2\blacktriangledown}=0$. The same computation with $Q_{1\blacktriangle}=-iQ_{1\blacktriangledown}$ gives $L_-$.

**Proposition (the lines are Lagrangian for $\omega$).** Each complex line is Lagrangian for the holomorphic symplectic form $\omega$ of *The Three Canonical Forms on $\mathbb{C}^2$*: $\omega$ vanishes on it, and its real dimension is half the real dimension of $\mathbb{C}^2$.

*Proof.* The form $\omega$ is a $(2,0)$-form, and a $(2,0)$-form vanishes on every complex line because the line has only one holomorphic direction. The real dimension of a complex line is $2$, half of the real dimension $4$ of $\mathbb{C}^2$.

**Remark (the contrast with the Hermitian form and with $\omega$).** The Hermitian form $H$ is positive definite, so it has no isotropic vectors; the holomorphic symplectic form $\omega$ has every complex line as an isotropic subspace, and its isotropic vectors are exactly the points of those lines; the bilinear form $B$ has exactly two isotropic lines. **The three forms therefore have three different isotropic geometries**, and the cone of $B$ is the only one that is a proper algebraic subvariety. The Kähler form $\Omega$ of *The Flat Kähler Structure of $\mathbb{C}^2$* is a fourth object: it has no isotropic vectors, and its Lagrangian planes are the totally real planes, not the complex lines.

**Remark (the stabilizer of the cone).** The complex orthogonal group $O(2,\mathbb{C})$ of *The Classical Groups of $\mathbb{C}^2$* preserves $B$, hence preserves the cone and permutes its two lines. **The subgroup preserving each line is the identity component $\mathbb{C}^{\times}$ of $O(2,\mathbb{C})$, and the full group exchanges the two lines through the swap of the two isotropic coordinates, an element of determinant $-1$.**

## The Real Picture

**The real locus of the cone is only the origin, but the underlying real algebraic set is the union of two real two-planes in $\mathbb{R}^4$, and the cone is the intersection of the null cones of $\operatorname{Re}B$ and $\operatorname{Im}B$.**

**Proposition (the real locus).** The real points of $\mathcal{N}$ are
$$
\mathcal{N}\cap\mathbb{R}^2=\{0\}.
$$

*Proof.* For real $Q_{\blacktriangle},Q_{\blacktriangledown}$, the equation $Q_{\blacktriangle}^2+Q_{\blacktriangledown}^2=0$ forces $Q_{\blacktriangle}=Q_{\blacktriangledown}=0$.

**Proposition (the real picture).** The complex lines $L_\pm$ are real two-planes in $\mathbb{R}^4$, and
$$
\mathcal{N}=L_+\cup L_-
$$
as a real algebraic set. The two planes meet only at the origin, and together they form a cone of real dimension $2$ inside $\mathbb{R}^4$.

*Proof.* A complex line is a real two-plane, because it is closed under multiplication by $i$. The union is the cone, and the intersection is the origin because the lines are distinct.

**Proposition (the intersection of two null cones).** The cone $\mathcal{N}$ is the intersection of the real null cone of $\operatorname{Re}B$ and the real null cone of $\operatorname{Im}B$:
$$
\mathcal{N}=\{Q:\operatorname{Re}B(Q,Q)=0\}\cap\{Q:\operatorname{Im}B(Q,Q)=0\}.
$$

*Proof.* $B(Q,Q)=0$ exactly when its real and imaginary parts vanish.

**Remark (the real picture of the split-complex cone).** The split-complex numbers have the norm $x^2-y^2$, whose null quadric is the union of the two real lines $x=\pm y$. **The complex cone of $B$ is the complexification of that real quadric**: after the complex change of variable $Q_{\blacktriangledown}\mapsto iQ_{\blacktriangledown}$, the equation $Q_{\blacktriangle}^2+Q_{\blacktriangledown}^2=0$ becomes $Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2=0$, the complexification of $x^2-y^2=0$. The real picture gains one dimension: the two real lines become two real planes.

**Remark (the cone and the complex structure).** The cone is invariant under $J$, because $B(JQ_1,JQ_2)=-B(Q_1,Q_2)$ and the zero set is unchanged; each of the two lines is $J$-invariant, since it is a complex line. **The cone is therefore a complex subvariety, not merely a real one**, and its real picture is the union of the two $J$-invariant planes.

## The Projective Image

**The image of the cone in $\mathbb{CP}^1$ is the two-point set of the isotropic directions; the projective quadric is reducible and degenerate.**

**Proposition (the image).** The projection $\mathbb{C}^2\setminus\{0\}\to\mathbb{CP}^1$ sends the cone to the two points
$$
[i:1],\qquad [-i:1].
$$
The projective quadric $\{Q_{\blacktriangle}^2+Q_{\blacktriangledown}^2=0\}\subset\mathbb{CP}^1$ is exactly this two-point set.

*Proof.* A point of $L_+$ is $(iQ_{\blacktriangledown},Q_{\blacktriangledown})$ with $Q_{\blacktriangledown}\neq0$, whose class is $[i:1]$; a point of $L_-$ gives $[-i:1]$. The homogeneous equation $Q_{\blacktriangle}^2+Q_{\blacktriangledown}^2=0$ has the two solutions $[Q_{\blacktriangle}:Q_{\blacktriangledown}]=[\pm i:1]$.

**Remark (the degeneracy).** A nondegenerate conic in $\mathbb{CP}^2$ is a smooth curve of genus zero; **the quadric of $B$ in $\mathbb{CP}^1$ is reducible**, two points, because a binary quadratic form over $\mathbb{C}$ factors into two linear forms. The two points are the two isotropic directions, and in $\mathbb{CP}^1$ they are the whole projective image of the cone.

**Remark (the two points and the two lines).** The correspondence is the projectivization of the two isotropic lines: **the cone is the union of the two lines through the origin over the two points, and its projectivization is the two-point set.** The cone is the simplest example of a reducible projective quadric.

## The Hopf Link

**The intersection of the cone with the unit sphere is a pair of great circles, and the two circles are linked with linking number one: they form the Hopf link.**

**Proposition (the intersection with $S^3$).** The intersection $\mathcal{N}\cap S^3$ is the union of the two circles
$$
C_+=\{(iQ_{\blacktriangledown},Q_{\blacktriangledown}):\lvert Q_{\blacktriangledown}\rvert=1/\sqrt2\},\qquad
C_-=\{(-iQ_{\blacktriangledown},Q_{\blacktriangledown}):\lvert Q_{\blacktriangledown}\rvert=1/\sqrt2\}.
$$
Each circle is a fibre of the Hopf fibration $S^3\to\mathbb{CP}^1=S^2$, over the points $[i:1]$ and $[-i:1]$.

*Proof.* On $L_+$, a point is $(iQ_{\blacktriangledown},Q_{\blacktriangledown})$; its norm is $\sqrt{2}\lvert Q_{\blacktriangledown}\rvert$, so it lies on $S^3$ exactly when $\lvert Q_{\blacktriangledown}\rvert=1/\sqrt2$. The fibres of the Hopf fibration are the intersections of the complex lines through the origin with $S^3$, and the two lines are the fibres over the two projective points.

**Theorem (the linking number).** The two circles $C_+$ and $C_-$ have linking number $1$.

*Proof.* The linking number of two fibres of the Hopf fibration over distinct points of $S^2$ is $1$; this is proved in *The Unit Sphere and the Hopf Fibration* by projecting one fibre to the other and computing the intersection number, or by the Gauss integral.

**Remark (the cone as a real surface).** The intersection $\mathcal{N}\cap S^3$ is a pair of circles, and the cone itself is the union of the two planes. **The Hopf link is the boundary of the cone at infinity**, and it is the simplest nontrivial link: two circles that cannot be separated without crossing.

**Remark (the isotropic lines and the Hopf fibration).** Every complex line through the origin meets $S^3$ in a Hopf fibre, and the Hopf fibration is the projectivization of $\mathbb{C}^2\setminus\{0\}$. **The isotropic lines are two special fibres**, the fibres over the two points where the projective quadric meets the projective line; the other fibres are not isotropic for $B$.

## The Split-Complex Comparison

**The complex isotropic cone of $B$ is the complexification of the split-complex null quadric; the dual numbers give the degenerate case of a double line, and the three cases are the three real forms of the same quadratic equation.**

**Definition.** The **split-complex numbers** are $\mathbb{R}[j]$ with $j^2=1$; the **null quadric** is the set of $x+yj$ with $x^2-y^2=0$.

**Proposition (the four readings).** The equation $u^2+v^2=0$ has four readings:
$$
\begin{aligned}
\text{real: } & u^2+v^2=0 \quad\text{(only the origin)},\\
\text{split-complex: } & u^2-y^2=0 \quad\text{(two real lines)},\\
\text{complex: } & Q_{\blacktriangle}^2+Q_{\blacktriangledown}^2=0 \quad\text{(two complex lines)},\\
\text{dual: } & u^2=0 \quad\text{(the axis, doubled)}.
\end{aligned}
$$
The split form is a real form of the complex form under the real structure $Q_{\blacktriangledown}=iy$; the definite form is the real form under $Q_{\blacktriangledown}=v$ real; the dual case is a degeneration, not a real form.

*Proof.* The dual numbers have $v^2=0$ and the equation reduces to $u^2=0$; the split-complex numbers have $j^2=1$ and the equation factors as $(u-y)(u+y)=0$; the complex numbers have $i^2=-1$ and the equation factors as $(Q_{\blacktriangle}+iQ_{\blacktriangledown})(Q_{\blacktriangle}-iQ_{\blacktriangledown})=0$. The change $Q_{\blacktriangledown}\mapsto iy$ carries the complex equation to $u^2-y^2=0$.

**Remark (the real forms).** The complex quadratic form $Q_{\blacktriangle}^2+Q_{\blacktriangledown}^2$ has two real forms: the **definite** form $x_1^2+x_2^2$, which has no nonzero isotropic vectors, and the **split** form $x_1^2-y^2$, which has two isotropic lines. **The complex cone is the complexification of the split cone**, and the definite real form sees only the origin. The dual case is the degeneration in which the two lines coincide.

**Remark (the comparison with the dual numbers).** The dual numbers have $\epsilon^2=0$ and the null cone is the axis, counted twice. **The complex cone is the split case, not the dual case**: the equation is nondegenerate, and the cone has two distinct irreducible components. The dual case is the degeneration in which the two lines coincide; it is the subject of *Dual Numbers* and of *The Dual-Numbers Null Quadric and Projective Geometry*.

## Summary

The complex bilinear form $B(Q_1,Q_2)=Q_{1\blacktriangle}Q_{2\blacktriangle}+Q_{1\blacktriangledown}Q_{2\blacktriangledown}$ has signature $(2,2)$ over the reals, and its isotropic cone $\mathcal{N}=\{Q_{\blacktriangle}^2+Q_{\blacktriangledown}^2=0\}$ is the union of the two complex lines $Q_{\blacktriangle}=\pm iQ_{\blacktriangledown}$. The lines are totally isotropic for $B$ and Lagrangian for the holomorphic symplectic form $\omega$; the Hermitian form $H$ is definite and has no isotropic vectors, so the three forms have three different isotropic geometries.

The real locus of the cone is only the origin, but the cone as a real algebraic set is the union of two real two-planes in $\mathbb{R}^4$, and it is the intersection of the null cones of the real and imaginary parts of $B$. Its projective image is the two-point set $\{[i:1],[-i:1]\}\subset\mathbb{CP}^1$. Its intersection with $S^3$ is a pair of great circles, the Hopf fibres over the two points, and they form the Hopf link with linking number one. The cone is the complexification of the split-complex null quadric $x^2-y^2=0$; the dual numbers give the degenerate case of a double line.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $B(Q_1,Q_2)=Q_{1\blacktriangle}Q_{2\blacktriangle}+Q_{1\blacktriangledown}Q_{2\blacktriangledown}$ | the complex bilinear form |
| $H(Q_1,Q_2)=Q_{1\blacktriangle}\overline{Q_{2\blacktriangle}}+Q_{1\blacktriangledown}\overline{Q_{2\blacktriangledown}}$ | the Hermitian form |
| $\omega$ | the holomorphic symplectic form |
| $\mathcal{N}=\{B(Q,Q)=0\}$ | the isotropic cone |
| $L_\pm=\{Q_{\blacktriangle}=\pm iQ_{\blacktriangledown}\}$ | the two isotropic lines |
| $[i:1],[-i:1]$ | the two isotropic directions in $\mathbb{CP}^1$ |
| $C_\pm=\mathcal{N}\cap S^3\cap L_\pm$ | the two Hopf fibres of the cone |
| $x^2-y^2=0$ | the split-complex null quadric |
| $u^2=0$ | the dual-number null quadric |

## Further Reading

- [Complex Two-Space](the-complex-two-space.html), for the space and the Hermitian form.
- [The Three Canonical Forms on $\mathbb{C}^2$](the-three-canonical-forms-on-the-complex-two-space.html), for $H$, $B$ and $\omega$ and their signatures.
- [The Subspaces of $\mathbb{C}^2$](the-subspaces-of-the-complex-two-space.html), for the complex lines, the Lagrangian lines and the isotropic subspaces.
- [The Flat Kähler Structure of $\mathbb{C}^2$](the-flat-kahler-structure-of-the-complex-two-space.html), the previous article, for $g$, $\omega$ and the relation among the forms.
- [The Classical Groups of $\mathbb{C}^2$](the-classical-groups-of-the-complex-two-space.html), the next article, for $O(2,\mathbb{C})$ and the stabilizer of the cone.
- [The Unit Sphere and the Hopf Fibration](the-unit-sphere-and-the-hopf-fibration.html), for the Hopf fibration and the linking number.
- [Split-Complex Algebra](split-complex-algebra.html), for the null quadric $x^2-y^2=0$.
- [Dual-Numbers Algebra](dual-numbers-algebra.html), for the degenerate null quadric $u^2=0$.
- [The Dual-Numbers Null Quadric and Projective Geometry](dual-numbers-null-quadric-and-projective-geometry.html), for the projective picture in the dual case.
- [Conventions in Mathematics](conventions-in-mathematics.html), for the glyphs and the typographic conventions of the corpus.
