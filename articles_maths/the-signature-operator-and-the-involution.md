
# __The Signature Operator and the Involution__

## Introduction

An isometry of a closed oriented Riemannian manifold acts on the differential forms, it commutes with the Hodge star and with the Laplacian, and it therefore commutes with the **signature operator** and permutes its harmonic forms. The action does not preserve the chirality in general — an orientation-reversing isometry exchanges the self-dual and anti-self-dual parts — and the refined invariant is the **equivariant signature** $\sigma(g,M)$, the trace of the action of an element $g$ on the positive part of the middle cohomology minus the trace on the negative part. The **$G$-signature theorem** of Atiyah and Singer computes this equivariant invariant as a sum of local terms over the fixed point set of $g$, the manifold analogue of a Lefschetz fixed point formula for the signature in place of the Euler characteristic.

The article treats the action of a finite group of isometries on the forms, its compatibility with the star, the Laplacian and the signature operator, the **equivariant index** and its character, the $G$-signature theorem with its local terms at the fixed points, and the parallel between the signature and the Lefschetz fixed point formula for the de Rham complex. The involution on the elements is the induced operator $g^{*}$ on the cohomology, and its fixed part is the invariant cohomology; the harmonic representatives of the invariant classes are the $g$-invariant harmonic forms, and the equivariant signature is the signature of the restriction of the intersection form to the fixed part.

The prerequisites are *The Signature Operator* for the operator, its chirality and the signature theorem; *The Hodge Laplacian* for the harmonic forms and the Hodge decomposition; *Hermitian Pairings on a Topological Space* for the action of a continuous involution on the intersection pairing, the orthogonal decomposition and the signature of the fixed part; *The Atiyah–Singer Index Theorem and K-Theory* for the general index theorem and the equivariant $K$-theory; *Riemannian Geometry* for the isometries and the fixed point sets; and *Transformation Groups and the Erlangen Program* for group actions. The fixed point formula is the original $G$-signature theorem of Atiyah and Singer, and its proof by the index theorem is cited; the Lefschetz fixed point formula for the de Rham complex is stated for comparison. The metric and the action are chosen, and the whole construction is the geometry of that choice. No physics is invoked.

## Isometries and the Action on Forms

Let $(M,g)$ be a closed oriented Riemannian manifold of even dimension $n=2m$, let $\Gamma$ be a finite group acting on $M$ by isometries, and let $\iota\in\Gamma$ be an element with induced map $\iota^{*}$ on the forms.

**Definition.** The **fixed point set** of $\iota$ is $M^{\iota}=\{x\in M:\iota x=x\}$; it is a closed totally geodesic submanifold of $M$ when nonempty, possibly with components of different dimensions, and the action of $\iota$ linearises at a fixed point to an orthogonal transformation of the tangent space, the **isotropy representation**, whose eigenvalues on the tangent space are the roots of unity of the rotation angles of $\iota$ at that point.

**Theorem.** The pullback $\iota^{*}$ commutes with the exterior derivative, $d\iota^{*}=\iota^{*}d$, and with the Hodge star up to the sign of the action on the orientation,

$$
\iota^{*}\star=\det(d\iota)\,\star\iota^{*},
$$

so that $\iota^{*}$ commutes with the Laplacian, $\iota^{*}\Delta=\Delta\iota^{*}$, and with the signature operator in the sense that $\iota^{*}$ preserves the space of harmonic forms. If $\iota$ is orientation-preserving then $\iota^{*}$ commutes with the chirality, $\tau\iota^{*}=\iota^{*}\tau$, and preserves the two eigenspaces $\Omega^{\pm}$; if $\iota$ is orientation-reversing then $\iota^{*}$ anticommutes with the chirality, $\tau\iota^{*}=-\iota^{*}\tau$, and exchanges $\Omega^{+}$ and $\Omega^{-}$.

**Proof.** The pullback commutes with $d$ because $d$ is natural; the action on the star is the change of the volume form under the pullback, $\iota^{*}\mathrm{vol}_g=\det(d\iota)\,\mathrm{vol}_g$, so $\iota^{*}\star=\det(d\iota)\star\iota^{*}$; the commutation with the Laplacian follows from that with $d$ and $d^{*}$, or from the fact that $\iota$ is an isometry and the Laplacian is metric; the chirality is a phase times the star, so the commutation sign is that of the star together with the exchanged degree in the phase, which is the determinant sign. $\square$

