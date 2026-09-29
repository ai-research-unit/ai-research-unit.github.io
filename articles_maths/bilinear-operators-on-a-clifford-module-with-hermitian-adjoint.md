
# __Bilinear Operators on a Clifford Module with Hermitian Adjoint__

## Introduction

A bilinear operator on a Clifford module is an operator built from two spinors rather than one. The space of such operators is finite-dimensional, and its structure is dictated by two facts: the Hermitian form of the module fixes the adjoint of every operator, and the Clifford algebra, acting on the module, generates **all** the endomorphisms of the module when the module is irreducible over a simple algebra. The second fact is the **completeness** of the Clifford action, and its bilinear reading is the classical **Fierz identity**: the bilinear covariants $(s,\Gamma^{A}t)$, indexed by a basis of the Clifford algebra, span the space of bilinear forms on a spinor module, and every endomorphism is a Clifford-linear combination of the covariant operators.

This article sets up the bilinear operators — the forms $S\times S\to A$, the equivariant ones, and the maps $S\to S$ they induce — and proves the completeness identity with the adjoint structure carried along: the adjoint of the operator $\Gamma^{A}$ is the operator $\Gamma^{A\dagger}$, the covariant form $(s,\Gamma^{A}t)$ has an adjoint covariant, and the types of the covariants are read off from the dagger. The two worked cases are the complex two-dimensional module, where the four blades are the four matrix units of $\mathrm{End}(\mathbb{C}^{2})$ and the Fierz identity is the completeness of a basis, and the quaternion algebra, where the invariants are the quaternion units.

The Clifford action and the module form are *Hermitian Clifford Modules with Hermitian Adjoint*; the adjoint of the action is *The Adjoint of the One-Sided Action with Hermitian Adjoint*; the spinor adjoint and the Dirac adjoint are *Spinor Adjoints and the Dirac Adjoint with Hermitian Adjoint*; the forms of the dagger are *Hermitian Forms on a Clifford Algebra with Hermitian Adjoint*; the classification of the invariant forms is *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint*; the trace form and the adjoint of multiplication are *The Blade Form and the Hilbert Structure with Hermitian Adjoint*; the completely positive maps and the operator systems are *Completely Positive Maps of a Clifford Algebra with Hermitian Adjoint*; and the spinor module and its idempotents are *Spinors as Minimal Left Ideals with Inner Conjugation*.

## Bilinear Forms and Bilinear Operators

### Definitions

**Definition.** Let $S$ be a Clifford module over $A$. A **bilinear form** on $S$ is a map $b : S\times S\to A$ that is $A$-linear in each argument; it is **Hermitian** if $b(t,s) = \sigma(b(s,t))$, and the **adjoint form** $b^{*}$ is defined by $b^{*}(s,t) = \sigma(b(t,s))$, so that $b$ is Hermitian exactly when $b^{*} = b$. A **bilinear operator** is the $A$-linear map $S\to S^{*}$, $s\mapsto b(s,\cdot)$, induced by a bilinear form; the two descriptions carry the same data, by the adjunction $\mathrm{Bil}_A(S,S;A)\cong \mathrm{Hom}_A(S,S^{*})$.

**Definition.** A bilinear form $b$ is **Clifford-equivariant** (or **invariant**) if

$$
b(x\cdot s, t) = b\bigl(s, x^{\dagger}\cdot t\bigr) \qquad \text{for all } x \in \mathrm{Cl}(V,q),
$$

which is the adjointness condition of *Hermitian Clifford Modules with Hermitian Adjoint*. So a Hermitian Clifford module is exactly a Clifford module with a Hermitian equivariant bilinear form, and the **spinor adjoint** $J$ of *Spinor Adjoints and the Dirac Adjoint with Hermitian Adjoint* is the bilinear operator of that form.

**Remark (the two-sided action on the forms).** The space $\mathrm{Bil}_A(S,S;A)$ carries the action of the operator algebra: for $T\in \mathrm{End}_A(S)$ the form $b\circ(T\times T)$ is again bilinear, and the equivariant forms are the fixed points of the subspace of operators of the form $\rho(x)\otimes\rho(x^{\dagger}) - \mathrm{id}$. This is the module-level form of the two-sided operators of *Two-Sided Operators on a Clifford Algebra*.

### The Adjoint of a Bilinear Operator

