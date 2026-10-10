
# __Operators of the Real Biquaternion Algebra__

## Introduction

The biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ acts on itself by left and right multiplication, and the two-sided sandwich $\tilde X\mapsto\tilde Q\tilde X\tilde Q^{*}$ is the product of one of each. These operators, their composition laws, their adjoints for the scalar form of the dagger and the three types — self-adjoint, skew-adjoint, unitary — are the subject of *One-Sided Operators on the General Plain Sesqualgebra of Biquaternions* and *Two-Sided Operators on the General Plain Sesqualgebra of Biquaternions*, which read them over $\mathbb{C}$. This article reads the same operators **over $\mathbb{R}$**: the two families as real endomorphisms of $\mathbb{B}\cong\mathbb{R}^{8}$, their adjoints for the four realified forms of *The Realification of the Four Forms*, and the real Cartan decomposition of the operator algebra that the dagger defines.

The article turns on the fact that the operator theory is already real, and that the real reading adds the Cartan structure. Every operator of the corpus is $\mathbb{C}$-linear in its argument and hence real-linear; the left multiplication $L_{\tilde Q}$ is real-linear in its parameter; and the dagger, though conjugate-linear, acts on the eight real coordinates as an orthogonal map for the realified Hermitian form. The three real groups that the realified forms single out — the compact unitary group $U(2)$ of the unit slice, and the orthogonal groups $O(4)$ and $O(1,3)$ of the definite and the interval restrictions of the two indefinite forms on the quaternion and Hermitian subspaces — are read off from those operators.

The organising theorem is the Cartan decomposition of the operator algebra. The Cartan involution $\theta(\tilde Q)=(\tilde Q^{*})^{-1}$ of the unit group has differential $\mathrm{d}\theta=-{}^{*}$, whose eigenspaces are the anti-Hermitian and the Hermitian sectors: the real Lie algebra splits as

$$
\mathfrak{gl}(2,\mathbb{C})=\mathbb{M}_{-}\oplus\mathbb{M}_{+}\cong u(2)\oplus H_{2}(\mathbb{C}),
$$

and the group of units decomposes as $\mathbb{B}^{\times}=U(2)\cdot\exp(\mathbb{M}_{+})$. The decomposition is the real form of the operator theory, and the article is its reading.

**Boundary.** The complex statements of the operator theory are *One-Sided Operators on the General Plain Sesqualgebra of Biquaternions* and *Two-Sided Operators on the General Plain Sesqualgebra of Biquaternions*, and their positivity and Cartan structure is *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint*, whose §*The Cartan Involution* is quoted here and not repeated. The forms are *The Realification of the Four Forms*; the trace form is the companion *The Trace Form of the Real Biquaternion Algebra*; the general one-sided and two-sided theories are *One-Sided Operators on a Clifford Algebra* and *Two-Sided Operators on a Clifford Algebra*.

## The One-Sided Operators

**Definition (the left and right multiplications).** For $\tilde B,\tilde C\in\mathbb{B}$ the **left multiplication by $\tilde B$** and the **right multiplication by $\tilde C$** are the real endomorphisms of $\mathbb{B}$ with

$$
L_{\tilde B}(\tilde V)=\tilde B\,\tilde V,\qquad R_{\tilde C}(\tilde V)=\tilde V\,\tilde C .
$$

**Proposition (the real reading).** $L_{\tilde B}$ and $R_{\tilde C}$ are real-linear; the assignments $\tilde B\mapsto L_{\tilde B}$ and $\tilde C\mapsto R_{\tilde C}$ are real-linear and injective; and the four composition laws hold:

$$
L_{\tilde B}L_{\tilde C}=L_{\tilde B\tilde C},\qquad R_{\tilde B}R_{\tilde C}=R_{\tilde C\tilde B},\qquad L_{\tilde B}R_{\tilde C}=R_{\tilde C}L_{\tilde B},\qquad L_{\tilde B}R_{\tilde B^{*}}=\Theta_{\tilde B},
$$

