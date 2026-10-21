# __Reduced Biquaternions and Hyperbolic Geometry__

## Introduction

The reduced biquaternion algebra is the commutative algebra $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\oplus\mathbb{C}$ of basis $1,i,j,ij$, with $i^{2}=-1$, $j^{2}=+1$ and $ji=ij$, element $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ and idempotent coordinates $(Q_{+},Q_{-})=(Q_{\blacktriangle}+Q_{\blacktriangledown},Q_{\blacktriangle}-Q_{\blacktriangledown})$. Its general plain sesquilinear form

$$
\langle \breve Q_{1},\breve Q_{2}\rangle_{\mathrm{H}}=\mathrm{Sc}(\breve Q_{1}\breve Q_{2}^{*})=Q_{1\blacktriangle}\bar Q_{2\blacktriangle}-Q_{1\blacktriangledown}\bar Q_{2\blacktriangledown},
$$

whose quadratic form is $\langle \breve Q\rangle_{*}=|Q_{\blacktriangle}|^{2}-|Q_{\blacktriangledown}|^{2}=q_{\blacktriangle}^{2}+q'^{2}_{\blacktriangle}-q_{\blacktriangledown}^{2}-q'^{2}_{\blacktriangledown}$, is real of signature $(2,2)$; it is the indefinite form of the algebra, and the article reads the hyperbolic geometry it carries.

The result is a degeneracy that is exact and worth stating plainly: the indefinite form carries a hyperbolic geometry, but the largest multiplication-invariant object that realises it is one-dimensional. The plane $\mathbb{R}\{1,j\}$ spanned by the unit and the hyperbolic unit is a subalgebra isomorphic to the split-complex numbers, the form restricts to it with signature $(1,1)$, and the level set $\{|Q_{\blacktriangle}|^{2}-|Q_{\blacktriangledown}|^{2}=-1\}$ inside that plane is a hyperbola, the hyperbolic line. The norm-one units of the subalgebra act on it as the boosts, and the natural sign and the flat (the negative of the star) are the two reflections, so that the algebra reaches the full isometry group $O(1,1)$. Larger subspaces of signature $(2,1)$, which would carry a hyperbolic plane, exist and are determined by the form, but the algebra's multiplication does not preserve any of them: the only multiplications that preserve such a subspace are the central real scalars $\pm1$, so no hyperbolic-plane isometry is realised by the algebra itself.

The article owns the signature pattern of the indefinite form, the split-complex subalgebra and its hyperbolic line, the hyperboloid model with its metric and geodesics, the boundary and the conformal picture, the classification of the isometries the algebra supplies, and the negative statement about the signature-$(2,1)$ subspaces. The form and its Gram matrix are *The Four Products, Their Forms and Their Algebraic Norms*; the idempotent coordinates are *Reduced Biquaternion Space*; the null cone and its projective geometry are *Zero Divisors of the Algebra of the Reduced Biquaternions* and *The Null Quadric and Its Projective Geometry*; the multiplicative action of the units and the isometry groups of the four forms are *Reduced Biquaternion Rotations and Lorentz Transformations*; the remarkable subspaces and the involutions are *Introduction to the Remarkable Subspaces* and *The Two Involutions and the Group of Involutions*. The split-complex companion, which is the same algebra over $\mathbb{R}$, is *Hyperbolic Geometry* and *Hyperbolic Rotations*; the split-biquaternion companion, where the hyperbolic three-space is carried by the anti-Hermitian subspace, is *Split-Biquaternions and Hyperbolic Geometry*.