**Proposition.** With respect to the module form $(\cdot,\cdot)$ and the induced adjoint on $\mathrm{End}_A(S)$, the adjoint of the bilinear operator $T_b : s\mapsto b(s,\cdot)$ is $T_{b^{*}}$, where $b^{*}(s,t) = \sigma(b(t,s))$; equivalently, the assignment $b\mapsto T_b$ commutes with the adjoint:

$$
(T_b)^{*} = T_{b^{*}} .
$$

**Proof.** $\langle T_bs, t\rangle = b(s,t)$ and $\langle s, T_{b^{*}}t\rangle = b^{*}(t,s) = \sigma(b(s,t))$; comparing with the defining property $\langle T_bs,t\rangle = \sigma(\langle s, T_b^{*}t\rangle)$ of the adjoint under the sesquilinear convention gives the identity.

**Corollary.** A bilinear form is Hermitian iff its bilinear operator is self-adjoint; a form is alternating iff its operator is skew-adjoint; and the Hermitian forms are the fixed points of the involution $b\mapsto b^{*}$ on $\mathrm{Bil}_A(S,S;A)$, so the Hermitian forms form the symmetric part of the space of bilinear forms under this involution.

## The Completeness of the Clifford Action

### The Theorem

**Theorem (completeness, the Fierz identity).** Let $V$ be even-dimensional over an algebraically closed field, so that $\mathrm{Cl}(V,q)\cong M_{2^m}(A)$ with $m = \dim V/2$, and let $S$ be the irreducible (spinor) module. Then the action map

$$
\rho : \mathrm{Cl}(V,q)\longrightarrow \mathrm{End}_A(S)
$$

is an **isomorphism** of algebras, and the $2^n$ blade operators $\rho(e_{i_1}\cdots e_{i_k})$ form a basis of $\mathrm{End}_A(S)$; equivalently every endomorphism of the spinor module is a Clifford-linear combination of the blades. In bilinear form, the **bilinear covariants**

$$
b_A(s,t) = \bigl(s, \rho(\Gamma_A)\,t\bigr), \qquad \Gamma_A \text{ a basis of } \mathrm{Cl}(V,q),
$$

span the space of bilinear forms on $S$, and every bilinear form is a linear combination of the covariants.

**Proof.** The Clifford algebra is simple and $\dim \rho(\mathrm{Cl}) = \dim \mathrm{Cl} = 2^n$ because the module is faithful; and $\dim \mathrm{End}_A(S) = (\dim_A S)^2 = (2^m)^2 = 2^n$. An injective linear map between spaces of the same dimension is an isomorphism, so the blades, being a basis of the algebra, map to a basis of the endomorphisms. The bilinear statement is the isomorphism $\mathrm{Bil}_A(S,S;A)\cong \mathrm{End}_A(S)$ read in the dual basis.

**Corollary (the adjoint of a covariant).** The operator $\rho(\Gamma_A)$ has adjoint $\rho(\Gamma_A)^{\dagger} = \rho(\Gamma_A^{\dagger})$, so the covariant $b_A$ has adjoint covariant $b_{A^{*}}$ with $\Gamma_{A^{*}} = \Gamma_A^{\dagger}$; the covariant is Hermitian or skew-Hermitian for the module form exactly as the blade $\Gamma_A$ is self-adjoint or skew-adjoint under the dagger. In particular, since every vector is skew-adjoint, the **vector covariants** $b_{e_j}(s,t) = (s,\rho(e_j)t)$ are skew-Hermitian, and the **scalar covariant** $b_1(s,t) = (s,t)$ is the Hermitian module form itself.

### The Bilinear Covariants of a Spinor Module

**Proposition (the classification by grade).** For a basis of $\mathrm{Cl}(V,q)$ by grade, the covariants organise by degree: degree $0$ gives the scalar covariant $b_1$ (the module form); degree $1$ the vector covariants $b_{e_j}$; degree $2$ the bivector covariants $b_{e_ie_j}$ with $i<j$, and so on up to the volume element. The covariant $b_A$ is Hermitian iff the blade $\Gamma_A$ is self-adjoint under the dagger, which for a real blade in the standard convention happens exactly when the degree satisfies $|A|\equiv 0,3 \pmod 4$, and skew-Hermitian exactly when $|A|\equiv 1,2\pmod 4$; so the scalar and the volume covariants are Hermitian, the vectors and the bivectors are skew-Hermitian.