**Remark.** The action of $\iota$ descends to the cohomology, and the **invariant cohomology** $H^{*}(M;\mathbb{C})^{\iota}$ is the fixed part of the induced operator; by the Hodge theorem its elements are represented by the $\iota$-invariant harmonic forms, so the fixed part of the cohomology is a space of harmonic forms, and the intersection pairing restricted to it is the pairing of *Hermitian Pairings on a Topological Space*. The orthogonal decomposition of the cohomology under an involution, and the splitting of the signature over the eigenspaces, are those of that article.

## Equivariance of the Signature Operator

**Theorem.** The signature operator $D=d+d^{*}$ commutes with the action of every isometry, $D\iota^{*}=\iota^{*}D$, so the spaces $\Omega^{\pm}(M)$ are $\Gamma$-modules; when $\iota$ is orientation-preserving the operators $D^{\pm}:\Omega^{\pm}\to\Omega^{\mp}$ are $\Gamma$-equivariant, and the kernels $\ker D^{\pm}$ are finite-dimensional $\Gamma$-modules. When $\iota$ is orientation-reversing the operator $D$ is still equivariant but it exchanges the chirality eigenspaces, and the pairing between the parts is a $\Gamma$-antilinear duality.

**Proof.** The exterior derivative is natural for the action and the codifferential is natural for an isometry because the metric is preserved; hence $D$ commutes with $\iota^{*}$, and the chirality commutation of the preceding theorem gives the preservation or the exchange of the parts. The finite-dimensionality of the kernels is the ellipticity of $D$. $\square$

**Definition.** For an element $g\in\Gamma$ the **equivariant index** of the signature operator is the virtual trace

$$
\operatorname{ind}_g(D^{+})=\operatorname{tr}\bigl(g\mid\ker D^{+}\bigr)-\operatorname{tr}\bigl(g\mid\operatorname{coker}D^{+}\bigr),
$$

the difference of the traces of the action on the harmonic self-dual and anti-self-dual middle forms; for $g=1$ it is the signature $\sigma(M)$, and for a general $g$ it is the **$g$-signature** (or equivariant signature) $\sigma(g,M)$.

**Theorem.** The equivariant index is constant on the conjugacy classes of $\Gamma$ and is a $\Gamma$-cobordism invariant; it is additive under the disjoint union and multiplicative under products, and it depends on the action of $g$ on the cohomology through the character

$$
\operatorname{ind}_g(D^{+})=\operatorname{tr}\bigl(g\mid H^{2k}_{+}(M)\bigr)-\operatorname{tr}\bigl(g\mid H^{2k}_{-}(M)\bigr),
$$

where $H^{2k}_{\pm}$ are the self-dual and anti-self-dual middle cohomology.

**Proof.** The equality of the analytic and topological traces is the Hodge theorem applied equivariantly: the harmonic forms are the cohomology, and $g$ preserves the harmonic forms and the chirality; the cobordism invariance is the invariance of the index under the equivariant deformations, as for the ordinary index. $\square$

## The $G$-Signature Theorem

**Theorem ($G$-signature theorem, Atiyah–Singer).** Let $M$ be a closed oriented Riemannian $4k$-manifold with a finite group $\Gamma$ acting isometrically, and let $g\in\Gamma$. Then the $g$-signature is computed from the fixed point set of $g$,

$$
\sigma(g,M)=\sum_{F\subseteq M^{g}}\sigma(g,F,\nu),
$$

where the sum is over the connected components $F$ of the fixed point set and the term depends only on the action of $g$ on the normal bundle $\nu$ of $F$ and on the restriction of the metric to $F$; introduced by Atiyah and Singer and proved by their equivariant index theorem, the formula expresses the equivariant invariant as a sum of **local terms** supported on the fixed point set.

**Theorem (isolated fixed points).** Let $g$ have an isolated fixed point $p$, let the isotropy representation of $g$ on $T_pM$ have rotation angles $\theta_1,\dots,\theta_{2k}\in(0,2\pi)$, and let the orientation be that in which the angles are measured. Then the contribution of $p$ to the $g$-signature is, up to the normalisation of the characteristic classes,

$$
\prod_{j=1}^{2k}\cot\frac{\theta_j}{2},
$$

