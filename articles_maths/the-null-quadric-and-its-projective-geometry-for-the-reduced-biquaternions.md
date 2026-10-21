# __The Null Quadric and Its Projective Geometry__

## Introduction

The reduced biquaternion algebra is

$$
\mathbb{B}_{\mathrm{r}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\oplus\mathbb{C},
$$

with basis $1,i,j,ij$, relation $j^{2}=+1$, idempotent coordinates $(Q_{++},Q_{--})=(Q_++Q_-,Q_+-Q_-)$ and element $\breve Q=Q_++jQ_-$. Its four general products carry the four algebraic norms

$$
\langle \breve Q\rangle=Q_+^{2}+Q_-^{2},\qquad \langle \breve Q\rangle_{\natural}=Q_+^{2}-Q_-^{2},\qquad \langle \breve Q\rangle_{*}=|Q_+|^{2}-|Q_-|^{2},\qquad \langle \breve Q\rangle_{\natural*}=|Q_+|^{2}+|Q_-|^{2},
$$

the two bilinear ones complex-valued and the two sesquilinear ones real-valued. A form in four real variables has a null set, and the null set of a non-degenerate form has a projective geometry: its projectivisation is a quadric. This article owns that geometry for the reduced biquaternion algebra, for each of the four forms, and the comparison between them.

The single most important fact is that the reduced algebra is the direct sum $\mathbb{C}\Pi_+\oplus\mathbb{C}\Pi_-$ of two complex lines, so its multiplicative norm factors as $\langle \breve Q\rangle_{\natural}=(Q_+-Q_-)(Q_++Q_-)=Q_{++}Q_{--}$, a product of two linear forms in the complex coordinates; the projective null quadric of the reduced norm is therefore degenerate, a pair of lines, and not a smooth quadric. The companion smooth quadric is the one carried by the indefinite Hermitian form $\langle\cdot,\cdot\rangle_{*}$, whose real signature is $(2,2)$ and whose projectivisation is a smooth ruled surface in real projective three-space. The definite form $\langle\cdot,\cdot\rangle_{\natural*}$ has no null points at all, and the plain bilinear form $\langle\cdot,\cdot\rangle$ degenerates exactly as $\langle\cdot,\cdot\rangle_{\natural}$ does.

The article owns the four null sets, the degenerate quadric of the reduced norm with its two components, the smooth quadric of $\langle\cdot\rangle_{*}$ with its two rulings, the Segre identification with $\mathbb{P}^{1}_{\mathbb{R}}\times\mathbb{P}^{1}_{\mathbb{R}}$, the polarity that the forms induce, and the automorphism group of the smooth quadric. The forms and their Gram matrices are *The Four Products, Their Forms and Their Algebraic Norms*; the idempotent coordinates and the two ideals are *Reduced Biquaternion Space* and *Ideals and Peirce Decomposition of the Algebra of the Reduced Biquaternions*; the zero divisors whose set is the null cone of $\langle\cdot\rangle_{\natural}$ are *Zero Divisors of the Algebra of the Reduced Biquaternions*; the metric reading of the forms on the space is *Topology and Metric for Each of the Operations*; the real subspaces that the null set meets are *Introduction to the Remarkable Subspaces*. The smooth null quadric of the biquaternion algebra, in complex projective three-space, is *The Null Quadric and Its Projective Geometry*.

**Conventions.** The algebra is read as the real four-dimensional space with coordinates $(q_+,q'_+,q_-,q'_-)$ where $Q_+=q_++iq'_+$ and $Q_-=q_-+iq'_-$; the real projective space of its lines is $\mathbb{P}^{3}_{\mathbb{R}}$. The complex reading, with the algebra as a complex 2-dimensional space on the basis $1,j$, has projective space $\mathbb{P}^{1}_{\mathbb{C}}$. The two readings are different and are kept apart throughout.

## The Four Null Sets

**Proposition (the sign of the forms).** On the real coordinates $(q_+,q'_+,q_-,q'_-)$ the four norms are

$$
B=q_+^{2}-q'^{2}_{+}+q_-^{2}-q'^{2}_{-}+2i(q_+q'_++q_-q'_-), \qquad N=q_+^{2}-q'^{2}_{+}-q_-^{2}+q'^{2}_{-}+2i(q_+q'_+-q_-q'_-),
$$

$$
H=q_+^{2}+q'^{2}_{+}-q_-^{2}-q'^{2}_{-}, \qquad K=q_+^{2}+q'^{2}_{+}+q_-^{2}+q'^{2}_{-}.
$$

Hence $\langle\cdot,\cdot\rangle_{*}$ is a real quadratic form of signature $(2,2)$, $\langle\cdot,\cdot\rangle_{\natural*}$ is positive definite of signature $(4,0)$, and $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{\natural}$ are complex-valued forms whose real and imaginary parts are each of signature $(2,2)$.

**Proof.** Substitute $Q_+=q_++iq'_+$ and $Q_-=q_-+iq'_-$ into the four norms and separate real and imaginary parts; the signatures are read from the diagonal matrices $\operatorname{diag}(1,1,-1,-1)$ and $\operatorname{diag}(1,1,1,1)$ and from the Gram matrices of *The Four Products, Their Forms and Their Algebraic Norms*.

**Proposition (the null sets).** The zero sets of the four norms are

$$
\{N=0\}=\{Q_+=Q_-\}\cup\{Q_+=-Q_-\}, \qquad \{B=0\}=\{Q_+=iQ_-\}\cup\{Q_+=-iQ_-\},
$$

$$
\{H=0\}=\{|Q_+|^{2}=|Q_-|^{2}\}, \qquad \{K=0\}=\{0\}.
$$

**Proof.** $Q_+^{2}=Q_-^{2}$ in the field $\mathbb{C}$ has the two solutions $Q_+=\pm Q_-$, and $Q_+^{2}=-Q_-^{2}$ the two solutions $Q_+=\pm iQ_-$; $\langle\cdot\rangle_{*}$ is the difference of the two non-negative quantities $|Q_+|^{2}$ and $|Q_-|^{2}$; and $\langle\cdot\rangle_{\natural*}$ is their sum, which vanishes only at the origin.

**Corollary (the two lines of the reduced norm).** Each of $\{Q_+=Q_-\}$ and $\{Q_+=-Q_-\}$ is a complex line through the origin of $\mathbb{C}^{2}$, hence a real two-plane in $\mathbb{B}_{\mathrm{r}}$, hence a projective line in $\mathbb{P}^{3}_{\mathbb{R}}$; the two lines meet only at the origin of $\mathbb{B}_{\mathrm{r}}$, so they are skew in $\mathbb{P}^{3}_{\mathbb{R}}$. They are the two minimal ideals

$$
\mathbb{C}\Pi_+=\{Q_{--}=0\}=\{Q_+=Q_-\}, \qquad \mathbb{C}\Pi_-=\{Q_{++}=0\}=\{Q_+=-Q_-\},
$$

the two summands of the direct product, and the null cone of the reduced norm is their union.

## The Degenerate Null Quadric of the Reduced Norm

**Proposition (the reduced norm is a product of two linear forms).** In the idempotent coordinates the reduced norm is $\langle \breve Q\rangle_{\natural}=Q_{++}Q_{--}$, and in the complex coordinates it is $\langle\cdot\rangle_{\natural}=Q_+^{2}-Q_-^{2}=(Q_+-Q_-)(Q_++Q_-)$.

**Proof.** $\langle \breve Q\rangle_{\natural}=Q_+^{2}-Q_-^{2}=(Q_+-Q_-)(Q_++Q_-)$ by the identity for a difference of squares in a commutative ring, and $Q_{++}=Q_++Q_-$, $Q_{--}=Q_+-Q_-$.

**Theorem (the quadric degenerates).** The projective null set of the reduced norm is the union of the two projective lines $\{Q_{--}=0\}$ and $\{Q_{++}=0\}$ of $\mathbb{P}^{3}_{\mathbb{R}}$; it is a quadric of rank two, a pair of lines, and it is not a smooth quadric surface. Over the complex reading the same null set is the two points $[1:0]$ and $[0:1]$ of $\mathbb{P}^{1}_{\mathbb{C}}$.

**Proof.** A homogeneous quadratic form that is a product of two distinct linear forms has rank two, and its projective zero set is the union of the two hyperplanes defined by the factors, which in a projective space of dimension three are two planes; here each factor is complex-linear, so each zero set is a complex line in $\mathbb{C}^{2}$, of real dimension two, and its projectivisation is a line, not a plane. Reading the algebra as a complex 2-dimensional space instead, the two factors $Q_{++}$ and $Q_{--}$ are two linear forms on $\mathbb{C}^{2}$ and their zero sets are the two points of $\mathbb{P}^{1}_{\mathbb{C}}$.

**Remark (why the complex dimension decides the shape).** The factor $Q_{--}=Q_+-Q_-$ is complex-linear, so its zero set is a complex subspace: of real dimension two in the real reading, of complex dimension one in the complex reading. The reduced algebra is four-real-dimensional but two-complex-dimensional, and this is the reason its norm's null quadric is a pair of lines rather than the four-dimensional cone of the biquaternion case.

## The Smooth Quadric of the Indefinite Hermitian Form

**Theorem (the quadric of $\langle\cdot,\cdot\rangle_{*}$ is smooth).** The real form $\langle\cdot,\cdot\rangle_{*}=q_+^{2}+q'^{2}_{+}-q_-^{2}-q'^{2}_{-}$ is non-degenerate of signature $(2,2)$, its null cone is a real three-dimensional cone, and its projectivisation is a smooth quadric surface in $\mathbb{P}^{3}_{\mathbb{R}}$.

**Proof.** The gradient of $\langle\cdot\rangle_{*}$ is $2(q_+,q'_+,-q_-,-q'_-)$, which vanishes only at the origin, so the cone is a smooth hypersurface and its projectivisation is a smooth quadric; the signature is read from the diagonal form $\operatorname{diag}(1,1,-1,-1)$.

**Theorem (the two rulings).** The quadric $\{H=0\}$ is doubly ruled. Its two families of lines are the projectivisations of the two families of totally isotropic two-planes

$$
\mathcal{F}_{1}(\phi)=\{(Q_+,Q_-):Q_-=e^{i\phi}Q_+\}, \qquad \mathcal{F}_{2}(\phi)=\{(Q_+,Q_-):Q_-=e^{i\phi}\bar Q_+\}, \qquad \phi\in\mathbb{R}/2\pi\mathbb{Z},
$$

and every point of the quadric lies on exactly one member of each family. Each family is parametrised by a circle, hence by a projective line, and the quadric is isomorphic to $\mathbb{P}^{1}_{\mathbb{R}}\times\mathbb{P}^{1}_{\mathbb{R}}$ through the Segre map that sends a pair of parameters to the intersection point of the two lines.

**Proof.** On a plane of $\mathcal{F}_{1}$, $|Q_-|=|Q_+|$ because $|e^{i\phi}|=1$, so $\langle\cdot\rangle_{*}=|Q_+|^{2}-|Q_-|^{2}=0$ identically, and the plane is totally isotropic; the same computation holds on $\mathcal{F}_{2}$ because $|\bar Q_+|=|Q_+|$. A point of the quadric satisfies $|Q_+|=|Q_-|$, hence $Q_-/Q_+$ and $Q_-/\bar Q_+$ are unit complex numbers whenever $Q_+\neq0$, which determines the phase $\phi$ in each family uniquely; the two isotropic planes $\mathcal{F}_{1}(\phi_{1})$ and $\mathcal{F}_{2}(\phi_{2})$ meet in the complex line $\{Q_-=e^{i\phi_{1}}Q_+,\;Q_-=e^{i\phi_{2}}\bar Q_+\}$, of real dimension two, whose projectivisation is the point carrying the pair $(\phi_{1},\phi_{2})$.

**Corollary (the two distinguished lines).** The two lines of the degenerate quadric of the reduced norm lie on the smooth quadric: $\{Q_+=Q_-\}=\mathcal{F}_{1}(0)$ and $\{Q_+=-Q_-\}=\mathcal{F}_{1}(\pi)$. Both belong to the same ruling, and they are the two members of that ruling fixed by the real structure of the algebra.

**Proof.** Both sets are of the form $Q_-=e^{i\phi}Q_+$ with $\phi=0$ and $\phi=\pi$; on each, $\langle\cdot,\cdot\rangle_{\natural}=Q_{++}Q_{--}$ and $\langle\cdot,\cdot\rangle_{*}$ both vanish, so the line lies on both quadrics.

## Polarity and Tangency

**Proposition (the polarity of $\langle\cdot,\cdot\rangle_{*}$).** The form $\langle\cdot,\cdot\rangle_{*}$ defines a polarity of $\mathbb{P}^{3}_{\mathbb{R}}$ sending a point to a plane, and a point of the quadric is sent to its tangent plane; for a point written $(Q_+,Q_-)$ the polar plane of the point $(Q_{+,0},Q_{-,0})$ is the set of classes of vectors $(Q_+,Q_-)$ with

$$
\operatorname{Re}\bigl(Q_+\bar Q_{+,0}\bigr)-\operatorname{Re}\bigl(Q_-\bar Q_{-,0}\bigr)=0 .
$$

**Proof.** The polarity of a non-degenerate quadratic form is the linear map on projective space induced by the bilinear form; the polar plane of a point is the orthogonal complement of its representative under the bilinear form, and for a point of the quadric the orthogonal complement is the tangent space, because the derivative of $\langle\cdot,\cdot\rangle_{*}$ vanishes exactly along the tangent directions.

**Remark (the degenerate quadric of $\langle\cdot\rangle_{\natural}$).** The reduced norm is a product of two linear forms, so its zero set is a pair of lines and not a smooth quadric. The bilinear form is nevertheless non-degenerate, with radical $\{0\}$ (*The Forms of the Algebra of the Reduced Biquaternions*), so the polarity is defined; what degenerates is the quadric, not the polarity. In the complex reading the polar hyperplane of a point of either line is that line itself, so each of the two lines is self-polar.

## Automorphisms of the Quadric

**Theorem (the automorphism group of the smooth quadric).** The projective automorphisms of the quadric $\{H=0\}$ are the projectivisations of the isometries of $\langle\cdot\rangle_{*}$, and the group is $\mathrm{PO}(2,2)_{\mathbb{R}}$; it acts on the two rulings and is isomorphic to the group $(\mathrm{PGL}_{2}(\mathbb{R})\times\mathrm{PGL}_{2}(\mathbb{R}))\rtimes(\mathbb{Z}/2)$, each copy of $\mathrm{PGL}_{2}(\mathbb{R})$ acting on one ruling, the exchange of the two rulings being the extra involution.

**Proof.** A projective transformation preserves the quadric exactly when the underlying linear map preserves the form up to a scalar, which is the orthogonal group modulo its centre; the two rulings are the two factors of the Segre isomorphism, and every automorphism either preserves each ruling or exchanges them, since the ruling structure is invariant under the form.

**Remark (the interaction with the algebra).** The automorphisms of the quadric form a continuous group of real dimension six, and the automorphism group of the algebra computed in *Reduced Biquaternion Automorphisms and Derivations* is a finite dihedral group of order eight; the two groups are different objects. The algebra automorphisms act on the algebra and carry the forms to the forms, hence act on the quadric, but they are a very small subgroup of the projective automorphism group: the continuous transformations of the quadric are not algebra automorphisms.

## Summary

The reduced biquaternion algebra carries four algebraic norms. The definite one, $\langle \breve Q\rangle_{\natural*}=|Q_+|^{2}+|Q_-|^{2}$, has no null points. The two bilinear ones, $\langle \breve Q\rangle=Q_+^{2}+Q_-^{2}$ and the reduced norm $\langle \breve Q\rangle_{\natural}=Q_+^{2}-Q_-^{2}=Q_{++}Q_{--}$, factor as products of two complex-linear forms, so their projective null sets are degenerate quadrics: a pair of skew lines in $\mathbb{P}^{3}_{\mathbb{R}}$, or a pair of points in the complex reading $\mathbb{P}^{1}_{\mathbb{C}}$. The two lines of the reduced norm are the two minimal ideals $\mathbb{C}\Pi_-$ and $\mathbb{C}\Pi_+$, the two summands of the direct product, which is the reason the null quadric degenerates. The indefinite Hermitian form $\langle\cdot,\cdot\rangle_{*}=|Q_+|^{2}-|Q_-|^{2}$, of real signature $(2,2)$, is the one form whose null quadric is smooth: it is a doubly ruled quadric surface in $\mathbb{P}^{3}_{\mathbb{R}}$, ruled by the two families of totally isotropic planes $Q_-=e^{i\phi}Q_+$ and $Q_-=e^{i\phi}\bar Q_+$, isomorphic to $\mathbb{P}^{1}_{\mathbb{R}}\times\mathbb{P}^{1}_{\mathbb{R}}$ by the Segre map, and the two lines of the reduced norm are two members of one ruling. The form $\langle\cdot,\cdot\rangle_{*}$ induces a polarity whose polar plane at a point of the quadric is the tangent plane, while the null quadric of the reduced norm is degenerate. The projective automorphisms of the smooth quadric form the group $\mathrm{PO}(2,2)_{\mathbb{R}}\cong(\mathrm{PGL}_{2}(\mathbb{R})\times\mathrm{PGL}_{2}(\mathbb{R}))\rtimes(\mathbb{Z}/2)$, which acts on the two rulings and is far larger than the finite group of automorphisms of the algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle \breve Q\rangle=Q_+^{2}+Q_-^{2}$ | the norm of the general plain bilinear product |
| $\langle \breve Q\rangle_{\natural}=Q_+^{2}-Q_-^{2}=Q_{++}Q_{--}$ | the reduced norm, the norm of the general quaternionic bilinear product |
| $\langle \breve Q\rangle_{*}=\lvert Q_+\rvert^{2}-\lvert Q_-\rvert^{2}$ | the norm of the general plain sesquilinear product, indefinite of signature $(2,2)$ |
| $\langle \breve Q\rangle_{\natural*}=\lvert Q_+\rvert^{2}+\lvert Q_-\rvert^{2}$ | the norm of the general quaternionic sesquilinear product, positive definite |
| $Q_+=q_++iq'_+$, $Q_-=q_-+iq'_-$ | the two complex coordinates |
| $Q_{++}=Q_++Q_-$, $Q_{--}=Q_+-Q_-$ | the idempotent coordinates, $\langle \breve Q\rangle_{\natural}=Q_{++}Q_{--}$ |
| $\mathbb{P}^{3}_{\mathbb{R}}$ | the real projective space of the algebra read as a real four-space |
| $\mathbb{P}^{1}_{\mathbb{C}}$ | the complex projective space of the algebra read as a complex two-space |
| $\mathcal{F}_{1}(\phi)=\{Q_-=e^{i\phi}Q_+\}$ | the first ruling of totally isotropic planes |
| $\mathcal{F}_{2}(\phi)=\{Q_-=e^{i\phi}\bar Q_+\}$ | the second ruling of totally isotropic planes |
| $\mathbb{C}\Pi_+=\{Q_+=Q_-\}$, $\mathbb{C}\Pi_-=\{Q_+=-Q_-\}$ | the two minimal ideals, the two lines of the reduced norm |

## Further Reading

- [Reduced Biquaternion Space](reduced-biquaternion-space.html), above this article in this category, for the idempotent coordinates and the isomorphism $\mathbb{B}_{\mathrm{r}}\cong\mathbb{C}\oplus\mathbb{C}$.
- [The Four Products, Their Forms and Their Algebraic Norms](the-four-products-their-forms-and-their-algebraic-norms-of-the-reduced-biquaternions.html), above this article, for the four norms, their Gram matrices and their signatures.
- [Ideals and Peirce Decomposition of the Algebra of the Reduced Biquaternions](ideals-and-peirce-decomposition-of-the-general-plain-algebra-of-the-reduced-biquaternions.html), below this article, for the two minimal ideals that are the lines of the degenerate quadric.
- [Zero Divisors of the Algebra of the Reduced Biquaternions](zero-divisors-of-the-general-plain-algebra-of-the-reduced-biquaternions.html), below this article, for the null cone of the reduced norm as the set of zero divisors.
- [The Null Quadric and Its Projective Geometry](the-null-quadric-and-its-projective-geometry.html), for the non-degenerate case of the biquaternion algebra, where the null quadric is smooth in complex projective three-space.
- [Split-Biquaternion Null Quadric and Projective Geometry](split-biquaternion-null-quadric-and-projective-geometry.html), for the split-complex companion.