**Conventions.** The four real coordinates of $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ are $Q_{\blacktriangle}=q_{\blacktriangle}+iq'_{\blacktriangle}$ and $Q_{\blacktriangledown}=q_{\blacktriangledown}+iq'_{\blacktriangledown}$; the form $\langle \breve Q\rangle_{*}=q_{\blacktriangle}^{2}+q'^{2}_{\blacktriangle}-q_{\blacktriangledown}^{2}-q'^{2}_{\blacktriangledown}$ is the quadratic form of $\langle\cdot,\cdot\rangle_{\mathrm{H}}$; a **hyperbolic line** is a one-dimensional hyperbolic space, that is one sheet of a hyperbola, and a **hyperbolic plane** is a two-dimensional hyperbolic space.

## The Indefinite Form and the Subspaces it Defines

**Proposition (the signature pattern).** On the real four-space the form $\langle\cdot,\cdot\rangle_{*}$ has signature $(2,2)$; on the real plane $\mathbb{R}\{1,j\}$ it has signature $(1,1)$; on the real plane $\mathbb{R}\{1,i\}$ it has signature $(2,0)$; on the real plane $\mathbb{R}\{j,ij\}$ it has signature $(0,2)$; and on each of the two real three-spaces $\mathbb{R}\{1,i,j\}$ and $\mathbb{R}\{1,i,ij\}$ it has signature $(2,1)$.

**Proof.** The values on the basis are $\langle 1\rangle_{*}=H(i)=1$, $H(j)=\langle ij\rangle_{*}=-1$, and distinct basis vectors are orthogonal for the bilinear form; the signature of a real subspace is read from the diagonal form restricted to it.

**Corollary (which subspace could carry which geometry).** A hyperbolic line lives in a subspace of signature $(1,1)$ and a hyperbolic plane in a subspace of signature $(2,1)$; a definite subspace of signature $(2,0)$ or $(0,2)$ carries no hyperbolic geometry.

**Remark (the two kinds of distinguished subspace).** The involution bar has its anti-invariant plane $\{\breve Q:\bar{\breve Q}=-\breve Q\}=\mathbb{R}\{i,ij\}$, of signature $(1,1)$, and the star has its anti-invariant plane $\{\breve Q:\breve Q^{*}=-\breve Q\}=\mathbb{R}\{i,j\}$, also of signature $(1,1)$; both are hyperbolic lines, and each is preserved by the three involutions of the Klein four-group. The planes $\mathbb{R}\{1,j\}$ and $\mathbb{R}\{i,ij\}$ are the two split-complex subalgebras of the algebra, and they are the multiplication-invariant ones.

## The Split-Complex Subalgebra and the Hyperbolic Line

**Proposition (the subalgebra).** The real span $\mathbb{D}=\mathbb{R}\{1,j\}$ is a subalgebra of $\mathbb{B}_{\mathrm{r}}$ isomorphic to the split-complex numbers, and so is its translate $i\mathbb{D}=\mathbb{R}\{i,ij\}$; the multiplication preserves each of them.

**Proof.** $j^{2}=1$, so $\mathbb{R}\{1,j\}$ is closed under the multiplication, and the multiplication table is that of $\mathbb{R}[j]/(j^{2}-1)$; multiplying by $i$ is an algebra isomorphism onto $\mathbb{R}\{i,ij\}$ with $(ij)^{2}=i^{2}j^{2}=-1$.

**Theorem (the hyperbolic line).** In the split-complex subalgebra the level set of the negative norm is the hyperbola

$$
\{\breve Q\in\mathbb{D}:\langle \breve Q\rangle_{*}=-1\}=\{q_{\blacktriangle}+jq_{\blacktriangledown}:q_{\blacktriangle}^{2}-q_{\blacktriangledown}^{2}=-1\},
$$

with its two branches $q_{\blacktriangledown}\geq1$ and $q_{\blacktriangledown}\leq-1$; each branch is a hyperbolic line under the metric whose distance is

$$
\cosh d(P,Q)=-\langle P,Q\rangle_{\mathrm{H}},\qquad \langle P,Q\rangle_{\mathrm{H}}=a_{P}a_{Q}-b_{P}b_{Q},
$$

and its isometry group is $O(1,1)$, of four components.