where $\Theta_{\tilde B}$ is the two-sided operator below.

*Proof.* Real-linearity is the distributivity of the algebra and the injectivity follows by evaluating at $e_{0}$; the composition laws are associativity and the definition of $\Theta_{\tilde B}$, and they are the complex laws of the companion articles, which hold in particular over $\mathbb{R}$.

**Remark (the one-sided operators over $\mathbb{R}$ and over $\mathbb{C}$).** The two families are the same operators whether the algebra is read over $\mathbb{C}$ or over $\mathbb{R}$; what the real reading adds is the eight-dimensional real domain and the four realified forms, over which the adjoints are computed below. The two-sided operator is the product $L_{\tilde B}R_{\tilde B^{*}}=R_{\tilde B^{*}}L_{\tilde B}$ of one member of each family.

## The Adjoints for the Four Realified Forms

**Theorem (the Euclidean adjoint).** With respect to the realified Hermitian form $\langle\tilde P,\tilde Q\rangle_{*\mathbb{R}}=\mathrm{Re}\sum_\mu P_\mu\overline{Q_\mu}$ of *The Realification of the Four Forms*, the adjoints of the one-sided operators are

$$
(L_{\tilde B})^{*}=L_{\tilde B^{*}},\qquad (R_{\tilde C})^{*}=R_{\tilde C^{*}}.
$$

*Proof.* The identity is the complex adjoint theorem of *One-Sided Operators on the General Plain Sesqualgebra of Biquaternions*, whose proof uses only the anti-involution property of the dagger and the invariance of the scalar part under cyclic permutation; taking real parts preserves it.

**Corollary (the real reading is a faithful real $*$-representation).** The assignment $L:\mathbb{B}\to\mathrm{End}_{\mathbb{R}}(\mathbb{B})$ is an injective real algebra homomorphism, compatible with the dagger and the adjoint, on the real Hilbert space $(\mathbb{B},\langle\cdot,\cdot\rangle_{*\mathbb{R}})$. Since $\mathbb{B}\cong M_{2}(\mathbb{C})$ and $\dim_{\mathbb{R}}\mathbb{B}=8$, it is the left regular representation of a real algebra of dimension eight.

**Theorem (the adjoint of a left multiplication for each realified form).** The four realified forms give the four adjoints

| realified form | adjoint of $L_{\tilde Q}$ |
|---|---|
| general plain bilinear | $R_{\tilde Q}$ (the transpose) |
| general quaternionic bilinear | $L_{\tilde Q^{\natural}}$ |
| Hermitian | $L_{\tilde Q^{*}}$ |
| Krein | $R_{\bar{\tilde Q}}$ |

where ${\natural}$ is the natural conjugation, ${}^{*}$ the Hermitian conjugation and $\bar{\cdot}$ the complex conjugation of the coefficients.

*Proof.* Each identity is the corresponding adjoint of *The Four Pairings of the Biquaternion Algebra*, §*The Forms in Comparison*, read on the real parts, which are the four realified forms of *The Realification of the Four Forms*; the general plain bilinear adjoint is the transpose $F^{\approx}=DF^{\mathsf T}D$ of *Association and the Transpose on the Biquaternion Algebra*, the general quaternionic bilinear adjoint is the natural conjugation on the parameter, the Hermitian adjoint is the dagger, and the Krein adjoint pairs a left multiplication with the right multiplication of the conjugate.

