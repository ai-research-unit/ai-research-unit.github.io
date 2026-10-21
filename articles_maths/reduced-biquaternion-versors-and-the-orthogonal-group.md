# __Reduced Biquaternion Versors and the Orthogonal Group__

## Introduction

The reduced biquaternion algebra is the commutative algebra $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\oplus\mathbb{C}$ of basis $1,i,j,ij$, with idempotent coordinates $(Q_{++},Q_{--})=(Q_++Q_-,Q_+-Q_-)$ and element $\breve Q=Q_++jQ_-$. Its general quaternionic bilinear product carries the form

$$
\langle \breve Q_{1},\breve Q_{2}\rangle_{\natural}=\mathrm{Sc}(\breve Q_{1}^{\natural}\breve Q_{2})=Q_{1+}Q_{2+}-Q_{1-}Q_{2-},
$$

whose quadratic form is the reduced norm $\langle \breve Q\rangle_{\natural}=Q_+^{2}-Q_-^{2}=Q_{++}Q_{--}$, the multiplicative norm and the invertibility criterion. This form is non-degenerate, and it is the one form of the algebra whose isometry group is the subject of the article. The elements that act on the space by multiplication preserving the form are the versors, and they form a group; the article identifies that group, its action on the orthogonal group, and the part of the orthogonal group that the multiplication cannot reach.

The reduced algebra degenerates in a way that makes the answer exact. The form is the hyperbolic plane: in the idempotent basis its Gram matrix is the off-diagonal pair, so the algebra is the even Clifford algebra of a hyperbolic plane, and its versors form the spin group of that plane. The multiplication by a versor realises the identity component of the orthogonal group and nothing else, because the algebra is commutative and its multiplicative action is connected; the reflections are odd elements of the full Clifford algebra, and the algebra reaches them only through its involutions, not through its units.

The article owns the bilinear form $\langle\cdot,\cdot\rangle_{\natural}$, its isometry group, the versor group and its structure, its faithful action on the orthogonal group, and the failure of the multiplication to reach the reflections and the Pin group. The four general products and the four norms are *The Four Products, Their Forms and Their Algebraic Norms*; the multiplication operators $L_{P}$ and their norms are *The Multiplication Operators of the Algebra of the Reduced Biquaternions*; the action of the units on the space, the two-dimensional rotations, the Lorentz transformations and the isometry groups of the four forms are *Reduced Biquaternion Rotations and Lorentz Transformations*, which owns the multiplicative action and is cited here rather than restated; the invertibility criterion is *Norm and Invertibility in the Algebra of the Reduced Biquaternions*; the null cone of the form is *Zero Divisors of the Algebra of the Reduced Biquaternions* and its projective geometry is *The Null Quadric and Its Projective Geometry*. The companion is *Biquaternion Versors and the Orthogonal Group*, where the algebra is the even part of a Clifford algebra of Lorentzian space and realises the proper orthochronous Lorentz transformations.

## The Bilinear Form and Its Isometries

**Proposition (the form is the hyperbolic plane).** The form $\langle \breve Q_{1},\breve Q_{2}\rangle_{\natural}=\mathrm{Sc}(\breve Q_{1}^{\natural}\breve Q_{2})=Q_{1+}Q_{2+}-Q_{1-}Q_{2-}$ is a symmetric, non-degenerate $\mathbb{C}$-bilinear form on the two-complex-dimensional algebra; on the complex basis $1,j$ its Gram matrix is $\operatorname{diag}(1,-1)$, and on the idempotent basis $\Pi_+,\Pi_-$ it is

$$
\begin{pmatrix}0&\tfrac12\\[2pt]\tfrac12&0\end{pmatrix},
$$

so the form is the split form of rank two, the hyperbolic plane.

**Proof.** $\langle\Pi_+,\Pi_-\rangle_{\natural}=\mathrm{Sc}(\Pi_+^{\natural}\Pi_-)=\mathrm{Sc}\bigl(\tfrac12(1-j)\cdot\tfrac12(1-j)\bigr)=\mathrm{Sc}\bigl(\tfrac12(1-j)\bigr)=\tfrac12$, while $\langle\Pi_+,\Pi_+\rangle_{\natural}=\mathrm{Sc}\bigl(\tfrac14(1-j)(1+j)\bigr)=0$ and likewise for $\Pi_-$; the matrix is therefore the off-diagonal pair. The Gram matrix in the basis $1,j$ is $\operatorname{diag}(1,-1)$ by the same computation with $\langle1,1\rangle_{\natural}=1$ and $\langle j,j\rangle_{\natural}=-1$.