**Proof.** The bilinear form restricted to $\mathbb{D}$ is $\operatorname{diag}(1,-1)$; the level set is a hyperbola of two branches, and the standard hyperboloid model of the hyperbolic line carries the metric $\cosh d=-(\cdot,\cdot)$, because the form is negative of signature $(1,1)$ on the sheet and the conditions of the model hold; the isometry group of a form of signature $(1,1)$ in two variables has $2^{2}=4$ components, distinguished by the signs of the two isotropic coordinates.

**Proposition (the boosts are the translations).** For a real parameter $\phi$ the element $\exp(j\phi)=\cosh\phi+j\sinh\phi$ is a unit of norm one, and its multiplication acts on the coordinates $(q_{\blacktriangle},q_{\blacktriangledown})$ of $\mathbb{D}$ by

$$
(q_{\blacktriangle},q_{\blacktriangledown})\longmapsto(q_{\blacktriangle}\cosh\phi+q_{\blacktriangledown}\sinh\phi,\;q_{\blacktriangle}\sinh\phi+q_{\blacktriangledown}\cosh\phi),
$$

which is the translation by $\phi$ along the hyperbolic line; the elements $\exp(j\phi)$ form a one-parameter subgroup isomorphic to $\mathbb{R}$, the identity component of $O(1,1)$.

**Proof.** $\exp(j\phi)$ has $Q_{+}=\exp(\phi)$ and $Q_{-}=\exp(-\phi)$, so $N=Q_{+}Q_{-}=1$; the multiplication in $\mathbb{D}$ gives the displayed matrix, which is the standard boost; the map $\phi\mapsto \exp(j\phi)$ is an injective continuous homomorphism $\mathbb{R}\to\mathbb{B}_{\mathrm{r}}^{\times}$ because $\exp(j\phi)\exp(j\psi)=\exp(j(\phi+\psi))$, and the connected component of the identity in $O(1,1)$ is one-dimensional.

**Proposition (the reflections).** On the plane $\mathbb{D}=\mathbb{R}\{1,j\}$, whose coefficients are real, the natural sign restricts to the reflection

$$
{}^{\natural}:q_{\blacktriangle}+jq_{\blacktriangledown}\longmapsto q_{\blacktriangle}-jq_{\blacktriangledown},
$$

while the coefficient conjugation restricts to the identity; the second reflection of the hyperbolic line, $q_{\blacktriangle}+jq_{\blacktriangledown}\mapsto-q_{\blacktriangle}+jq_{\blacktriangledown}$, is the negative of the star, the flat, which is a linear isometry of the form but not an algebra automorphism. The boosts together with these two reflections generate all of $O(1,1)$.

**Proof.** On $\mathbb{D}$ the two coefficients $q_{\blacktriangle}$ and $q_{\blacktriangledown}$ are real, so the bar fixes them and is the identity, while the natural sign negates the second slot and sends $q_{\blacktriangle}+jq_{\blacktriangledown}$ to $q_{\blacktriangle}-jq_{\blacktriangledown}$; the star sends $q_{\blacktriangle}+jq_{\blacktriangledown}$ to $q_{\blacktriangle}-jq_{\blacktriangledown}$ there as well, and its negative sends $q_{\blacktriangle}+jq_{\blacktriangledown}$ to $-q_{\blacktriangle}+jq_{\blacktriangledown}$, of determinant $-1$, which preserves the form because $-1$ times a linear isometry is a linear isometry; the identity component is the boosts, and adjoining the two reflections generates the four components of $O(1,1)$.

## The Hyperboloid Model, the Metric and the Geodesics

**Proposition (the geodesics).** The geodesics of the hyperbolic line are the intersections of the hyperboloid with the two-dimensional subspaces of $\mathbb{D}$ through the origin, that is the hyperbolae $\{q_{\blacktriangle}^{2}-q_{\blacktriangledown}^{2}=-1\}\cap\{q_{\blacktriangle}=sq_{\blacktriangledown}\}$ for $s$ with $s^{2}<1$, and the null asymptotic directions $q_{\blacktriangle}=\pm q_{\blacktriangledown}$ are the boundary points.