**Proof.** The dagger acts on a blade by $\Gamma_A^{\dagger} = \sigma(\alpha(\Gamma_A^{r})) = (-1)^{|A|(|A|-1)/2}(-1)^{|A|}\sigma(\Gamma_A) = (-1)^{T_{|A|}}\sigma(\Gamma_A)$ with $T_{|A|} = |A|(|A|+1)/2$ the triangular number, which is even exactly for $|A|\equiv0,3\pmod4$; the covariant inherits the sign by the corollary above. This was checked on the blades of $\mathrm{Cl}_{2,0}(\mathbb{C})$, $\mathrm{Cl}_{0,3}(\mathbb{R})$ and $\mathrm{Cl}_{3,0}(\mathbb{R})$: degrees $0$ and $3$ self-adjoint, degrees $1$ and $2$ skew-adjoint.

**Remark (the Fierz coefficients).** The expansion of a bilinear form in the covariants $b_A$ is the **Fierz rearrangement**. Because the blades are orthogonal for the trace form of *The Blade Form and the Hilbert Structure with Hermitian Adjoint*, the coefficient of $b_A$ in a form $b$ is $\mathrm{Tr}(\rho(\Gamma_A)^{*}T_b)$ up to the normalisation of the trace form, so the expansion is obtained by orthogonality and is a finite computation on the algebra.

## The Invariance Under the Slice

**Theorem.** For $u$ in the unitary slice $U$, the bilinear form $b\circ(u\times u)$ has the same expansion coefficients as $b$ in the covariants:

$$
b_A(u\cdot s, u\cdot t) = b_{\,u^{\dagger}\Gamma_Au}(s,t) ,
$$

so the slice permutes the covariants by the conjugation $\Gamma_A\mapsto u^{\dagger}\Gamma_A u$ of the Clifford algebra; in particular the scalar covariant is invariant, the space of degree-$k$ covariants is preserved, and the expansion of any form in the covariants is transformed by the adjoint representation of the slice.

**Proof.** $b_A(us,ut) = (us, \rho(\Gamma_A)ut) = (s, \rho(u^{\dagger}\Gamma_A u)t)$ by the adjointness of the action, $= b_{u^{\dagger}\Gamma_Au}(s,t)$, and $u^{\dagger}\Gamma_Au$ is again a blade combination of the same degree.

**Corollary (invariance and its failure).** The slice acts on the space of covariants, and the invariants are the forms whose expansion is fixed by all $u$, which on the definite module is the span of the scalar covariant alone; off the slice, the conjugation is the two-sided operator of *Two-Sided Operators on a Clifford Algebra*, and the exponent reads the sign of the general operator.

## Worked Cases

### The Complex Two-Dimensional Module

Let $A = \mathbb{C}$ with the conjugation, $\dim V = 2$ and $e_1^{2} = e_2^{2} = 1$, so that $\mathrm{Cl}\cong M_2(\mathbb{C})$ and $S = \mathbb{C}^{2}$. The four blades $1,e_1,e_2,e_1e_2$ give four action matrices, and a direct computation of their action on a minimal left ideal shows that they are linearly independent and hence a basis of the four-dimensional $\mathrm{End}_{\mathbb{C}}(\mathbb{C}^{2})$: the rank of the span is $4$, equal to $(\dim S)^{2}$. The Fierz identity is then the statement that the four covariants $b_1, b_{e_1}, b_{e_2}, b_{e_1e_2}$ span the four-dimensional space of bilinear forms on $\mathbb{C}^{2}$: $b_1$ is the Hermitian module form, and $b_{e_1}, b_{e_2}, b_{e_1e_2}$ are the three skew-Hermitian covariants of degrees $1,1,2$. The matching of the counts — $2^n = 4$ blades, $(\dim S)^{2} = 4$ endomorphisms — is the content of the theorem.

### The Quaternion Algebra