**Remark (the real reading distinguishes the forms through the adjoint).** The four forms are told apart by the adjoint they assign to a single operator and by the side it keeps. The two anti-automorphic conjugations — the natural conjugation ${\natural}$ of the general quaternionic bilinear form and the dagger ${}^{*}$ of the Hermitian form — keep the left multiplication on the left; the general plain bilinear form, whose conjugation is the identity, and the Krein form, whose conjugation is the automorphism of complex conjugation, move it to the right. For the Hermitian form the criterion is the one of §*Self-Adjoint, Skew and Unitary One-Sided Operators*: $L_{\tilde Q}$ is self-adjoint exactly when $\tilde Q\in\mathbb{M}_{+}$. The dichotomy — left for the anti-automorphic conjugations, right for the identity and the automorphism — is the one organising *Association and the Transpose on the Biquaternion Algebra* and *J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra of Biquaternions*.

## The Types of the One-Sided Operators

**Theorem (the type criteria over $\mathbb{R}$).** Let $\tilde B\in\mathbb{B}$. For the realified Hermitian form,

$$
L_{\tilde B}\ \text{self-adjoint}\iff\tilde B\in\mathbb{M}_{+},\qquad
L_{\tilde B}\ \text{skew-adjoint}\iff\tilde B\in\mathbb{M}_{-},
$$

$$
L_{\tilde B}\ \text{unitary}\iff\tilde B\in U=\{\tilde B:\tilde B^{*}\tilde B=e_{0}\}=U(2),
$$

and $L_{\tilde B}$ is invertible if and only if $\tilde B\in\mathbb{B}^{\times}$. The same criteria hold for $R_{\tilde C}$.

*Proof.* By the Euclidean adjoint theorem, $L_{\tilde B}^{*}=L_{\tilde B^{*}}$ and the assignment is injective, so self-adjointness reads $\tilde B^{*}=\tilde B$ and skew-adjointness $\tilde B^{*}=-\tilde B$, which are the definitions of $\mathbb{M}_{+}$ and $\mathbb{M}_{-}$; unitarity reads $L_{\tilde B}^{*}L_{\tilde B}=L_{\tilde B^{*}\tilde B}=\mathrm{id}$, that is $\tilde B^{*}\tilde B=e_{0}$. The criteria are those of the companion articles, whose content is complex, transferred to the realified Hermitian form. The two sectors $\mathbb{M}_{\pm}$ are real four-dimensional subspaces and $U=U(2)$ is a real Lie group of dimension four.

**Corollary (the Lie-theoretic reading).** The image of the slice $U$ under $L$ is a group of unitary operators isomorphic to $U(2)$, and the image of the anti-Hermitian sector $\mathbb{M}_{-}$ is a space of skew-adjoint operators closed under the commutator, the Lie algebra of that group; the exponential stays inside the family, $e^{L_{\tilde B}}=L_{e^{\tilde B}}$ for $\tilde B\in\mathbb{M}_{-}$. This is the Lie algebra $\mathfrak{u}(2)$ acting on the real Hilbert space by skew-adjoint operators.

**Remark (the one-sided and the two-sided types differ, and the real reading shows why).** The parameter of a one-sided operator enters once, so the sector of the parameter is the type of the operator. The parameter of the two-sided operator $\Theta_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{*}}$ enters twice, so both sectors give self-adjoint operators, $\Theta_{\mathbb{M}_{+}}=\Theta_{\mathbb{M}_{-}}$, and no nonzero two-sided operator is skew; the model article proves both statements and the real reading does not alter them. The contrast is the content of the complex pair of articles, and it is quoted here.

## The Real Cartan Decomposition

**Definition (the Cartan involution).** On the group of units let

$$
\theta(\tilde Q)=\bigl(\tilde Q^{*}\bigr)^{-1}.
$$

**Theorem (the Cartan involution and its eigenspaces).** $\theta$ is an automorphism of $\mathbb{B}^{\times}$ of order two, its fixed set is the unitary slice $U=U(2)$, and its differential $\mathrm{d}\theta=-{}^{*}$ is an involution of the real Lie algebra $\mathfrak{gl}(2,\mathbb{C})$ with $+1$ eigenspace the anti-Hermitian sector and $-1$ eigenspace the Hermitian sector:

$$
\mathfrak{gl}(2,\mathbb{C})=\mathbb{M}_{-}\oplus\mathbb{M}_{+}\cong u(2)\oplus H_{2}(\mathbb{C}),\qquad
[\mathbb{M}_{-},\mathbb{M}_{-}]\subseteq\mathbb{M}_{-},\quad
[\mathbb{M}_{-},\mathbb{M}_{+}]\subseteq\mathbb{M}_{+},\quad
[\mathbb{M}_{+},\mathbb{M}_{+}]\subseteq\mathbb{M}_{-}.
$$

*Proof.* The automorphism property, the order two, the fixed set, the differential and the three bracket relations are those of *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint*, §*The Cartan Involution*, quoted and not repeated. In the matrix model $\Phi(\mathbb{M}_{+})=H_{2}(\mathbb{C})$ is the Hermitian and $\Phi(\mathbb{M}_{-})=u(2)$ the skew-Hermitian part, both real four-dimensional, and $\mathfrak{gl}(2,\mathbb{C})=u(2)\oplus H_{2}(\mathbb{C})$ is the decomposition of a matrix into its Hermitian and skew-Hermitian parts.

**Theorem (the group decomposition and the symmetric space).** Every unit has a unique decomposition

$$
\tilde Q=U\,\exp(\tilde H),\qquad U\in U(2),\quad \tilde H\in\mathbb{M}_{+},
$$

so that $\mathbb{B}^{\times}=U(2)\cdot\exp(\mathbb{M}_{+})$, and the quotient $\mathbb{B}^{\times}/U(2)$ is the interior of the Hermitian cone, the positive definite Hermitian elements.

*Proof.* The decomposition is the polar decomposition $\tilde Q=U\lvert\tilde Q\rvert$ with $\lvert\tilde Q\rvert=(\tilde Q^{*}\tilde Q)^{1/2}\in P=\exp(\mathbb{M}_{+})$ and $U\in U(2)$ unique off the null cone, which is *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint*, §*The Polar Decomposition*; the quotient statement is the last corollary of §*The Cartan Involution*.

**Remark (the involution is positive for the realified Hermitian form).** The realified Hermitian form is positive definite and $\theta$-invariant, $\mathrm{Re}\langle\theta\tilde P,\theta\tilde Q\rangle_{*}=\mathrm{Re}\langle\tilde P,\tilde Q\rangle_{*}$, so the involution is the Cartan involution of the real reductive algebra $\mathfrak{gl}(2,\mathbb{C})$ whose associated positive form is the realified Hermitian form of *The Realification of the Four Forms*. In the semisimple theory the positive form is $\kappa_{\theta}(x,y)=-\kappa(x,\theta y)$; here the Killing form is degenerate on the centre and the positive form that plays the role is the realified Hermitian form. The general theory of the involution, the decomposition and the symmetric pair is *The Cartan Involution and the Cartan Decomposition*, *Symmetric Spaces* and *Real Forms of a Complex Lie Group and the Cartan Involution*.

## The Three Real Groups

The realified forms single out three real groups, and each acts on the space of the operators.

**Theorem (the unitary group $U(2)$).** The unitary slice $U=U(2)$ is the fixed group of the Cartan involution and the maximal compact subgroup of the unit group $\mathbb{B}^{\times}\cong GL_{2}(\mathbb{C})$; it is a compact connected real Lie group of dimension four, and its Lie algebra is the anti-Hermitian sector $\mathbb{M}_{-}=u(2)$, acting on $\mathbb{B}$ by skew-adjoint operators.

*Proof.* The fixed set and the maximality are the Cartan theorems above and of *The Unitary Group and the Hermitian Symmetric Space* and *The Biquaternion Unit Group as a Topological Group*.

**Theorem (the orthogonal groups $O(4)$ and $O(1,3)$).** On the quaternion subspace $\mathbb{H}_{\mathbb{B}}$ and the Hermitian subspace $\mathbb{M}_{+}$, both real four-dimensional, the realified forms restrict to forms whose automorphism groups are