**Proof.** The geodesics of the hyperboloid model are the intersections with the totally geodesic submanifolds, which are the linear subspaces; in signature $(1,1)$ a linear subspace carries a geodesic exactly when it is timelike, that is when the restriction of the form to it has signature $(1,1)$, which for a line means $s^{2}<1$.

**Proposition (the distance formula in coordinates).** For two points $P$ and $Q$ of the sheet $b>0$ the distance is

$$
\cosh d(P,Q)=b_{P}b_{Q}-a_{P}a_{Q},
$$

and the sphere of radius $t$ about $P$ is the intersection of the hyperboloid with the affine line $\langle X,P\rangle_{\mathrm{H}}=-\cosh t$, which consists of two points.

**Proof.** The formula is the distance formula of the hyperboloid model, and the level sets of the distance are the intersections with the affine hyperplanes orthogonal to $P$: the level set $\{X:\langle X,P\rangle_{\mathrm{H}}=-\cosh t\}$ is the intersection of the non-degenerate bilinear form level with the hyperboloid, which in two dimensions is a pair of points.

## The Boundary, the Conformal Picture and the Doubly Ruled Quadric

**Proposition (the boundary of the line).** The null set of $\langle\cdot\rangle_{*}$ inside $\mathbb{D}$ is the pair of lines $q_{\blacktriangle}=\pm q_{\blacktriangledown}$, the two isotropic lines; its projectivisation is the two-point boundary of the hyperbolic line, $\partial\mathbb{H}^{1}=\mathbb{P}^{1}_{\mathbb{R}}(\mathbb{D})$, and the two points are the directions $q_{\blacktriangle}=q_{\blacktriangledown}$ and $q_{\blacktriangle}=-q_{\blacktriangledown}$.

**Proof.** $q_{\blacktriangle}^{2}-q_{\blacktriangledown}^{2}=0$ gives $q_{\blacktriangle}=\pm q_{\blacktriangledown}$; each is a real line of the algebra, hence a point in the projective space; those are the two points at infinity of the two branches.

**Proposition (the boundary of the algebra).** The null set of $\langle\cdot\rangle_{*}$ in the whole algebra is the cone $\{|Q_{\blacktriangle}|=|Q_{\blacktriangledown}|\}$ of real dimension three, whose projectivisation is the smooth quadric of signature $(2,2)$, doubly ruled by the two families of totally isotropic planes $\{Q_{\blacktriangledown}=\exp(i\phi)Q_{\blacktriangle}\}$ and $\{Q_{\blacktriangledown}=\exp(i\phi)\bar Q_{\blacktriangle}\}$.

**Proof.** This is the theorem on the rulings of *The Null Quadric and Its Projective Geometry*; the cone is the union of the lines of the quadric.

**Remark (the conformal boundary).** The boundary of the hyperbolic line is the two-point set, that of the hyperbolic plane would be a circle; the boundary of the indefinite form's cone in the four-space is the doubly ruled quadric, whose two rulings are the two families of isotropic planes. The conformal structure at infinity is the projective structure of the null quadric, and the algebra's involutions act on it as the reflections of the two rulings.

## The Isometries and Their Classification

**Theorem (the multiplicative isometries).** A unit $P$ acts by multiplication as an isometry of the indefinite form $\langle\cdot,\cdot\rangle_{*}$ exactly when $p\bar q=1$ in the idempotent coordinates; the group of such units is the split unitary group $\{p\bar q=1\}\cong\mathbb{C}^{\times}$ of *The Unitary Group of the Reduced Biquaternion Algebra*, the versors $\{N=1\}$ of *Reduced Biquaternion Versors and the Orthogonal Group* preserve the bilinear companion of the form, and the involutions $\bar{\cdot}$, ${}^{\natural}$, ${}^{*}$ supply the reflections.

