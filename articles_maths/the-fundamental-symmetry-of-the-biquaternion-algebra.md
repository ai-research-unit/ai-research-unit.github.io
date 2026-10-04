# __The Fundamental Symmetry of the Biquaternion Algebra__

## Introduction

An indefinite inner product is a definite one together with an involution $J$ of square one, self-adjoint for the indefinite form, such that $[\tilde{Q},\tilde{Q}']=\langle J\tilde{Q},\tilde{Q}'\rangle$ and $\langle \tilde{Q},\tilde{Q}\rangle=[J\tilde{Q},\tilde{Q}]>0$ off zero: the **fundamental symmetry** (*The Fundamental Symmetry*). For the Krein form of the biquaternion algebra that involution is already at hand in the Algebra layer: it is the **natural conjugation** ${}^{\natural}$, which negates the vector units and fixes the centre. The bridge identity is

$$
[\tilde{Q},\tilde{Q}']=\langle\tilde{Q}^{\natural},\tilde{Q}'\rangle,
$$

with $\langle\cdot,\cdot\rangle$ the positive definite Hermitian inner product of the dagger form. This article fixes that symmetry, its eigenspaces — the centre and the vector subspace — the parametrisation of all the other fundamental symmetries by the open unit ball of the vector subspace, and the fact that ${}^{\natural}$ is the only fundamental symmetry that respects the algebra as an anti-automorphism.

The general theory is *The Fundamental Symmetry*, *Krein Spaces* and *Indefinite Inner Product Spaces*; the operators that ${}^{\natural}$ makes available are *J-Self-Adjoint and J-Unitary Operators on the Biquaternion Algebra*; the form is *The Biquaternion Krein Form and Its Signature*; the positive definite form of the bridge is *The Hermitian Form on the Biquaternion Algebra*; and the four involutions whose lattice ${}^{\natural}$ belongs to are *Biquaternion Involution Lattice* and *Biquaternion Relations Between Subspaces*.

**Conventions.** As in the companion articles: $\tilde{Q}=\sum_\mu Q_\mu e_\mu$, $N(\tilde{Q})=\sum_\mu Q_\mu^{2}$, $\|\tilde{Q}\|_E=(\sum_\mu|Q_\mu|^{2})^{1/2}$, dagger ${}^{*}={}^{\natural}\circ\bar{\cdot}$, Krein form $[\tilde{Q},\tilde{Q}']=\mathrm{Sc}(\tilde{Q}^{\natural*}\tilde{Q}')$, and $\Phi:\mathbb{B}\to M_2(\mathbb{C})$ the matrix model, which carries ${}^{\natural}$ to the adjugate, $\Phi(\tilde{Q}^{\natural})=\mathrm{adj}\,\Phi(\tilde{Q})$ (*The Forms in the Matrix Representation of the Biquaternion Algebra*).

## The Natural Conjugation as a Fundamental Symmetry

**Theorem.** The natural conjugation $J:= {}^{\natural}$ is a fundamental symmetry of the Krein form:

$$
J^{2}=\mathrm{id},\qquad [J\tilde{Q},\tilde{Q}']=[\tilde{Q},J\tilde{Q}'],\qquad [J\tilde{Q},\tilde{Q}]=\|\tilde{Q}\|_E^{2}>0\ (\tilde{Q}\neq0),
$$

and the definite form it induces is the Hermitian inner product,

$$
[\tilde{Q},\tilde{Q}']=\langle J\tilde{Q},\tilde{Q}'\rangle=\langle\tilde{Q}^{\natural},\tilde{Q}'\rangle .
$$

**Proof.** $J$ is $\mathbb{C}$-linear and an involution because it multiplies each coefficient $Q_\mu$ by the real sign $\varepsilon_\mu$. For the self-adjointness, $[J\tilde{Q},\tilde{Q}']=\langle J^{2}\tilde{Q},\tilde{Q}'\rangle=\langle\tilde{Q},\tilde{Q}'\rangle$ and $[\tilde{Q},J\tilde{Q}']=\langle J\tilde{Q},J\tilde{Q}'\rangle=\sum_\mu\varepsilon_\mu^{2}Q_\mu^{*}Q'_\mu=\langle\tilde{Q},\tilde{Q}'\rangle$, using $(J\tilde{Q})_\mu=\varepsilon_\mu Q_\mu$; the two agree. For positivity, $[J\tilde{Q},\tilde{Q}]=\sum_\mu\varepsilon_\mu^{2}|Q_\mu|^{2}=\sum_\mu|Q_\mu|^{2}=\|\tilde{Q}\|_E^{2}$, which is positive off zero. The bridge identity is the first of the two computations.

**Corollary ($J$ is an isometry of both forms).** $J$ preserves the Krein form and the Hermitian form,

$$
[J\tilde{Q},J\tilde{Q}']=[\tilde{Q},\tilde{Q}'],\qquad \langle J\tilde{Q},J\tilde{Q}'\rangle=\langle\tilde{Q},\tilde{Q}'\rangle,
$$

and it is orthogonal for the Euclidean structure, $\|J\tilde{Q}\|_E=\|\tilde{Q}\|_E$.

**Proof.** Both forms are built from $|Q_\mu|^{2}$ and from the off-diagonal coefficient pairings; $J$ permutes the coefficients among themselves up to the real signs $\varepsilon_\mu$, and $\varepsilon_\mu^{2}=1$ removes them from every diagonal expression, while the off-diagonal pairing is unchanged because the same sign multiplies both factors. Orthogonality is the third identity of the theorem.

## The Eigenspaces and the Fundamental Decomposition

**Theorem (the decomposition is the $\natural$-splitting).** The eigenspaces of $J$ are

$$
\mathbb{B}_{+}=\ker(J-\mathrm{id})=\mathbb{C}_{\mathbb{B}}=\mathrm{span}_{\mathbb{C}}\{e_0\},\qquad
\mathbb{B}_{-}=\ker(J+\mathrm{id})=\mathbb{V}_{\mathbb{B}}=\{Q_0=0\},
$$

the **centre** and the **vector subspace**; they are the positive and the negative definite parts of the fundamental decomposition

$$
\mathbb{B}=\mathbb{C}_{\mathbb{B}}\oplus\mathbb{V}_{\mathbb{B}},\qquad \mathbb{C}_{\mathbb{B}}\perp\mathbb{V}_{\mathbb{B}},
$$

of complex dimensions $(1,3)$ and real dimensions $(2,6)$, in agreement with the signature of *The Biquaternion Krein Form and Its Signature*.

**Proof.** An element is fixed by $J$ exactly when its vector coefficients vanish, i.e. when it lies in the centre, and it is negated exactly when its scalar coefficient vanishes; $J^{2}=\mathrm{id}$ gives the direct sum, and orthogonality is the sign computation of the Krein form. The dimensions are read from the coefficients.

**Corollary (the fundamental decomposition is Algebra data).** The fundamental decomposition of the Krein space is exactly the eigenspace splitting of one of the four involutions of the algebra; the six distinguished subspaces and their dimensions determine it, and it needs no choice. The centre is the positive part and the vector subspace the negative part, and the two real slices $\mathbb{B}_{\mathbb{R}},\ i\mathbb{B}_{\mathbb{R}}$ of signature $(1,3)$ cut across it.

**Proof.** The statement is the theorem together with the identification of the fixed and anti-fixed spaces of ${}^{\natural}$ in *Biquaternion Relations Between Subspaces*.

## The Natural Conjugation as an Anti-Automorphism

**Proposition.** ${}^{\natural}$ is a $\mathbb{C}$-linear algebra **anti-automorphism** of order two: ${}^{\natural}(e_0)=e_0$ and

$$
(\tilde{Q}\tilde{R})^{\natural}=\tilde{R}^{\natural}\tilde{Q}^{\natural}.
$$

It commutes with the complex conjugation and with the dagger, ${}^{\natural}\bar{\cdot}=\bar{\cdot}\,{}^{\natural}$ and ${}^{\natural}{}^{*}={}^{*}{}^{\natural}$, and on the left and right multiplications it exchanges the sides,

$$
{}^{\natural}\,L_{\tilde{Q}}\,{}^{\natural}=R_{\tilde{Q}^{\natural}},\qquad
{}^{\natural}\,R_{\tilde{R}}\,{}^{\natural}=L_{\tilde{R}^{\natural}}.
$$

**Proof.** ${}^{\natural}$ is quaternion conjugation on the coefficients, and quaternion conjugation reverses products; on the units, $e_k^{\natural}=-e_k$ and $(-e_k)(-e_l)=e_ke_l=-(e_le_k)$ for $k\neq l$. The commutation with $\bar{\cdot}$ is that $i$ is fixed and $\bar{\cdot}$ acts on the coefficients, and ${}^{*}={}^{\natural}\circ\bar{\cdot}$ commutes with ${}^{\natural}$ because $\bar{\cdot}$ does and ${}^{\natural}{}^{2}=\mathrm{id}$. For the last identities, $\left({}^{\natural}L_{\tilde{Q}}{}^{\natural}\right)(\tilde{P})={}^{\natural}(\tilde{Q}\,\tilde{P}^{\natural})=\tilde{P}\,\tilde{Q}^{\natural}=R_{\tilde{Q}^{\natural}}\tilde{P}$, using the anti-automorphism; the second is the same computation.

**Remark (the matrix picture).** Under $\Phi$ the natural conjugation is the adjugate: $\Phi(\tilde{Q}^{\natural})=\mathrm{adj}\,\Phi(\tilde{Q})=\varepsilon\,\Phi(\tilde{Q})^{\mathsf T}\varepsilon^{-1}$ with $\varepsilon=i\sigma_2$, and the anti-automorphism property is the classical identity $\mathrm{adj}(MN)=\mathrm{adj}(N)\mathrm{adj}(M)$. The fundamental symmetry is therefore the linear operator $X\mapsto\mathrm{adj}X=\varepsilon X^{\mathsf T}\varepsilon^{-1}$ on $M_2(\mathbb{C})$.

## The Uniqueness of the Symmetry, and the Others

The fundamental symmetries of an indefinite inner product are not unique when both ranks are nonzero (*The Fundamental Symmetry*, §*Non-Uniqueness and the Angular Operator*). For the biquaternion Krein form the whole family is parametrised by the vector subspace.

**Theorem (the family of fundamental symmetries).** The fundamental symmetries of the Krein form are exactly the involutions $J_{\tilde V}$ that act as $+\mathrm{id}$ on the positive definite complex line

$$
\ell_{\tilde V}=\mathbb{C}\cdot(e_0+\tilde V),\qquad \tilde V\in\mathbb{V}_{\mathbb{B}},\ \|\tilde V\|_E<1,
$$

and as $-\mathrm{id}$ on its Krein-orthogonal complement. The parametrisation $\tilde V\mapsto\ell_{\tilde V}$ is a bijection onto the open unit ball of $\mathbb{V}_{\mathbb{B}}$:

$$
\{\text{fundamental symmetries}\}\longleftrightarrow\{\tilde V\in\mathbb{V}_{\mathbb{B}}:\|\tilde V\|_E<1\}\cong\{T:\mathbb{C}_{\mathbb{B}}\to\mathbb{V}_{\mathbb{B}},\ \|T\|<1\}.
$$

**Proof.** By the general parametrisation, the fundamental symmetries correspond to the maximal positive definite subspaces, and a maximal positive definite subspace of this Krein space has complex dimension one because the positive index is one; each such line is the graph of a $\mathbb{C}$-linear map $T:\mathbb{C}_{\mathbb{B}}\to\mathbb{V}_{\mathbb{B}}$, that is, is generated by $e_0+\tilde V$ with $\tilde V=T(e_0)$; and it is positive definite exactly when $\|T\|<1$, which is $\|\tilde V\|_E<1$ because $\|e_0\|_E=1$. Distinct $\tilde V$ give distinct lines and distinct symmetries.

**Theorem ($\natural$ is the only one that respects the algebra).** The natural conjugation ${}^{\natural}=J_0$ is the unique fundamental symmetry of the Krein form that is a $\mathbb{C}$-algebra anti-automorphism, equivalently the unique one that fixes the identity and satisfies $J(\tilde{Q}\tilde{R})=J(\tilde{R})J(\tilde{Q})$. In the parametrisation above it is the member $\tilde V=0$.

**Proof.** Let $J$ be a fundamental symmetry and a unital $\mathbb{C}$-algebra anti-automorphism. The $+1$-eigenspace $W$ of $J$ is a complex subspace of complex dimension one (the positive index), and it contains $e_0$, because a unital anti-automorphism of a bijective-involution type satisfies $J(e_0)=J(e_0^{2})=J(e_0)^{2}$ with $J$ bijective, whence $J(e_0)=e_0$. A one-dimensional complex subspace containing $e_0$ is $\mathbb{C}_{\mathbb{B}}$, so $W=\mathbb{C}_{\mathbb{B}}$, and then $J$ is $+\mathrm{id}$ on the centre and $-\mathrm{id}$ on the vector subspace, which is ${}^{\natural}$. Conversely ${}^{\natural}$ is such a symmetry by the two preceding sections.

**Corollary (the tilted symmetries are not algebraic).** For $\tilde V\neq0$ the symmetry $J_{\tilde V}$ fixes no algebra structure: it does not preserve the multiplication, and it does not even fix $e_0$, since $e_0\notin\ell_{\tilde V}$.

**Proof.** $e_0\in\ell_{\tilde V}$ would force $\tilde V\in\mathbb{V}_{\mathbb{B}}\cap\mathbb{C}_{\mathbb{B}}=0$.

## The Indefinite Adjoint and the Order

**Definition.** For a $\mathbb{C}$-linear operator $T$ on $\mathbb{B}$ the **$J$-adjoint** is $T^{\dagger}=J\,T^{*}J$, where $T^{*}$ is the adjoint for the Hermitian form; it is the unique operator with $[T\tilde{Q},\tilde{Q}']=[\tilde{Q},T^{\dagger}\tilde{Q}']$ (*J-Self-Adjoint and J-Unitary Operators*).

**Proposition (the dictionary).** The indefinite theory is the definite theory conjugated by $J$:

| Indefinite notion for $[\cdot,\cdot]$ | Definite notion for $\langle\cdot,\cdot\rangle$ |
|---|---|
| $T$ is $J$-self-adjoint, $T^{\dagger}=T$ | $JT$ is self-adjoint |
| $T$ is $J$-unitary, $T^{\dagger}T=TT^{\dagger}=1$ | $JTJ$ is unitary |
| $T$ is $J$-positive, $[T\tilde{Q},\tilde{Q}]\geq0$ | $JT$ is positive |
| the eigenspaces $\mathbb{C}_{\mathbb{B}},\mathbb{V}_{\mathbb{B}}$ | the $\pm1$-eigenspaces of $J$ |

**Proof.** Each line is the substitution $[\tilde{Q},\tilde{Q}']=\langle J\tilde{Q},\tilde{Q}'\rangle$ with $J^{2}=\mathrm{id}$; for the second, $T^{\dagger}T=1\iff JT^{*}JT=1\iff T^{*}JT=J\iff (JTJ)^{*}(JTJ)=1$.

**Corollary.** The $J$-positive cone contains $J$ itself, $[J\tilde{Q},\tilde{Q}]=\|\tilde{Q}\|_E^{2}\geq0$, while $J$ is not positive for the Hermitian form, its spectrum being $\{+1,-1\}$ with multiplicities $(2,6)$. So positive definiteness in the indefinite sense is a genuinely weaker notion, and the asymmetry is exactly the sign change of ${}^{\natural}$ on the vector subspace.

**Proof.** The first statement is the theorem; the spectrum of $J$ is the list of its eigenvalues with the dimension of the eigenspaces of the previous section.

## Worked Examples

**The canonical symmetry.** $J_0={}^{\natural}$: positive part $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$, negative part $\mathbb{V}_{\mathbb{B}}$.

**A tilted symmetry.** $\tilde V=\tfrac12e_1$. The line $\ell=\mathbb{C}(e_0+\tfrac12e_1)$ is positive definite, $[e_0+\tfrac12e_1,e_0+\tfrac12e_1]=1-\tfrac14=\tfrac34>0$, so $J_{\tilde V}$ is a fundamental symmetry; it does not fix $e_0$, and it is not an anti-automorphism.

**The boundary.** $\tilde V=e_1$: $[e_0+e_1,e_0+e_1]=0$, the line is totally isotropic, so $\|\tilde V\|_E<1$ is optimal and the open ball is exactly the set of admissible parameters.

**A non-admissible parameter.** $\tilde V=2e_1$: $[e_0+2e_1,e_0+2e_1]=1-4<0$, the line is negative, and no fundamental symmetry with that positive part exists.

## Summary

The **fundamental symmetry** of the biquaternion Krein form is the natural conjugation $J={}^{\natural}$: a $\mathbb{C}$-linear involution, self-adjoint for $[\cdot,\cdot]$, positive on $e_0$-lines, with the bridge $[\tilde{Q},\tilde{Q}']=\langle\tilde{Q}^{\natural},\tilde{Q}'\rangle$. Its eigenspaces are the centre (positive, complex dimension one) and the vector subspace (negative, complex dimension three), so the fundamental decomposition of the Krein space is precisely the eigenspace splitting of one of the algebra's four involutions. ${}^{\natural}$ is a $\mathbb{C}$-algebra anti-automorphism (quaternion conjugation, the adjugate in the matrix model) and commutes with the complex conjugation and the dagger; it exchanges left and right multiplications. All the other fundamental symmetries are the involutions with positive part a positive definite line $\mathbb{C}(e_0+\tilde V)$, $\|\tilde V\|_E<1$, a family parametrised by the open unit ball of the vector subspace; among them ${}^{\natural}$ is the unique one that is an anti-automorphism, equivalently the unique one fixing $e_0$. The $J$-adjoint $T^{\dagger}=JT^{*}J$ makes the indefinite operator theory the definite theory conjugated by $J$, and the $J$-positive cone contains $J$ itself.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $J={}^{\natural}$ | Fundamental symmetry; negates the vector units |
| $[\tilde{Q},\tilde{Q}']=\langle J\tilde{Q},\tilde{Q}'\rangle$ | The bridge to the Hermitian form |
| $\mathbb{B}_{+}=\mathbb{C}_{\mathbb{B}}$, $\mathbb{B}_{-}=\mathbb{V}_{\mathbb{B}}$ | The $\pm1$-eigenspaces; centre and vector subspace |
| $(\tilde{Q}\tilde{R})^{\natural}=\tilde{R}^{\natural}\tilde{Q}^{\natural}$ | Anti-automorphism property |
| ${}^{\natural}L_{\tilde{Q}}{}^{\natural}=R_{\tilde{Q}^{\natural}}$ | Exchange of the sides |
| $\ell_{\tilde V}=\mathbb{C}(e_0+\tilde V)$, $\|\tilde V\|_E<1$ | General fundamental symmetry |
| $T^{\dagger}=JT^{*}J$ | The $J$-adjoint |
| $\{+1,-1\}$, multiplicities $(2,6)$ | The spectrum of $J$ |

## Further Reading

- *The Fundamental Symmetry* (`articles_maths/the-fundamental-symmetry.md`), for the general theory and the angular operator
- *The Biquaternion Krein Form and Its Signature* (`articles_maths/the-biquaternion-krein-form-and-its-signature.md`), for the form whose symmetry this is
- *J-Self-Adjoint and J-Unitary Operators on the Biquaternion Algebra* (`articles_maths/j-self-adjoint-and-j-unitary-operators-on-the-biquaternion-algebra.md`), for the operators the symmetry defines
- *Biquaternion Involution Lattice* (`articles_maths/biquaternion-involution-lattice.md`) and *Biquaternion Relations Between Subspaces* (`articles_maths/biquaternion-relations-between-subspaces.md`), for the involutions and their fixed spaces
- *Introduction to the Six Subspaces* (`articles_maths/introduction-to-the-six-subspaces.md`), for the two eigenspaces, the centre and the vector subspace, as algebras
- János Bognár, *Indefinite Inner Product Spaces* (Springer, 1974), for the fundamental symmetry and the parametrisation of the fundamental decompositions