**Corollary (the quadratic form is the reduced norm).** $\langle \breve Q,\breve Q\rangle_{\natural}=\langle \breve Q\rangle_{\natural}=Q_+^{2}-Q_-^{2}=Q_{++}Q_{--}$.

**Proof.** $\langle \breve Q,\breve Q\rangle_{\natural}=\mathrm{Sc}(\breve Q^{\natural}\breve Q)=\mathrm{Sc}(Q_+^{2}-Q_-^{2})=Q_+^{2}-Q_-^{2}$.

**Definition (isometry, versor).** An **isometry** of the form is a $\mathbb{C}$-linear map $g$ of the algebra with $\langle g\breve Q_{1},g\breve Q_{2}\rangle_{\natural}=\langle \breve Q_{1},\breve Q_{2}\rangle_{\natural}$ for all $\breve Q_{1},\breve Q_{2}$; the group of them is the **orthogonal group** $O(\mathbb{B}_{\mathrm{r}},\langle\cdot,\cdot\rangle_{\natural})$, denoted $O(2,\mathbb{C})$ for the hyperbolic plane. A **versor** is a unit $P$ with $\langle P\rangle_{\natural}=1$.

**Proposition (scaling of the form by a multiplication).** For every element $P$ and all $\breve Q_{1},\breve Q_{2}$,

$$
\langle P \breve Q_{1},P \breve Q_{2}\rangle_{\natural}=\langle P\rangle_{\natural}\,\langle \breve Q_{1},\breve Q_{2}\rangle_{\natural}.
$$

**Proof.** $\mathrm{Sc}((P \breve Q_{1})^{\natural}P \breve Q_{2})=\mathrm{Sc}(P^{\natural}\breve Q_{1}^{\natural}P \breve Q_{2})=\mathrm{Sc}(P^{\natural}P\,\breve Q_{1}^{\natural}\breve Q_{2})=\langle P\rangle_{\natural}\,\mathrm{Sc}(\breve Q_{1}^{\natural}\breve Q_{2})$, using that the algebra is commutative and that $P^{\natural}P=\langle P\rangle_{\natural}$.

**Corollary (the isometries among the multiplications).** The left multiplication $L_{P}$ by a unit is an isometry of the form exactly when $P$ is a versor; a general unit scales the form by $\langle P\rangle_{\natural}$, hence acts as a similitude of ratio $\langle P\rangle_{\natural}$.

## The Versors and Their Structure

**Theorem (the versor group).** The versors of the algebra form the abelian group

$$
\mathrm{Vers}(\mathbb{B}_{\mathrm{r}})=\{P:\langle P\rangle_{\natural}=1\}=\{Q_{++}\Pi_++Q_{++}^{-1}\Pi_-:Q_{++}\in\mathbb{C}^{\times}\}\cong\mathbb{C}^{\times},
$$

which is the split torus of real dimension two; it is non-compact and has fundamental group $\mathbb{Z}$.

**Proof.** $\langle P\rangle_{\natural}=Q_{++}Q_{--}=1$ forces $Q_{++}\neq0$ and $Q_{--}=Q_{++}^{-1}$, so the versors are the pairs $(Q_{++},Q_{++}^{-1})$ with $Q_{++}$ nonzero; the multiplication is componentwise, $(Q_{++},Q_{++}^{-1})(w,w^{-1})=(Q_{++}w,Q_{++}^{-1}w^{-1})=(Q_{++}w,(Q_{++}w)^{-1})$, which identifies the group with $\mathbb{C}^{\times}$ by the first coordinate. The group $\mathbb{C}^{\times}$ is a real two-dimensional torus in the split sense, non-compact, homotopy equivalent to the circle.

**Theorem (the action gives the identity component).** The map $P\mapsto L_{P}$ from the versor group to the orthogonal group is an injective homomorphism onto the identity component $SO(2,\mathbb{C})$, with trivial kernel, so it is an isomorphism

$$
\mathrm{Vers}(\mathbb{B}_{\mathrm{r}})\cong SO(2,\mathbb{C})\cong\mathbb{C}^{\times},
$$

sending the versor $Q_{++}\Pi_++Q_{++}^{-1}\Pi_-$ to the hyperbolic rotation of parameter $Q_{++}$ in the coordinates above.