**Proof.** $\langle P \breve Q\rangle_{*}=\mathrm{Re}\bigl(p\bar q\,Q_{+}\bar Q_{-}\bigr)$ and $\langle \breve Q\rangle_{*}=\mathrm{Re}\bigl(Q_{+}\bar Q_{-}\bigr)$, so the multiplicative preservation of $\langle\cdot\rangle_{*}$ for all $\breve Q$ is the condition $p\bar q=1$; the versors preserve the bilinear form $\langle\cdot,\cdot\rangle_{\natural}$ by its scaling law, and the involutions are isometries or conjugate-isometries by *The Two Involutions and the Group of Involutions*.

**Proposition (the classification).** An element of the split unitary group, written in the idempotent coordinates as $(p,q)=(r\exp(i\theta),r^{-1}\exp(i\theta))$ with $r>0$ real, is the product of the two commuting factors $(r,r^{-1})$ and $(\exp(i\theta),\exp(i\theta))$: the first, real and positive, preserves each of the split planes $\mathbb{R}\{1,j\}$ and $\mathbb{R}\{i,ij\}$ and acts on it as the boost of parameter $\log r$, and the second, of unit modulus, preserves each of the definite planes $\mathbb{R}\{1,i\}$ and $\mathbb{R}\{j,ij\}$ and acts on it as the rotation of angle $\theta$. The elements with $r=1$ are the elliptic ones, those with $\theta=0$ the hyperbolic ones; there is no parabolic class, because a form of signature $(1,1)$ in two variables has no unipotent isometry.

**Proof.** The condition $p\bar q=1$ is solved by the polar pair $(\exp(i\theta),r^{-1}\exp(i\theta))$, and the multiplication by such an element acts diagonally in the idempotent coordinates, hence by the displayed matrices on the invariant planes; the classification of an isometry of an indefinite form is by the vanishing of the two invariants, the modulus and the argument, and in the plane $\mathbb{R}\{1,j\}$ of signature $(1,1)$ the identity component of $O(1,1)$ is one-dimensional and consists of the boosts.

**Remark (what the algebra does not reach).** The hyperbolic line's isometry group $O(1,1)$ is reached by the subalgebra $\mathbb{D}$ itself, but the hyperbolic plane's isometry group $O(2,1)$ is not reached by any subspace: the multiplication by an element preserves a three-space of signature $(2,1)$ only when the element is $\pm1$, because preservation would force the second idempotent-free coefficient of the multiplier to vanish and the first to be a real scalar, which then acts as a similitude and is an isometry only for $\pm1$.

## The Signature-$(2,1)$ Subspaces and Why No Hyperbolic Plane Is Carried

**Proposition (only the central scalars act).** Let $W$ be the real three-space $\mathbb{R}\{1,i,j\}$. If a unit $P$ satisfies $PW\subset W$ then $P$ is a nonzero real scalar, and if in addition $P$ preserves the form $\langle\cdot,\cdot\rangle_{*}$ then $P=\pm1$; consequently the multiplication by the units realises no nontrivial isometry of the hyperbolic plane that $W$ carries.

**Proof.** Write $P=P_{0}+P_{1}j$ with $P_{0},P_{1}\in\mathbb{C}$ and let $\breve Q=q_{\blacktriangle}+iq'_{\blacktriangle}+jq_{\blacktriangledown}$ run over $W$. The product is $P \breve Q=(P_{0}q_{\blacktriangle}+P_{0}iq'_{\blacktriangle}+P_{1}q_{\blacktriangledown})+(P_{0}q_{\blacktriangledown}+P_{1}q_{\blacktriangle})j+P_{1}q'_{\blacktriangle}\,ij$, so the $ij$-coefficient $P_{1}q'_{\blacktriangle}$ must vanish for every real $q'_{\blacktriangle}$, which forces $P_{1}=0$; then $P \breve Q=P_{0}q_{\blacktriangle}+P_{0}iq'_{\blacktriangle}+P_{0}q_{\blacktriangledown}\,j$, and its $j$-coefficient $P_{0}q_{\blacktriangledown}$ must be real for every real $q_{\blacktriangledown}$, which forces $P_{0}$ real. Hence $P=P_{0}$ is a nonzero real scalar, and the preservation of the form among the real scalars leaves $P_{0}=\pm1$.