| subspace | form | restriction | automorphism group |
|---|---|---|---|
| $\mathbb{H}_{\mathbb{B}}$ | general quaternionic bilinear | $(4,0)$ | $O(4)$ |
| $\mathbb{M}_{+}$ | general plain bilinear | $(4,0)$ | $O(4)$ |
| $\mathbb{H}_{\mathbb{B}}$ | general plain bilinear | $(1,3)$ | $O(1,3)$ |
| $\mathbb{M}_{+}$ | Krein | $(1,3)$ | $O(1,3)$ |

*Proof.* The restrictions are the rows of *The Realification of the Four Forms*, §*Remarkable Subspaces under the Four Realified Forms*; the group of real-linear automorphisms of a non-degenerate real form of signature $(p,q)$ on a space of dimension $n=p+q$ is $O(p,q)$, whence $O(4)$ for the definite rows and $O(1,3)$ for the interval rows.

**Remark (the real forms of the model entry point, read on the operators).** The groups $O(4)$ and $O(1,3)$ are the two real forms of the complex orthogonal group $O_{4}(\mathbb{C})$ of *The General Plain Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*, §*The General Plain Bilinear Form in the Representation*, exhibited by the Hermitian subspace and the quaternion subspace respectively; the unitary group $U(2)$ is the form of the operator algebra singled out by the dagger. The three real groups, $O(4)$, $U(2)$ and $O(1,3)$, are the orthogonal and unitary groups of the real reading, of real dimensions $6$, $4$ and $6$. The indefinite operators of the Krein form, with the $J$-adjoint, are *The Krein Isometry Group and Its $J$-Contractions*, and the operator-theoretic Cartan decomposition of the Krein form is *The Krein Cartan Decomposition of the Operator Algebra*.

## Worked Examples

**The vector generators.** For $\tilde B=e_{k}$, $k=1,2,3$, one has $e_{k}^{*}=-e_{k}$ and $e_{k}^{2}=-e_{0}$, so $L_{e_{k}}$ is skew-adjoint and $L_{e_{k}}^{2}=-L_{e_{0}}=-\mathrm{id}$: the left multiplication by a vector generator is a complex structure on the real algebra, of square minus the identity, and the three operators anticommute, as the Clifford relations of the algebra require.

**A parameter in neither sector.** For $\tilde B=e_{1}+ie_{2}$ the Hermitian part is $ie_{2}\in\mathbb{M}_{+}$ and the anti-Hermitian part is $e_{1}\in\mathbb{M}_{-}$, so $L_{\tilde B}=L_{ie_{2}}+L_{e_{1}}$ splits into a self-adjoint and a skew-adjoint part and is of neither type. The example records that the type is decided by the parameter and the sector it lies in.

**The two-sided operator forgets the sector.** For $\tilde Q\in\mathbb{M}_{-}$ one has $\tilde Q^{*}=-\tilde Q$ and $\Theta_{\tilde Q}=\Theta_{-\tilde Q}=\Theta_{\tilde Q^{*}}$, so the operator is self-adjoint although its parameter is anti-Hermitian; the real reading reproduces the trap of the model article, and no real-linear structure alters it.

**A Cartan decomposition.** For the unit $\tilde Q=(\cosh t)e_{0}+(\sinh t)e_{1}$ of the quaternion subspace one has $\tilde Q^{*}=\tilde Q^{\natural}=(\cosh t)e_{0}-(\sinh t)e_{1}$, and the polar decomposition writes $\tilde Q=U\exp(\tilde H)$ with $U\in U(2)$ and $\tilde H\in\mathbb{M}_{+}$; the factor $\exp(\tilde H)$ is positive definite Hermitian and the quotient is the interior of the Hermitian cone.