**Proof.** $L_{P}L_{W}=L_{PW}$, so the map is a homomorphism; it is an isometry by the corollary above and it is $\mathbb{C}$-linear, so its image lies in the orthogonal group, and its determinant is $\det L_{P}=\langle P\rangle_{\natural}=1$, since $L_{P}$ has the matrix $\left(\begin{smallmatrix}Q_+&Q_-\\ Q_-&Q_+\end{smallmatrix}\right)$ on the basis $1,j$, so the image lies in the identity component. Its kernel is the set of $P$ with $L_{P}$ the identity; a unit acting trivially must satisfy $P=L_{P}(1)=1$, so the kernel is $\{1\}$ and the map is injective. It is also surjective: for the form $\operatorname{diag}(1,-1)$ an element of the identity component has the matrix $\left(\begin{smallmatrix}Q_+&Q_-\\ Q_-&Q_+\end{smallmatrix}\right)$ with $Q_+^{2}-Q_-^{2}=1$, which is $L_{P}$ for the versor $P=Q_++jQ_-$. Both groups are isomorphic to $\mathbb{C}^{\times}$ and the map is that isomorphism. Because the algebra is commutative the conjugation $P \breve Q P^{-1}$ is the identity, so the standard spin action is trivial and the two-to-one covering is not the mechanism here: the versors are abstractly the spin group $\mathrm{Spin}(2,\mathbb{C})\cong\mathbb{C}^{\times}$ of the plane, but they act faithfully on the space, by left multiplication, and the realised map is an isomorphism rather than a double covering.

**Corollary (the algebra is the even Clifford algebra of the form).** The algebra is isomorphic to the even Clifford algebra of the hyperbolic plane, $\mathbb{B}_{\mathrm{r}}\cong \mathrm{Cl}^{+}(\mathbb{C}^{2},\langle\cdot,\cdot\rangle_{\natural})\cong\mathbb{C}\oplus\mathbb{C}$, and the versors are its spin group.

**Proof.** The even Clifford algebra of a two-dimensional non-degenerate quadratic space is the sum of two copies of the base field, the two projections being the two idempotent coordinates; the identification is the isomorphism $\mathbb{B}_{\mathrm{r}}\cong\mathbb{C}\oplus\mathbb{C}$ of *Reduced Biquaternion Space*, and the versor group of the even Clifford algebra is its spin group.

## What the Multiplication Does Not Reach

**Proposition (the reflections are not multiplications).** The reflection of the hyperbolic plane that negates the $j$-direction, $Q_++jQ_-\mapsto Q_+-jQ_-$, is the natural sign ${}^{\natural}$; it is a $\mathbb{C}$-linear isometry of the form with determinant $-1$, but it is not the left multiplication by any element.

**Proof.** $\langle \breve Q_{1}^{\natural},\breve Q_{2}^{\natural}\rangle_{\natural}=\mathrm{Sc}((\breve Q_{1}^{\natural})^{\natural}\breve Q_{2}^{\natural})=\mathrm{Sc}(\breve Q_{1}\breve Q_{2}^{\natural})=\mathrm{Sc}(\breve Q_{1}^{\natural}\breve Q_{2})$ because the scalar part of the $\natural$-product is symmetric, so ${}^{\natural}$ preserves the form; in the basis $1,j$ it is $\operatorname{diag}(1,-1)$, of determinant $-1$. If it were $L_{P}$ for some $P=P_{0}+P_{1}j$, then $L_{P}$ would send $1$ to $P_{0}+P_{1}j$ and $j$ to $P_{1}+P_{0}j$, that is it would be the matrix $\left(\begin{smallmatrix}P_{0}&P_{1}\\ P_{1}&P_{0}\end{smallmatrix}\right)$ on the basis $(1,j)$, whereas ${}^{\natural}$ is $\operatorname{diag}(1,-1)$; the two agree only for $P_{1}=0$ with $P_{0}=1$ in the first column, which then gives the second column $(0,1)$ and not $(0,-1)$.

**Corollary (the algebra reaches the reflections only through the involutions).** The orthogonal group of the form is realised on the algebra, its identity component by the left multiplications and its other component by the reflections: the reflection of the $j$-direction is the involution ${}^{\natural}$, and the other involutions $\bar{\cdot}$ and ${}^{*}$ preserve the form only up to the coefficient conjugation. None of these reflections is a left multiplication. The Pin group, whose elements are the products of odd numbers of reflections, is not contained in the algebra either; it lies in the full Clifford algebra, whose odd part is a second copy of the algebra as a vector space.

**Proof.** The orthogonal group of a two-dimensional non-degenerate form has two components, distinguished by the determinant; the identity component is reached by the versors, and any element of the other component is a reflection composed with an element of the identity component, hence needs a reflection. The reflection of the plane is the involution negating one isotropic direction, and the involutive isometries available from the algebra's own structure are those of *The Two Involutions and the Group of Involutions*; the Clifford conjugations that give the odd elements lie in the odd part of the Clifford algebra, and the algebra is the even part by the corollary above, so an odd element is not in it.