**Corollary (the hyperbolic plane is carried by the form and not by the algebra).** The level set $\{H=-1\}\cap\mathbb{R}\{1,i,j\}$ is a two-sheeted hyperboloid, each sheet a hyperbolic plane of isometry group $O(2,1)$; it is an object determined by the form of the algebra, but the algebra's multiplication does not act on it, and only its involutions give the reflections.

**Remark (why the realised hyperbolic geometry is one-dimensional).** Every multiplication preserves each of the two idempotent lines and acts on them independently, by a complex scalar on each; the indefinite form in the idempotent coordinates is $\langle\cdot,\cdot\rangle_{*}=\mathrm{Re}(Q_{+}\bar Q_{-})$, so a multiplication changes the two arguments and the two moduli, and the largest multiplication-invariant real subspace on which the form is non-degenerate and indefinite is the split-complex plane, of signature $(1,1)$, which carries the hyperbolic line. The three-spaces of signature $(2,1)$ are not subalgebras: $\mathbb{R}\{1,i,j\}$ fails to be closed under the multiplication because $i\cdot j=ij$ lies outside it, and the three-dimensional subalgebras that do exist, such as $\mathbb{R}\oplus\mathbb{C}\Pi_-$, have a radical for the form, so they carry no hyperbolic geometry.

## Comparison with the Sibling Cases

**Remark (split-complex, split-biquaternion, biquaternion).** The split-complex numbers are the subalgebra $\mathbb{D}$ itself, so the hyperbolic line of this article is the classical hyperbolic line of *Hyperbolic Geometry*. In the split-biquaternion algebra the anti-Hermitian subspace is four-real-dimensional of signature $(1,3)$, and its level set of the Hermitian norm is a hyperboloid of three sheets, the hyperbolic three-space of *Split-Biquaternions and Hyperbolic Geometry*, with isometry group the restricted Lorentz group. In the biquaternion algebra the same construction gives hyperbolic three-space through the Hermitian matrices and $SL_{2}(\mathbb{C})$. The reduced biquaternion algebra is the case in which the Hermitian form has signature $(2,2)$, the anti-invariant subspaces have signature $(1,1)$, and the hyperbolic geometry is therefore the hyperbolic line and not the hyperbolic three-space: the dimension drops by two.

## Summary