**A unitary parameter.** For the central phase $\tilde B=e^{i\theta}e_{0}$ one has $\tilde B^{*}=e^{-i\theta}e_{0}$ and $\tilde B^{*}\tilde B=e_{0}$, so $L_{\tilde B}$ is unitary for every $\theta$. The phase is Hermitian only for $e^{i\theta}=\pm1$ and anti-Hermitian only for $e^{i\theta}=\pm i$, so away from those four points the unitary operator is of neither symmetric type: the central circle $S^{1}e_{0}$ lies in $U=U(2)$ and meets the two sectors exactly in those four points.

## Summary

The operators of the real biquaternion algebra are the left and right multiplications $L_{\tilde B}(\tilde V)=\tilde B\tilde V$ and $R_{\tilde C}(\tilde V)=\tilde V\tilde C$, with the two-sided sandwich $\Theta_{\tilde B}=L_{\tilde B}R_{\tilde B^{*}}$ as their product; they are real endomorphisms of $\mathbb{B}\cong\mathbb{R}^{8}$, and the complex operator theorems of the companion articles hold over $\mathbb{R}$ unchanged. The four realified forms assign four different adjoints to the left multiplication — the transpose $R_{\tilde Q}$ for the general plain bilinear form, $L_{\tilde Q^{\natural}}$ for the general quaternionic bilinear form, $L_{\tilde Q^{*}}$ for the Hermitian form and $R_{\bar{\tilde Q}}$ for the Krein form — and for the realified Hermitian form the type criteria are the ones of the involution lattice: $L_{\tilde B}$ is self-adjoint exactly on the Hermitian sector $\mathbb{M}_{+}$, skew-adjoint exactly on the anti-Hermitian sector $\mathbb{M}_{-}$, and unitary exactly on the slice $U=U(2)$. The dagger defines the Cartan involution $\theta(\tilde Q)=(\tilde Q^{*})^{-1}$ of the unit group, of order two, with fixed set $U(2)$ and differential $-{}^{*}$, and its eigenspaces give the real Cartan decomposition $\mathfrak{gl}(2,\mathbb{C})=u(2)\oplus H_{2}(\mathbb{C})$ with the bracket relations of a $\mathbb{Z}/2$-graded Lie algebra and the group decomposition $\mathbb{B}^{\times}=U(2)\cdot\exp(\mathbb{M}_{+})$, whose quotient is the interior of the Hermitian cone. The three real groups that the realified forms single out are the compact $U(2)$, of dimension four; and the orthogonal groups $O(4)$ and $O(1,3)$, of dimension six, read as the automorphism groups of the definite and the interval restrictions of the two indefinite forms on the quaternion and Hermitian subspaces.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_{\tilde B}(\tilde V)=\tilde B\tilde V$, $R_{\tilde C}(\tilde V)=\tilde V\tilde C$ | the one-sided operators; real-linear and injective in the parameter |
| $\Theta_{\tilde B}=L_{\tilde B}R_{\tilde B^{*}}=R_{\tilde B^{*}}L_{\tilde B}$ | the two-sided operator, the product of the two families |
| $L_{\tilde B}L_{\tilde C}=L_{\tilde B\tilde C}$, $R_{\tilde B}R_{\tilde C}=R_{\tilde C\tilde B}$, $L_{\tilde B}R_{\tilde C}=R_{\tilde C}L_{\tilde B}$ | the composition laws |
| $(L_{\tilde B})^{*}=L_{\tilde B^{*}}$, $(R_{\tilde C})^{*}=R_{\tilde C^{*}}$ | the adjoints for the realified Hermitian form |
| $R_{\tilde Q}$, $L_{\tilde Q^{\natural}}$, $L_{\tilde Q^{*}}$, $R_{\bar{\tilde Q}}$ | the four adjoints, for the general plain bilinear, general quaternionic bilinear, Hermitian and Krein forms |
| $\mathbb{M}_{+}=H_{2}(\mathbb{C})$, $\mathbb{M}_{-}=u(2)$ | the Hermitian and anti-Hermitian sectors; self-adjoint and skew-adjoint parameters |
| $U=\{\tilde Q^{*}\tilde Q=e_{0}\}=U(2)$ | the unitary slice; the fixed group of the Cartan involution |
| $\theta(\tilde Q)=(\tilde Q^{*})^{-1}$, $\mathrm{d}\theta=-{}^{*}$ | the Cartan involution and its differential |
| $\mathfrak{gl}(2,\mathbb{C})=u(2)\oplus H_{2}(\mathbb{C})$ | the Cartan decomposition of the operator algebra |
| $\mathbb{B}^{\times}=U(2)\cdot\exp(\mathbb{M}_{+})$ | the group decomposition; quotient the interior of the Hermitian cone |
| $O(4)$, $U(2)$, $O(1,3)$ | the three real groups of the realified forms |