Let $\mathrm{Cl}_{0,2}(\mathbb{R}) = \mathbb{H}$ with the dagger positive and the frame $e_1,e_2$ of square $-1$. The module is the algebra itself over the division algebra $\mathbb{H}$, and the covariants are $b_1$ (the positive definite form $\mathrm{Sc}(x^{\dagger}y)$), the two skew-Hermitian vector covariants $b_{e_1}, b_{e_2}$, and the skew-Hermitian bivector covariant $b_{e_1e_2}$ of degree $2$. The completeness fails in the form stated above because $\mathbb{H}$ is a division algebra and the module is not the simple module of a full matrix algebra; instead the invariant forms are the multiples of the quaternion bilinear $\mathrm{Sc}(x^{\dagger}y)$ and of its left translations, and the coherent statement is the uniqueness theorem of *Hermitian Clifford Modules with Hermitian Adjoint* rather than the Fierz basis. The example shows the hypothesis of the completeness theorem — a simple algebra that is a full matrix algebra over the base field, with its irreducible module — and what replaces it when the module is over a division algebra.

## Summary

A **bilinear operator** on a Clifford module is the operator $s\mapsto b(s,\cdot)$ induced by a bilinear form $b$, the two carrying the same data up to the adjunction $\mathrm{Bil}_A(S,S;A)\cong \mathrm{Hom}_A(S,S^{*})$. The adjoint of a bilinear operator is the operator of the **adjoint form** $b^{*}(s,t) = \sigma(b(t,s))$, so the Hermitian forms are the self-adjoint operators and form the symmetric part of the space of bilinear forms. A form is **Clifford-equivariant** exactly when it satisfies the adjointness axiom, and the Hermitian Clifford module is the case of a Hermitian equivariant form, of which the spinor adjoint is the bilinear operator.

The **completeness of the Clifford action** — the Fierz identity — says that for an even-dimensional algebra over an algebraically closed field the action is an isomorphism $\mathrm{Cl}(V,q)\cong \mathrm{End}_A(S)$, so the $2^n$ blades are a basis of the endomorphisms and the $2^n$ **bilinear covariants** $(s,\Gamma_A t)$ span the space of bilinear forms; it was checked for the complex two-dimensional module, where the rank of the span is $4 = (\dim S)^{2}$. The covariants are classified by grade, the covariant $b_A$ being Hermitian for $|A|\equiv0,3\pmod4$ and skew-Hermitian for $|A|\equiv1,2\pmod4$, so the scalar and volume covariants are Hermitian and the vector and bivector covariants are skew-Hermitian; the adjoint of a covariant is the covariant of the dagger $\Gamma_A^{\dagger}$, so the scalar covariant is the module form and the vector covariants are skew-Hermitian. The **unitary slice** permutes the covariants by $\Gamma_A\mapsto u^{\dagger}\Gamma_Au$, fixes the scalar covariant, preserves the degree, and the invariants on the definite module are the scalar covariant alone; the expansion coefficients are the Fierz coefficients, computed by orthogonality of the blades for the trace form.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $b : S\times S\to A$ | Bilinear form |
| $b^{*}(s,t) = \sigma(b(t,s))$ | Adjoint form, $b$ Hermitian iff $b^{*}=b$ |
| $T_b : s\mapsto b(s,\cdot)$ | Bilinear operator, $T_b\in\mathrm{Hom}_A(S,S^{*})$ |
| $(T_b)^{*} = T_{b^{*}}$ | Adjoint of a bilinear operator |
| $b(xs,t) = b(s,x^{\dagger}t)$ | Clifford-equivariance |
| $\rho : \mathrm{Cl}(V,q)\cong \mathrm{End}_A(S)$ | Completeness (Fierz identity) |
| $b_A(s,t) = (s,\rho(\Gamma_A)t)$ | Bilinear covariants, spanning the forms |
| $b_A(us,ut) = b_{u^{\dagger}\Gamma_Au}(s,t)$ | Slice action on the covariants |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors*, London Mathematical Society Lecture Note Series 286 (Cambridge University Press, 2nd ed. 2001), for the bilinear covariants of a spinor module, the Fierz identity and the completeness of the Clifford action.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the Clifford algebra as the full endomorphism algebra of the spinor module and the invariant bilinear forms.
- Nicole Berline, Ezra Getzler and Michèle Vergne, *Heat Kernels and Dirac Operators*, Grundlehren der mathematischen Wissenschaften 298 (Springer, 1992), for the Clifford action, its completeness and the induced structure on the endomorphisms of a Clifford module.
- Markus Fierz, "Zur Fermischen Theorie des β-Zerfalls", *Zeitschrift für Physik* 104 (1937), 553–565, for the original rearrangement identities of the spinor bilinears.
- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for the structure of a simple algebra as a full matrix algebra and the resulting identification of the endomorphisms of its simple module.