**Remark (the contrast with the biquaternion algebra).** There the algebra is the even part of the Clifford algebra of Lorentzian space, so it composes an even number of reflections and realises the proper orthochronous Lorentz group; the reflections are again outside the algebra, in the odd slot. The reduced case is the same picture in the smallest dimension: the even part is the algebra, the versors give the identity component, and the reflections need the odd part. What is special here is that the algebra is commutative, so the even Clifford algebra is the sum of two fields and the spin group is a torus.

## Versors of the Definite Form, for Comparison

**Proposition (the versors of the definite form).** The form $\langle \breve Q\rangle_{\natural*}=|Q_+|^{2}+|Q_-|^{2}$ is positive definite, and the group of its multiplicative isometries is the torus $\mathbb{T}^{2}=\{P:|Q_{++}|=|Q_{--}|=1\}$, which is the maximal compact subgroup of the unit group and is studied in *The Unitary Group of the Reduced Biquaternion Algebra*. The compact versor $\{P:\langle P\rangle_{\natural*}=1\}=S^{3}$ is not a group.

**Proof.** $\langle P \breve Q\rangle_{\natural*}$ equals $\tfrac12\bigl(|p|^{2}|Q_{++}|^{2}+|q|^{2}|Q_{--}|^{2}\bigr)$ in the idempotent coordinates, so $\langle\cdot\rangle_{\natural*}$ is preserved for all $\breve Q$ exactly when $|p|=|q|=1$. The set $\{\langle P\rangle_{\natural*}=1\}$ is the unit sphere of the four-real-dimensional space, and it is not closed under multiplication: for a definite form the product $\langle P \breve Q_{2}\rangle_{\natural*}$ is not $\langle P\rangle_{\natural*}\langle \breve Q_{2}\rangle_{\natural*}$ in general, and $\langle\cdot,\cdot\rangle_{\natural*}$ is not multiplicative for the multiplication, unlike the reduced norm $\langle\cdot\rangle_{\natural}$, which is.

**Remark (the two versor groups).** The bilinear form gives the non-compact versor group $\{N=1\}\cong\mathbb{C}^{\times}$, homotopy equivalent to a circle, and the definite form gives the compact group $\mathbb{T}^{2}$, homotopy equivalent to a two-torus. Both sit inside the unit group $\mathbb{C}^{\times}\times\mathbb{C}^{\times}$: the first is the graph $\{q=p^{-1}\}$ of the inversion, a split torus, and the second is the product of the two unit circles, the compact maximal torus. They meet in the diagonal circle $\{(Q_{++},\bar Q_{++}):|Q_{++}|=1\}\cong \mathrm{U}(1)$, which is the unitary group of the split-complex plane $\mathbb{R}\{1,j\}$.

## Worked Examples

**The hyperbolic basis.** In the idempotent basis the versor $P=Q_{++}\Pi_++Q_{++}^{-1}\Pi_-$ acts on the coordinates by multiplication by $Q_{++}$ in the first and by $Q_{++}^{-1}$ in the second, so it is the hyperbolic rotation of the plane $\{j\}$ with parameter $Q_{++}$; the reflection ${}^{\natural}$ exchanges the two coordinates on the $1,j$-basis and negates the $j$-direction.

**A reflection is not a versor action.** The natural sign sends $1$ to $1$ and $j$ to $-j$; no left multiplication sends $1$ to $1$ and $j$ to $-j$, since left multiplication by $P$ sends $1$ to $P$ and $j$ to $P^{\natural}$; the two would force $P=1$ and then $P^{\natural}=1\neq-j$.

**Verification.** The Gram matrices, the scaling identity $\langle P \breve Q_{1},P \breve Q_{2}\rangle_{\natural}=\langle P\rangle_{\natural}\langle \breve Q_{1},\breve Q_{2}\rangle_{\natural}$, the preservation of the form by the versors, the preservation of $\langle\cdot,\cdot\rangle_{\natural*}$ by the torus and the preservation of $\langle\cdot,\cdot\rangle_{*}$ by the group $\{pq^{*}=1\}$ were checked by recomputation on random elements of the algebra; the deviations found were at the level of the floating-point noise.

## Summary