The indefinite form of the reduced biquaternion algebra, $\langle\cdot,\cdot\rangle_{*}=|Q_{\blacktriangle}|^{2}-|Q_{\blacktriangledown}|^{2}$, has signature $(2,2)$ on the algebra, $(1,1)$ on the two split-complex subalgebras $\mathbb{R}\{1,j\}$ and $\mathbb{R}\{i,ij\}$, $(2,0)$ and $(0,2)$ on the definite planes $\mathbb{R}\{1,i\}$ and $\mathbb{R}\{j,ij\}$, and $(2,1)$ on the three-spaces $\mathbb{R}\{1,i,j\}$ and $\mathbb{R}\{1,i,ij\}$. The hyperbolic geometry that the form carries and the algebra realises is one-dimensional: on the split-complex plane the level set $\langle\cdot,\cdot\rangle_{*}=-1$ is a hyperbola of two branches, the hyperboloid model of the hyperbolic line, with metric $\cosh d=-\langle P,Q\rangle_{\mathrm{H}}$, geodesics the intersections with the timelike lines through the origin, boundary the two isotropic directions $q_{\blacktriangle}=\pm q_{\blacktriangledown}$, and isometry group $O(1,1)$, whose identity component is realised by the boosts $\exp(j\phi)$ and whose reflections are the natural sign and the coefficient conjugation. In the whole algebra the null set is the three-dimensional cone whose projectivisation is the smooth doubly ruled quadric, and the split unitary group acts in the idempotent coordinates by a boost on the split planes and a rotation on the definite planes, with the elliptic and hyperbolic classes distinguished by the rotation angle and the modulus and no parabolic class. The three-spaces of signature $(2,1)$ carry hyperbolic planes as objects of the form, but no nontrivial multiplication of the algebra preserves one of them: the only such multiplications are $\pm1$. The comparison with the split-complex, split-biquaternion and biquaternion algebras places the article as the case of the hyperbolic line, the dimension dropping by two from the hyperbolic three-space of the quaternionic companions.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle \breve Q\rangle_{*}=\lvert Q_{\blacktriangle}\rvert^{2}-\lvert Q_{\blacktriangledown}\rvert^{2}$ | the indefinite form, of signature $(2,2)$ on the algebra |
| $\langle \breve Q_{1},\breve Q_{2}\rangle_{\mathrm{H}}=\mathrm{Sc}(\breve Q_{1}\breve Q_{2}^{*})=Q_{1\blacktriangle}\bar Q_{2\blacktriangle}-Q_{1\blacktriangledown}\bar Q_{2\blacktriangledown}$ | its sesquilinear pairing |
| $\mathbb{D}=\mathbb{R}\{1,j\}$ | the split-complex subalgebra, $j^{2}=1$ |
| $i\mathbb{D}=\mathbb{R}\{i,ij\}$ | the second split-complex subalgebra |
| $\{H=-1\}$ in $\mathbb{D}$ | the hyperbola, the hyperbolic line |
| $\cosh d(P,Q)=-\langle P,Q\rangle_{\mathrm{H}}$ | the distance in the hyperboloid model |
| $\exp(j\phi)=\cosh\phi+j\sinh\phi$ | the boost, a translation of the hyperbolic line |
| $O(1,1)$ | the isometry group of the hyperbolic line, four components |
| $q_{\blacktriangle}=\pm q_{\blacktriangledown}$ | the two isotropic directions, the boundary of the line |
| $\mathbb{R}\{1,i,j\}$, signature $(2,1)$ | the three-space whose hyperbolic plane the algebra does not act on |

## Further Reading

- [Reduced Biquaternion Space](reduced-biquaternion-space.html), above this article in this category, for the basis, the relations and the idempotent coordinates.
- [The Four Products, Their Forms and Their Algebraic Norms](the-four-products-their-forms-and-their-algebraic-norms-of-the-reduced-biquaternions.html), above this article, for the indefinite form and its Gram matrix.
- [The Null Quadric and Its Projective Geometry](the-null-quadric-and-its-projective-geometry-for-the-reduced-biquaternions.html), above this article, for the doubly ruled quadric that is the boundary of the cone.
- [The Unitary Group of the Reduced Biquaternion Algebra](the-unitary-group-of-the-reduced-biquaternion-algebra.html), above this article, for the split unitary group $\{p\bar q=1\}$.
- [The Two Involutions and the Group of Involutions](the-two-involutions-and-the-group-of-involutions-of-the-reduced-biquaternions.html), above this article, for the reflections of the hyperbolic line.
- [Hyperbolic Geometry](hyperbolic-geometry.html), for the general theory of hyperbolic spaces, geodesics and boundaries, cited and not restated.
- [Split-Biquaternions and Hyperbolic Geometry](split-biquaternions-and-hyperbolic-geometry.html), for the companion in which the hyperbolic three-space is carried by the anti-Hermitian subspace.