the product of the cotangents of the half-angles; the formula is the local form of the $G$-signature theorem at an isolated fixed point, and the contributions of the higher-dimensional fixed components are the corresponding expressions in the Chern classes of the normal bundle and in the classes of the fixed submanifold.

**Proof sketch.** The equivariant index is computed by the equivariant index theorem, whose local density at a fixed point is the character of the $g$-action on the symbol of the signature operator; at an isolated fixed point the symbol is the product of the rotation factors, and the resulting density integrates to the product of the cotangents. The computation is the Atiyah–Singer $G$-index theorem in the case of the signature operator, and the corresponding fixed point formula of Atiyah–Bott for the elliptic complexes. $\square$

**Corollary.** If the action of $g$ is free — the fixed point set empty — then $\sigma(g,M)=0$. If $g=1$ the theorem is the signature theorem, $\sigma(1,M)=\sigma(M)=\int_ML(TM)$, the sum of the local terms reducing to the integral of the $L$-class. If $g$ is orientation-reversing and fixes an isolated point, the contribution is the product of the cotangents, and the equivariant signature need not be the signature of the fixed part.

**Remark.** The $G$-signature theorem is the refinement of the signature theorem to the equivariant setting and the exact analogue, for the signature, of the **Lefschetz fixed point formula** for the Euler characteristic. The two are the two characteristic numbers of the de Rham complex: the signature corresponds to the $L$-class and the fixed point formula for it to the $G$-signature theorem, the Euler characteristic to the Euler class and the fixed point formula for it to the Lefschetz formula. The refinement of the signature to the fixed part is the algebraic statement of *Hermitian Pairings on a Topological Space*, and the analysis that computes the fixed part from the fixed point set is the $G$-signature theorem.

## Lefschetz and the Local Terms

**Theorem (Lefschetz fixed point formula).** Let $M$ be a closed oriented manifold with a finite group $\Gamma$ acting smoothly, and let $g\in\Gamma$ have fixed point set $M^{g}$. Then the **Lefschetz number**

$$
L(g)=\sum_{q}(-1)^{q}\operatorname{tr}\bigl(g\mid H^{q}(M;\mathbb{Q})\bigr)
$$

equals the Euler characteristic of the fixed point set,

$$
L(g)=\chi(M^{g}),
$$

when the fixed point set is a smooth submanifold; the number $L(g)$ is the equivariant index of the Gauss–Bonnet operator, the analogue for the Euler characteristic of the equivariant signature.

**Proof sketch.** The Lefschetz number is the supertrace of the action on the de Rham complex, hence the index of the equivariant Gauss–Bonnet operator $d+d^{*}$ graded by the total degree; the local density of the equivariant index is supported on the fixed point set and integrates to the Euler characteristic of the fixed manifold, by the same equivariant index theorem used for the $G$-signature theorem. $\square$

**Remark.** The two fixed point formulas are the two ends of the index theory of the de Rham complex: the total-degree grading gives the Lefschetz number and the Euler characteristic of the fixed set, and the chirality grading gives the $g$-signature and the local terms of the $G$-signature theorem. Both are specialisations of the equivariant Atiyah–Singer index theorem, whose general statement is in *The Atiyah–Singer Index Theorem and K-Theory*; the algebraic version of the action of an involution on a pairing is *Hermitian Pairings on a Topological Space*.

## Examples

**Example (the antipodal map of the sphere).** The antipodal map $a$ of $S^{4k}$ is a free isometry, so its fixed point set is empty and the $G$-signature theorem gives $\sigma(a,S^{4k})=0$; consistently the signature of the sphere is zero and the cohomology in the middle degree vanishes, so the equivariant index is zero. For the sphere the involution acts on the only nonzero cohomology, that in degrees $0$ and $n$, by the degree $(-1)^{n+1}$, which is the model computed in *Hermitian Pairings on a Topological Space*.

**Example (complex conjugation on a projective space).** Complex conjugation on $\mathbb{CP}^{2}$ is an isometry of the Fubini–Study metric whose fixed point set is $\mathbb{RP}^{2}$, of real dimension two; the induced map on $H^{2}(\mathbb{CP}^{2})=\mathbb{Z}$ is multiplication by $-1$ or by $+1$ according to the normalisation of the conjugation, and the $g$-signature is $\pm1$, computed by the $G$-signature theorem from the fixed surface $\mathbb{RP}^{2}$ and its normal bundle. The example shows that the equivariant signature is a genuine refinement of the signature, which is the value at the identity.

