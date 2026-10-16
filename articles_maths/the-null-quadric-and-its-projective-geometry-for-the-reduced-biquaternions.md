# __The Null Quadric and Its Projective Geometry__

## Introduction

The reduced biquaternion algebra is

$$
\mathbb{B}_{\mathrm{r}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\oplus\mathbb{C},
$$

with basis $1,i,j,ij$, relation $j^{2}=+1$, idempotent coordinates $(q_1,q_2)=(A+B,A-B)$ and element $T=A+Bj$. Its four general products carry the four algebraic norms

$$
\langle T\rangle=A^{2}+B^{2},\qquad \langle T\rangle_{\natural}=A^{2}-B^{2},\qquad \langle T\rangle_{*}=|A|^{2}-|B|^{2},\qquad \langle T\rangle_{\natural*}=|A|^{2}+|B|^{2},
$$

the two bilinear ones complex-valued and the two sesquilinear ones real-valued. A form in four real variables has a null set, and the null set of a non-degenerate form has a projective geometry: its projectivisation is a quadric. This article owns that geometry for the reduced biquaternion algebra, for each of the four forms, and the comparison between them.

The single most important fact is that the reduced algebra is the direct sum $\mathbb{C}\Pi_{1}\oplus\mathbb{C}\Pi_{2}$ of two complex lines, so its multiplicative norm factors as $\langle T\rangle_{\natural}=(A-B)(A+B)=q_1q_2$, a product of two linear forms in the complex coordinates; the projective null quadric of the reduced norm is therefore degenerate, a pair of lines, and not a smooth quadric. The companion smooth quadric is the one carried by the indefinite Hermitian form $\langle\cdot,\cdot\rangle_{*}$, whose real signature is $(2,2)$ and whose projectivisation is a smooth ruled surface in real projective three-space. The definite form $\langle\cdot,\cdot\rangle_{\natural*}$ has no null points at all, and the plain bilinear form $\langle\cdot,\cdot\rangle$ degenerates exactly as $\langle\cdot,\cdot\rangle_{\natural}$ does.

The article owns the four null sets, the degenerate quadric of the reduced norm with its two components, the smooth quadric of $\langle\cdot\rangle_{*}$ with its two rulings, the Segre identification with $\mathbb{P}^{1}_{\mathbb{R}}\times\mathbb{P}^{1}_{\mathbb{R}}$, the polarity that the forms induce, and the automorphism group of the smooth quadric. The forms and their Gram matrices are *The Four Products, Their Forms and Their Algebraic Norms*; the idempotent coordinates and the two ideals are *Reduced Biquaternion Space* and *Ideals and Peirce Decomposition of the General Plain Algebra of the Reduced Biquaternions*; the zero divisors whose set is the null cone of $\langle\cdot\rangle_{\natural}$ are *Zero Divisors of the General Plain Algebra of the Reduced Biquaternions*; the metric reading of the forms on the space is *Topology and Metric for Each of the Operations*; the real subspaces that the null set meets are *Introduction to the Remarkable Subspaces*. The smooth null quadric of the biquaternion algebra, in complex projective three-space, is *The Null Quadric and Its Projective Geometry*.

**Conventions.** The algebra is read as the real four-dimensional space with coordinates $(a,a',b,b')$ where $A=a+ia'$ and $\langle\cdot\rangle=b+ib'$; the real projective space of its lines is $\mathbb{P}^{3}_{\mathbb{R}}$. The complex reading, with the algebra as a complex 2-dimensional space on the basis $1,j$, has projective space $\mathbb{P}^{1}_{\mathbb{C}}$. The two readings are different and are kept apart throughout.

## The Four Null Sets

**Proposition (the sign of the forms).** On the real coordinates $(a,a',b,b')$ the four norms are

$$
B=a^{2}-a'^{2}+b^{2}-b'^{2}+2i(aa'+bb'), \qquad N=a^{2}-a'^{2}-b^{2}+b'^{2}+2i(aa'-bb'),
$$

$$
H=a^{2}+a'^{2}-b^{2}-b'^{2}, \qquad K=a^{2}+a'^{2}+b^{2}+b'^{2}.
$$

Hence $\langle\cdot,\cdot\rangle_{*}$ is a real quadratic form of signature $(2,2)$, $\langle\cdot,\cdot\rangle_{\natural*}$ is positive definite of signature $(4,0)$, and $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{\natural}$ are complex-valued forms whose real and imaginary parts are each of signature $(2,2)$.

**Proof.** Substitute $A=a+ia'$ and $\langle\cdot,\cdot\rangle=b+ib'$ into the four norms and separate real and imaginary parts; the signatures are read from the diagonal matrices $\operatorname{diag}(1,1,-1,-1)$ and $\operatorname{diag}(1,1,1,1)$ and from the Gram matrices of *The Four Products, Their Forms and Their Algebraic Norms*.

**Proposition (the null sets).** The zero sets of the four norms are

$$
\{N=0\}=\{A=B\}\cup\{A=-B\}, \qquad \{B=0\}=\{A=iB\}\cup\{A=-iB\},
$$

$$
\{H=0\}=\{|A|^{2}=|B|^{2}\}, \qquad \{K=0\}=\{0\}.
$$

**Proof.** $A^{2}=B^{2}$ in the field $\mathbb{C}$ has the two solutions $A=\pm B$, and $A^{2}=-B^{2}$ the two solutions $A=\pm iB$; $\langle\cdot\rangle_{*}$ is the difference of the two non-negative quantities $|A|^{2}$ and $|B|^{2}$; and $\langle\cdot\rangle_{\natural*}$ is their sum, which vanishes only at the origin.

**Corollary (the two lines of the reduced norm).** Each of $\{A=B\}$ and $\{A=-B\}$ is a complex line through the origin of $\mathbb{C}^{2}$, hence a real two-plane in $\mathbb{B}_{\mathrm{r}}$, hence a projective line in $\mathbb{P}^{3}_{\mathbb{R}}$; the two lines meet only at the origin of $\mathbb{B}_{\mathrm{r}}$, so they are skew in $\mathbb{P}^{3}_{\mathbb{R}}$. They are the two minimal ideals

$$
\mathbb{C}\Pi_{1}=\{q_2=0\}=\{A=B\}, \qquad \mathbb{C}\Pi_{2}=\{q_1=0\}=\{A=-B\},
$$

the two summands of the direct product, and the null cone of the reduced norm is their union.

## The Degenerate Null Quadric of the Reduced Norm

**Proposition (the reduced norm is a product of two linear forms).** In the idempotent coordinates the reduced norm is $\langle T\rangle_{\natural}=q_1q_2$, and in the complex coordinates it is $\langle\cdot\rangle_{\natural}=A^{2}-B^{2}=(A-B)(A+B)$.

**Proof.** $\langle T\rangle_{\natural}=A^{2}-B^{2}=(A-B)(A+B)$ by the identity for a difference of squares in a commutative ring, and $q_1=A+B$, $q_2=A-B$.

**Theorem (the quadric degenerates).** The projective null set of the reduced norm is the union of the two projective lines $\{q_2=0\}$ and $\{q_1=0\}$ of $\mathbb{P}^{3}_{\mathbb{R}}$; it is a quadric of rank two, a pair of lines, and it is not a smooth quadric surface. Over the complex reading the same null set is the two points $[1:0]$ and $[0:1]$ of $\mathbb{P}^{1}_{\mathbb{C}}$.

**Proof.** A homogeneous quadratic form that is a product of two distinct linear forms has rank two, and its projective zero set is the union of the two hyperplanes defined by the factors, which in a projective space of dimension three are two planes; here each factor is complex-linear, so each zero set is a complex line in $\mathbb{C}^{2}$, of real dimension two, and its projectivisation is a line, not a plane. Reading the algebra as a complex 2-dimensional space instead, the two factors $q_1$ and $q_2$ are two linear forms on $\mathbb{C}^{2}$ and their zero sets are the two points of $\mathbb{P}^{1}_{\mathbb{C}}$.

**Remark (why the complex dimension decides the shape).** The factor $q_2=A-B$ is complex-linear, so its zero set is a complex subspace: of real dimension two in the real reading, of complex dimension one in the complex reading. The reduced algebra is four-real-dimensional but two-complex-dimensional, and this is the reason its norm's null quadric is a pair of lines rather than the four-dimensional cone of the biquaternion case.

## The Smooth Quadric of the Indefinite Hermitian Form

**Theorem (the quadric of $\langle\cdot,\cdot\rangle_{*}$ is smooth).** The real form $\langle\cdot,\cdot\rangle_{*}=a^{2}+a'^{2}-b^{2}-b'^{2}$ is non-degenerate of signature $(2,2)$, its null cone is a real three-dimensional cone, and its projectivisation is a smooth quadric surface in $\mathbb{P}^{3}_{\mathbb{R}}$.

**Proof.** The gradient of $\langle\cdot\rangle_{*}$ is $2(a,a',-b,-b')$, which vanishes only at the origin, so the cone is a smooth hypersurface and its projectivisation is a smooth quadric; the signature is read from the diagonal form $\operatorname{diag}(1,1,-1,-1)$.

**Theorem (the two rulings).** The quadric $\{H=0\}$ is doubly ruled. Its two families of lines are the projectivisations of the two families of totally isotropic two-planes

$$
\mathcal{F}_{1}(\phi)=\{(A,B):B=e^{i\phi}A\}, \qquad \mathcal{F}_{2}(\phi)=\{(A,B):B=e^{i\phi}\bar A\}, \qquad \phi\in\mathbb{R}/2\pi\mathbb{Z},
$$

and every point of the quadric lies on exactly one member of each family. Each family is parametrised by a circle, hence by a projective line, and the quadric is isomorphic to $\mathbb{P}^{1}_{\mathbb{R}}\times\mathbb{P}^{1}_{\mathbb{R}}$ through the Segre map that sends a pair of parameters to the intersection point of the two lines.

**Proof.** On a plane of $\mathcal{F}_{1}$, $|B|=|A|$ because $|e^{i\phi}|=1$, so $\langle\cdot\rangle_{*}=|A|^{2}-|B|^{2}=0$ identically, and the plane is totally isotropic; the same computation holds on $\mathcal{F}_{2}$ because $|\bar A|=|A|$. A point of the quadric satisfies $|A|=|B|$, hence $B/A$ and $B/\bar A$ are unit complex numbers whenever $A\neq0$, which determines the phase $\phi$ in each family uniquely; the two isotropic planes $\mathcal{F}_{1}(\phi_{1})$ and $\mathcal{F}_{2}(\phi_{2})$ meet in the complex line $\{B=e^{i\phi_{1}}A,\;B=e^{i\phi_{2}}\bar A\}$, of real dimension two, whose projectivisation is the point carrying the pair $(\phi_{1},\phi_{2})$.

**Corollary (the two distinguished lines).** The two lines of the degenerate quadric of the reduced norm lie on the smooth quadric: $\{A=B\}=\mathcal{F}_{1}(0)$ and $\{A=-B\}=\mathcal{F}_{1}(\pi)$. Both belong to the same ruling, and they are the two members of that ruling fixed by the real structure of the algebra.

**Proof.** Both sets are of the form $\langle\cdot,\cdot\rangle=e^{i\phi}A$ with $\phi=0$ and $\phi=\pi$; on each, $\langle\cdot,\cdot\rangle_{\natural}=q_1q_2$ and $\langle\cdot,\cdot\rangle_{*}$ both vanish, so the line lies on both quadrics.

## Polarity and Tangency

**Proposition (the polarity of $\langle\cdot,\cdot\rangle_{*}$).** The form $\langle\cdot,\cdot\rangle_{*}$ defines a polarity of $\mathbb{P}^{3}_{\mathbb{R}}$ sending a point to a plane, and a point of the quadric is sent to its tangent plane; for a point written $(A,B)$ the polar plane of the point $(A_{0},B_{0})$ is the set of classes of vectors $(A,B)$ with

$$
\operatorname{Re}\bigl(A\bar A_{0}\bigr)-\operatorname{Re}\bigl(B\bar B_{0}\bigr)=0 .
$$

**Proof.** The polarity of a non-degenerate quadratic form is the linear map on projective space induced by the bilinear form; the polar plane of a point is the orthogonal complement of its representative under the bilinear form, and for a point of the quadric the orthogonal complement is the tangent space, because the derivative of $\langle\cdot,\cdot\rangle_{*}$ vanishes exactly along the tangent directions.

**Remark (the degenerate polarity of $\langle\cdot\rangle_{\natural}$).** The reduced norm is a product of two linear forms, so its polarity is degenerate: it has a one-dimensional radical and does not define a duality of the projective space. The radical is the intersection $\{q_1=0\}\cap\{q_2=0\}$, which is the origin, so the polarity vanishes on it; the tangent spaces at the points of the two lines are constant along each line, which is the projective reading of the rank defect.

## Automorphisms of the Quadric

**Theorem (the automorphism group of the smooth quadric).** The projective automorphisms of the quadric $\{H=0\}$ are the projectivisations of the isometries of $\langle\cdot\rangle_{*}$, and the group is $\mathrm{PO}(2,2)_{\mathbb{R}}$; it acts on the two rulings and is isomorphic to the group $(\mathrm{PGL}_{2}(\mathbb{R})\times\mathrm{PGL}_{2}(\mathbb{R}))\rtimes(\mathbb{Z}/2)$, each copy of $\mathrm{PGL}_{2}(\mathbb{R})$ acting on one ruling, the exchange of the two rulings being the extra involution.

**Proof.** A projective transformation preserves the quadric exactly when the underlying linear map preserves the form up to a scalar, which is the orthogonal group modulo its centre; the two rulings are the two factors of the Segre isomorphism, and every automorphism either preserves each ruling or exchanges them, since the ruling structure is invariant under the form.

**Remark (the interaction with the algebra).** The automorphisms of the quadric form a continuous group of real dimension six, and the automorphism group of the algebra computed in *Reduced Biquaternion Automorphisms and Derivations* is a finite dihedral group of order eight; the two groups are different objects. The algebra automorphisms act on the algebra and carry the forms to the forms, hence act on the quadric, but they are a very small subgroup of the projective automorphism group: the continuous transformations of the quadric are not algebra automorphisms.

## Summary

The reduced biquaternion algebra carries four algebraic norms. The definite one, $\langle\cdot\rangle_{\natural*}=|A|^{2}+|B|^{2}$, has no null points. The two bilinear ones, $\langle\cdot\rangle=A^{2}+B^{2}$ and the reduced norm $\langle\cdot\rangle_{\natural}=A^{2}-B^{2}=q_1q_2$, factor as products of two complex-linear forms, so their projective null sets are degenerate quadrics: a pair of skew lines in $\mathbb{P}^{3}_{\mathbb{R}}$, or a pair of points in the complex reading $\mathbb{P}^{1}_{\mathbb{C}}$. The two lines of the reduced norm are the two minimal ideals $\mathbb{C}\Pi_{2}$ and $\mathbb{C}\Pi_{1}$, the two summands of the direct product, which is the reason the norm degenerates. The indefinite Hermitian form $\langle\cdot,\cdot\rangle_{*}=|A|^{2}-|B|^{2}$, of real signature $(2,2)$, is the one form whose null quadric is smooth: it is a doubly ruled quadric surface in $\mathbb{P}^{3}_{\mathbb{R}}$, ruled by the two families of totally isotropic planes $\langle\cdot,\cdot\rangle=e^{i\phi}A$ and $\langle\cdot\rangle=e^{i\phi}\bar A$, isomorphic to $\mathbb{P}^{1}_{\mathbb{R}}\times\mathbb{P}^{1}_{\mathbb{R}}$ by the Segre map, and the two lines of the reduced norm are two members of one ruling. The form $\langle\cdot,\cdot\rangle_{*}$ induces a polarity whose polar plane at a point of the quadric is the tangent plane, while the polarity of the reduced norm is degenerate. The projective automorphisms of the smooth quadric form the group $\mathrm{PO}(2,2)_{\mathbb{R}}\cong(\mathrm{PGL}_{2}(\mathbb{R})\times\mathrm{PGL}_{2}(\mathbb{R}))\rtimes(\mathbb{Z}/2)$, which acts on the two rulings and is far larger than the finite group of automorphisms of the algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle\cdot\rangle=A^{2}+B^{2}$ | the norm of the general plain bilinear product |
| $\langle\cdot\rangle_{\natural}=A^{2}-B^{2}=q_1q_2$ | the reduced norm, the norm of the general quaternionic bilinear product |
| $\langle\cdot\rangle_{*}=\lvert A\rvert^{2}-\lvert B\rvert^{2}$ | the norm of the general plain sesquilinear product, indefinite of signature $(2,2)$ |
| $\langle\cdot\rangle_{\natural*}=\lvert A\rvert^{2}+\lvert B\rvert^{2}$ | the norm of the general quaternionic sesquilinear product, positive definite |
| $A=a+ia'$, $\langle\cdot\rangle=b+ib'$ | the two complex coordinates |
| $q_1=A+B$, $q_2=A-B$ | the idempotent coordinates, $\langle\cdot\rangle_{\natural}=q_1q_2$ |
| $\mathbb{P}^{3}_{\mathbb{R}}$ | the real projective space of the algebra read as a real four-space |
| $\mathbb{P}^{1}_{\mathbb{C}}$ | the complex projective space of the algebra read as a complex two-space |
| $\mathcal{F}_{1}(\phi)=\{B=e^{i\phi}A\}$ | the first ruling of totally isotropic planes |
| $\mathcal{F}_{2}(\phi)=\{B=e^{i\phi}\bar A\}$ | the second ruling of totally isotropic planes |
| $\mathbb{C}\Pi_{1}=\{A=B\}$, $\mathbb{C}\Pi_{2}=\{A=-B\}$ | the two minimal ideals, the two lines of the reduced norm |

## Further Reading

- *Reduced Biquaternion Space* (`articles_maths/reduced-biquaternion-space.md`), above this article in this category, for the idempotent coordinates and the isomorphism $\mathbb{B}_{\mathrm{r}}\cong\mathbb{C}\oplus\mathbb{C}$.
- *The Four Products, Their Forms and Their Algebraic Norms* (`articles_maths/the-four-products-their-forms-and-their-algebraic-norms-of-the-reduced-biquaternions.md`), above this article, for the four norms, their Gram matrices and their signatures.
- *Ideals and Peirce Decomposition of the General Plain Algebra of the Reduced Biquaternions* (`articles_maths/ideals-and-peirce-decomposition-of-the-general-plain-algebra-of-the-reduced-biquaternions.md`), below this article, for the two minimal ideals that are the lines of the degenerate quadric.
- *Zero Divisors of the General Plain Algebra of the Reduced Biquaternions* (`articles_maths/zero-divisors-of-the-general-plain-algebra-of-the-reduced-biquaternions.md`), below this article, for the null cone of the reduced norm as the set of zero divisors.
- *The Null Quadric and Its Projective Geometry* (`articles_maths/the-null-quadric-and-its-projective-geometry.md`), for the non-degenerate case of the biquaternion algebra, where the null quadric is smooth in complex projective three-space.
- *Split-Biquaternion Null Quadric and Projective Geometry* (`articles_maths/split-biquaternion-null-quadric-and-projective-geometry.md`), for the split-complex companion.