## Further Reading

- *One-Sided Operators on the General Plain Sesqualgebra of Biquaternions* (`articles_maths/one-sided-operators-on-the-general-plain-sesqualgebra-of-biquaternions.md`), for the one-sided composition laws, adjoints and types over $\mathbb{C}$
- *Two-Sided Operators on the General Plain Sesqualgebra of Biquaternions* (`articles_maths/two-sided-operators-on-the-general-plain-sesqualgebra-of-biquaternions.md`), for the sandwich, its quadratics and the type theorems
- *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint* (`articles_maths/positivity-and-the-hermitian-cone-of-the-biquaternion-algebra-with-hermitian-adjoint.md`), for the polar decomposition and the Cartan involution quoted here
- *The Realification of the Four Forms* (`articles_maths/the-realification-of-the-four-forms.md`), for the four realified forms, their restrictions and their signatures
- *The Trace Form of the Real Biquaternion Algebra* (`articles_maths/the-trace-form-of-the-real-biquaternion-algebra.md`), for the companion invariant form built from the regular representation
- *The Four Pairings of the Biquaternion Algebra* (`articles_maths/the-four-pairings-of-the-biquaternion-algebra.md`) and *Association and the Transpose on the Biquaternion Algebra* (`articles_maths/association-and-the-transpose-on-the-biquaternion-algebra.md`), for the four adjoints of a left multiplication
- *The Cartan Involution and the Cartan Decomposition* (`articles_maths/the-cartan-involution-and-the-cartan-decomposition.md`) and *Symmetric Spaces* (`articles_maths/symmetric-spaces.md`), for the general involution, the Cartan decomposition and the symmetric pair
- *Real Forms of a Complex Lie Group and the Cartan Involution* (`articles_maths/real-forms-of-a-complex-lie-group-and-the-cartan-involution.md`), for the real forms and their involutions
- *One-Sided Operators on a Clifford Algebra* (`articles_maths/one-sided-operators-on-a-clifford-algebra.md`) and *Two-Sided Operators on a Clifford Algebra* (`articles_maths/two-sided-operators-on-a-clifford-algebra.md`), for the general operator theories whose instance this article is
- *The Unitary Group and the Hermitian Symmetric Space* (`articles_maths/the-unitary-group-and-the-hermitian-symmetric-space.md`), for $U(2)$ and the symmetric space of the decomposition
- *The Krein Isometry Group and Its J-Contractions* (`articles_maths/the-krein-isometry-group-and-its-j-contractions.md`), for the indefinite operators of the Krein form
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the group of units and the invertibility criterion
- Sigurdur Helgason, *Differential Geometry, Lie Groups and Symmetric Spaces*, Graduate Studies in Mathematics 34 (American Mathematical Society, 2001), for the Cartan involution, the Cartan decomposition and the symmetric space.
- Anthony W. Knapp, *Lie Groups Beyond an Introduction*, Progress in Mathematics 140 (Birkhäuser, 2nd ed. 2002), for the maximal compact subgroups and the group decomposition of a reductive group.