**Example (an involution with isolated fixed points).** Let $\mathbb{Z}/2$ act on a closed oriented four-manifold with isolated fixed points; at each fixed point the isotropy representation has two rotation angles, each equal to $\pi$ for an involution acting with determinant $+1$ on the tangent space, and the local contribution is $\cot(\pi/2)^{2}=0$; the $g$-signature is then zero, which is compatible with the fact that an involution of a four-manifold acting with isolated fixed points and orientation-preserving has $\sigma(g,M)=0$. A holomorphic involution of a complex surface fixes a union of points and curves, and the contributions of the curves are the nonvanishing terms.

## Summary

A finite group of **isometries** of a closed oriented manifold acts on the forms by pullback, commuting with the exterior derivative and the Laplacian and with the star up to the determinant sign; it therefore commutes with the **signature operator**, preserving the chirality when the element is orientation-preserving and exchanging it when the element is orientation-reversing. The **equivariant index** $\operatorname{ind}_g(D^{+})=\operatorname{tr}(g|\ker D^{+})-\operatorname{tr}(g|\operatorname{coker}D^{+})$ is the **$g$-signature** $\sigma(g,M)$, equal to the difference of the traces of $g$ on the self-dual and anti-self-dual middle cohomology, and equal to the signature for $g=1$; it is a $\Gamma$-cobordism invariant constant on conjugacy classes. The **$G$-signature theorem** computes it as a sum of local terms over the fixed point set of $g$, the term at an isolated fixed point being the product $\prod_j\cot(\theta_j/2)$ of the half-angles; the theory is the equivariant refinement of $\sigma(M)=\int_ML(TM)$. The **Lefschetz fixed point formula** $L(g)=\chi(M^{g})$ is the parallel statement for the total-degree grading and the Euler characteristic, and the two fixed point formulas are the two specialisations of the equivariant index theorem. The action of an involution on the intersection pairing and the signature of its fixed part are the algebraic statements of *Hermitian Pairings on a Topological Space*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Gamma$, $\iota$, $g$ | Finite group of isometries, an element, its action |
| $M^{g}$ | Fixed point set of $g$; isotropy representation on the normal bundle |
| $\iota^{*}\star=\det(d\iota)\star\iota^{*}$ | The star commutes with the pullback up to the determinant sign |
| $\sigma(g,M)=\operatorname{ind}_g(D^{+})$ | $g$-signature, equivariant index |
| $\operatorname{tr}(g\mid H^{2k}_{\pm})$ | Traces on the self-dual and anti-self-dual middle cohomology |
| $\sigma(g,M)=\sum_{F\subseteq M^{g}}\sigma(g,F,\nu)$ | The $G$-signature theorem |
| $\prod_j\cot(\theta_j/2)$ | Local term at an isolated fixed point, rotation angles $\theta_j$ |
| $L(g)=\sum_q(-1)^q\operatorname{tr}(g\mid H^q)$ | Lefschetz number |
| $L(g)=\chi(M^{g})$ | Lefschetz fixed point formula |

## Further Reading

- Michael F. Atiyah and Isadore M. Singer, "The index of elliptic operators III," *Annals of Mathematics* **87** (1968), 546–604, for the $G$-signature theorem and the fixed point formula.
- Michael F. Atiyah and Raoul Bott, "A Lefschetz fixed point formula for elliptic complexes I, II," *Annals of Mathematics* **86** (1967), 374–407 and **88** (1968), 451–491, for the fixed point formula for elliptic complexes and the Lefschetz formula.
- Friedrich Hirzebruch and Dietmar Zagier, *The Atiyah–Singer Theorem and Elementary Number Theory* (Publish or Perish, 1974), for the equivariant signature and its number-theoretic applications.
- Glen E. Bredon, *Introduction to Compact Transformation Groups* (Academic Press, 1972), for group actions on manifolds, fixed point sets and the equivariant invariants.
- Nicole Berline, Ezra Getzler and Michèle Vergne, *Heat Kernels and Dirac Operators* (Springer, 1992), for the equivariant local index theorem and the fixed point densities.
- Peter B. Gilkey, *Invariance Theory, the Heat Equation and the Atiyah–Singer Index Theorem* (CRC Press, 2nd ed. 1995), for the equivariant index density of the signature operator and the $L$-class.