The general quaternionic bilinear form of the reduced biquaternion algebra, $\langle \breve Q_{1},\breve Q_{2}\rangle_{\natural}=Q_{1+}Q_{2+}-Q_{1-}Q_{2-}$, is non-degenerate and is the hyperbolic plane; in the idempotent basis its Gram matrix is the off-diagonal pair and its quadratic form is the reduced norm $\langle \breve Q\rangle_{\natural}=Q_+^{2}-Q_-^{2}=Q_{++}Q_{--}$. The algebra is therefore the even Clifford algebra $\mathrm{Cl}^{+}(\mathbb{C}^{2})$ of that plane, isomorphic to $\mathbb{C}\oplus\mathbb{C}$. The versors, the elements of norm one, form the split torus $\{Q_{++}\Pi_++Q_{++}^{-1}\Pi_-\}\cong\mathbb{C}^{\times}$, abstractly the spin group $\mathrm{Spin}(2,\mathbb{C})$; the left multiplication by a versor is an isometry of the form, and the map from the versor group to the orthogonal group is an isomorphism onto the identity component $SO(2,\mathbb{C})\cong\mathbb{C}^{\times}$, the versor $Q_{++}\Pi_++Q_{++}^{-1}\Pi_-$ going to the hyperbolic rotation of parameter $Q_{++}$ (the standard two-to-one spin covering degenerates here, because the conjugation is trivial in a commutative algebra). The multiplication reaches only the identity component: the reflections of the plane are the involutions of the algebra, the natural sign being the example, and they are not left multiplications; the Pin group lies in the odd part of the Clifford algebra and not in the algebra. The same algebra carries the definite form $\langle\cdot,\cdot\rangle_{\natural*}=|Q_+|^{2}+|Q_-|^{2}$, whose multiplicative isometries form the compact torus $\mathbb{T}^{2}$, the compact companion of the non-compact versor group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle \breve Q_{1},\breve Q_{2}\rangle_{\natural}=\mathrm{Sc}(\breve Q_{1}^{\natural}\breve Q_{2})=Q_{1+}Q_{2+}-Q_{1-}Q_{2-}$ | the general quaternionic bilinear form |
| $\langle \breve Q\rangle_{\natural}=Q_+^{2}-Q_-^{2}=Q_{++}Q_{--}$ | the reduced norm, the quadratic form of $\langle\cdot,\cdot\rangle_{\natural}$ |
| $\langle\Pi_+,\Pi_-\rangle_{\natural}=\tfrac12$ | the hyperbolic Gram matrix in the idempotent basis |
| $\mathrm{Vers}(\mathbb{B}_{\mathrm{r}})=\{N=1\}$ | the versor group, $\cong\mathbb{C}^{\times}$ |
| $L_{P}$ | the left multiplication by $P$, an isometry exactly for a versor |
| $\mathrm{Vers}(\mathbb{B}_{\mathrm{r}})\cong SO(2,\mathbb{C})$ | the versor group as the identity component, via $P\mapsto L_{P}$ |
| ${}^{\natural}$ | the natural sign, a reflection of the form, not a left multiplication |
| $\mathbb{T}^{2}=\{\lvert Q_{++}\rvert=\lvert Q_{--}\rvert=1\}$ | the torus of multiplicative isometries of the definite form $\langle\cdot,\cdot\rangle_{\natural*}$ |
| $\langle \breve Q\rangle_{\natural*}=\lvert Q_+\rvert^{2}+\lvert Q_-\rvert^{2}$ | the positive definite norm, the topological norm |

## Further Reading

- [Reduced Biquaternion Space](reduced-biquaternion-space.html), above this article in this category, for the idempotents and the isomorphism $\mathbb{B}_{\mathrm{r}}\cong\mathbb{C}\oplus\mathbb{C}$.
- [The Four Products, Their Forms and Their Algebraic Norms](the-four-products-their-forms-and-their-algebraic-norms-of-the-reduced-biquaternions.html), above this article, for the four forms, their Gram matrices and the reduced norm.
- [The Two Involutions and the Group of Involutions](the-two-involutions-and-the-group-of-involutions-of-the-reduced-biquaternions.html), above this article, for the bar, the natural sign, the star and the flat that realise the reflections.
- [The Multiplication Operators of the Algebra of the Reduced Biquaternions](the-multiplication-operators-of-the-general-plain-algebra-of-the-reduced-biquaternions.html), below this article, for the operators $L_{P}$ and $R_{P}$ and their norms.
- [Reduced Biquaternion Rotations and Lorentz Transformations](reduced-biquaternion-rotations-and-lorentz-transformations.html), above this article, for the multiplicative action on the space and the isometry groups of the four forms.
- [Biquaternion Versors and the Orthogonal Group](biquaternion-versors-and-the-orthogonal-group.html), for the companion in which the algebra is the even part of the Clifford algebra of Lorentzian space.
