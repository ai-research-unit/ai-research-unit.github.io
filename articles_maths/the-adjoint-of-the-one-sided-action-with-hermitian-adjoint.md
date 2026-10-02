
# __The Adjoint of the One-Sided Action with Hermitian Adjoint__

## Introduction

A Hermitian Clifford module is a Clifford module with a Hermitian form for which the Clifford action is self-adjoint, $(x\cdot s,t) = (s,x^{\dagger}\cdot t)$. That single axiom is a statement about the **adjoint of the action**: the adjoint of the operator "multiply on the left by $x$" is the operator "multiply on the left by $x^{\dagger}$", so that the action of the algebra and the action of its dagger are adjoint to one another. This article is about that adjoint: the identity $\rho(x)^{*} = \rho(x^{\dagger})$, the resulting $*$-structure on the algebra of operators, the rule for the adjoint of a composite operator built from the one-sided action, and the special case that is the algebraic reason a Dirac operator is formally self-adjoint.

The topic is algebraic. The analytic consequences of the self-adjointness — domains, closures, essential self-adjointness, spectrum, compactness of the resolvent — are the content of *Dirac Differential Operators* and are cited, not repeated. What is established here is the algebra that makes those theorems apply: the coefficients of a Dirac operator are elements of the Clifford algebra acting one-sidedly, and they are skew-adjoint exactly when the elements are; from that, and the skew-adjointness of the derivative, the formal self-adjointness of the operator follows in one line.

The Clifford action and the module form are *Hermitian Modules over a Hilbert Algebra with Hermitian Adjoint*; the one-sided operators on the algebra and their adjoints are *One-Sided Operators on a Hilbert Algebra with Hermitian Adjoint*; the two-sided family is *Two-Sided Operators on a Clifford Algebra*; the Hermitian member of that family, whose adjoint is the theorem at the end, is *The Hermitian Sandwich on a Hilbert Algebra with Hermitian Adjoint*; the forms of the dagger and the adjoint of multiplication are *The Blade Form and the Hilbert Structure with Hermitian Adjoint*; the unitary slice is *The Unitary Slice and the Compact Real Form with Hermitian Adjoint*; the spinor module is *Spinors as Minimal Left Ideals with Inner Conjugation*; and the analysis of the Dirac operator is *Dirac Differential Operators*.

## The One-Sided Action on a Hermitian Module

### The Action and Its Adjoint

**Setting.** Let $S$ be a Hermitian Clifford module over $\mathrm{Cl}(V,q)$ with form $(\cdot,\cdot)$ and scalar field $A$ with involution $\sigma$, and let

$$
\rho : \mathrm{Cl}(V,q)\longrightarrow \mathrm{End}_A(S), \qquad \rho(x)(s) = x\cdot s
$$

be the action. The **adjoint action** is the assignment $\rho^{*}(x) = \rho(x)^{*}$, the adjoint of $\rho(x)$ in $\mathrm{End}_A(S)$ with respect to the module form.

**Theorem (the adjoint of the action is the action of the dagger).** For every $x \in \mathrm{Cl}(V,q)$,

$$
\rho(x)^{*} = \rho\bigl(x^{\dagger}\bigr),
$$

and consequently $\rho$ is a **$*$-homomorphism** of the daggered algebra into the $*$-algebra of operators on $S$:

$$
\rho(xy) = \rho(x)\rho(y), \qquad \rho(x^{\dagger}) = \rho(x)^{*} .
$$

**Proof.** The adjointness axiom of *Hermitian Modules over a Hilbert Algebra with Hermitian Adjoint* is precisely $(x\cdot s,t) = (s,x^{\dagger}\cdot t)$, that is $(\rho(x)s,t) = (s,\rho(x^{\dagger})t)$; comparing with the defining property of the adjoint, $(\rho(x)s,t) = (s,\rho(x)^{*}t)$, and using the non-degeneracy of the form to cancel $s$ and $t$, gives $\rho(x)^{*} = \rho(x^{\dagger})$. The multiplicativity of $\rho$ is the module axiom, and the $*$-property is what has just been shown.

**Corollary (the adjoint action is multiplicative).** The adjoint action is a homomorphism of the daggered algebra, $\rho(x)^{*}\rho(y)^{*} = \rho(x^{\dagger})\rho(y^{\dagger}) = \rho(x^{\dagger}y^{\dagger})$, and it agrees with the action on the daggered element, so $\rho(x^{*}) = \rho(x)^{*}$ when ${}^{*}$ is the dagger of the coefficient field composed with the algebra anti-involution. Consequently the image of $\rho$ is a $*$-subalgebra of $\mathrm{End}_A(S)$, isomorphic to the quotient of $\mathrm{Cl}(V,q)$ by the kernel of the action.

### The Adjoint on the Algebra

**Corollary (the adjoint of a one-sided operator on the algebra).** With $S = \mathrm{Cl}(V,q)$ the regular module and the form $(x,y) = \mathrm{Sc}(x^{\dagger}y)$,

$$
L_a^{*} = L_{a^{\dagger}}, \qquad R_b^{*} = R_{b^{\dagger}},
$$

the statement of *One-Sided Operators on a Hilbert Algebra with Hermitian Adjoint*; so the module theorem above is the general form of that identity, and the algebra case is its regular instance.

**Corollary (vectors act by skew-adjoint operators).** For $v \in V$, $\rho(v)^{*} = \rho(v^{\dagger}) = -\rho(v)$, because the dagger negates the vectors; so every vector acts by a **skew-adjoint** operator, $\rho(v)^{*} = -\rho(v)$, and the Clifford relation reads $\rho(v)^{2} = q(v)\cdot\mathrm{id}$ with $\rho(v)$ skew-adjoint. This is the single fact from which the formal self-adjointness of the Dirac operator is read off below.

## The Adjoint as an Involution on Operators

**Proposition (the adjoint is an involutive anti-automorphism of the operator algebra).** For all $S, T \in \mathrm{End}_A(S)$ and $\lambda \in A$,

$$
(T^{*})^{*} = T, \qquad (ST)^{*} = T^{*}S^{*}, \qquad (\lambda T)^{*} = \sigma(\lambda)T^{*},
$$

so that $T\mapsto T^{*}$ is an involutive $\sigma$-antilinear anti-automorphism of $\mathrm{End}_A(S)$; the image of $\rho$ is closed under it, by the theorem.

**Proof.** The first two are the standard properties of the Hilbert-space adjoint with respect to a $\sigma$-sesquilinear form, and the third records the semilinearity: $(\lambda Ts,t) = \lambda(Ts,t)$ while $(s, T^{*}\sigma(\lambda)t) = \sigma(\lambda)(s,T^{*}t)$.

**Corollary (self-adjoint, skew-adjoint and normal elements).** For $a \in \mathrm{Cl}(V,q)$,

$$
\rho(a) \text{ is self-adjoint} \iff a^{\dagger} = a, \qquad
\rho(a) \text{ is skew-adjoint} \iff a^{\dagger} = -a, \qquad
\rho(a) \text{ is normal} \iff [a^{\dagger},a] \text{ acts as } 0 ,
$$

and $\rho(a)$ is unitary iff $a^{\dagger}a = 1$, that is iff $a$ lies in the unitary slice $U$. The slice is therefore exactly the set of elements whose one-sided action is a unitary operator on $S$, which is the operator-theoretic content of the slice.

## The Adjoint of a Composite Operator

### The General Rule

**Theorem (adjoint of a composite one-sided action).** Let $T_1,\dots,T_k$ be $A$-linear operators on $S$ that admit adjoints, and let $a_1,\dots,a_k \in \mathrm{Cl}(V,q)$. Then

$$
\Bigl(\sum_{i} \rho(a_i)\,T_i\Bigr)^{*} = \sum_{i} T_i^{*}\,\rho\bigl(a_i^{\dagger}\bigr) .
$$

**Proof.** By the anti-multiplicativity and the involution property, $(\rho(a_i)T_i)^{*} = T_i^{*}\rho(a_i)^{*} = T_i^{*}\rho(a_i^{\dagger})$, and the adjoint of a sum is the sum of the adjoints.

**Corollary (formal self-adjointness of the Dirac operator).** Let $D = \sum_j \rho(e_j)\,\partial_j$ be the flat Dirac-type operator built from an orthonormal frame $e_j$ and first-order operators $\partial_j$ that are **skew-adjoint**, $\partial_j^{*} = -\partial_j$. Then

$$
D^{*} = \sum_j \partial_j^{*}\rho(e_j^{\dagger}) = \sum_j (-\partial_j)(-\rho(e_j)) = \sum_j \rho(e_j)\partial_j = D,
$$

so $D$ is **formally self-adjoint**. The two sign flips — the coefficient is skew because it is a vector, and the derivative is skew because integration by parts introduces a minus — cancel, and the operator is its own adjoint. This is the algebraic core of the self-adjointness that *Dirac Differential Operators* develops analytically: the ellipticity of the symbol, the domain, the closure, essential self-adjointness and the spectrum are treated there, and what is shown here is only why the formal adjoint of the operator coincides with the operator.

**Remark (why the scalar direction breaks it, algebraically).** The corpus's Cauchy–Riemann operator has one coefficient equal to $1$, which is self-adjoint and not skew, $\rho(1) = \mathrm{id}$ with $\rho(1)^{*} = \rho(1)$, so the corresponding term acquires no minus from the coefficient and the operator is not symmetric; its formal adjoint is the conjugate operator, and the two split into a self-adjoint part and a skew-adjoint part. The algebra of the split is exactly the failure of one coefficient to be skew, and the analysis of the two operators is *Dirac Differential Operators*.

## The Adjoint Action of the Slice, and the Two-Sided Case

**Theorem (the slice acts by inner $*$-automorphisms).** For $u$ in the unitary slice $U$ let $\mathrm{Ad}_u(T) = \rho(u)\,T\,\rho(u)^{-1}$. Then $\rho(u)$ is unitary, $\mathrm{Ad}_u$ is an automorphism of the operator algebra, and it preserves the adjoint:

$$
\mathrm{Ad}_u(T)^{*} = \mathrm{Ad}_u\bigl(T^{*}\bigr) \qquad \text{for all } T .
$$

**Proof.** Unitarity of $\rho(u)$ is the slice theorem of *Hermitian Modules over a Hilbert Algebra with Hermitian Adjoint*; then $\mathrm{Ad}_u(T)^{*} = \rho(u)^{-*}\,T^{*}\,\rho(u)^{*} = \rho(u)\,T^{*}\,\rho(u)^{-1}$ because $\rho(u)^{*} = \rho(u)^{-1}$ for a unitary.

**Remark.** So the slice $U$ acts on the one-sided operators by $*$-automorphisms, and this action extends to the whole operator algebra; on the image of $\rho$ it is the adjoint action inside the algebra, and on the module it is the unitary action of the slice. This is the operator-algebraic form of the statement that the slice acts by operators and not by isometries of the quadratic space.

**Theorem (the adjoint of a two-sided operator is the operator at the dagger).** The standard maps $\mathrm{id}$, $\alpha$, $r$, $\bar\cdot$ and ${}^{\dagger}$ commute pairwise and each commutes with the dagger, so for the two-sided operator $\Phi^{\theta,c}_x = L_{\theta(x)}R_{c(x)}$ with $\theta$ and $c$ among them one has

$$
\bigl(\Phi^{\theta,c}_x\bigr)^{*} = \Phi^{\theta,c}_{x^{\dagger}} .
$$

In particular the **Hermitian sandwich** $\Phi^{\mathrm{id},\dagger}_x = L_xR_{x^{\dagger}}$ has adjoint $\Phi^{\mathrm{id},\dagger}_{x^{\dagger}} = L_{x^{\dagger}}R_x$, and on the slice $U$ it is unitary, $(\Phi^{\mathrm{id},\dagger}_x)^{*}\Phi^{\mathrm{id},\dagger}_x = \mathrm{id}$, which is the operator form of $u^{\dagger}u = 1$ that *The Hermitian Sandwich on a Hilbert Algebra with Hermitian Adjoint* uses.

**Proof.** $(\Phi^{\theta,c}_x)^{*} = (L_{\theta(x)}R_{c(x)})^{*} = R_{c(x)}^{*}L_{\theta(x)}^{*} = R_{c(x)^{\dagger}}L_{\theta(x)^{\dagger}} = L_{\theta(x)^{\dagger}}R_{c(x)^{\dagger}}$; and because each of the maps commutes with the dagger, $\theta(x)^{\dagger} = \theta(x^{\dagger})$ and $c(x)^{\dagger} = c(x^{\dagger})$, giving $\Phi^{\theta,c}_{x^{\dagger}}$.

## Summary

The **adjoint of the one-sided action** is the one-sided action of the dagger: for the action $\rho$ of a Clifford algebra on a Hermitian Clifford module, $\rho(x)^{*} = \rho(x^{\dagger})$, so $\rho$ is a $*$-homomorphism of the daggered algebra into the $*$-algebra of operators on the module. On the regular module this is the identity $L_a^{*} = L_{a^{\dagger}}$, $R_b^{*} = R_{b^{\dagger}}$ of the one-sided operators; for the vectors it is the **skew-adjointness** $\rho(v)^{*} = -\rho(v)$, since the dagger negates the vectors; and for an element it gives the criteria: self-adjoint, skew-adjoint, normal or unitary exactly as the element is self-adjoint, skew-adjoint, normal or in the **unitary slice** $U$.

The adjoint is an involutive, $\sigma$-antilinear, anti-multiplicative map on the operator algebra. For a composite operator it gives $(\sum_i\rho(a_i)T_i)^{*} = \sum_i T_i^{*}\rho(a_i^{\dagger})$, and applying it to the flat Dirac-type operator $D = \sum_j\rho(e_j)\partial_j$ with skew coefficients and skew derivatives produces $D^{*} = D$: the two sign flips cancel and the operator is **formally self-adjoint**, which is the algebraic core of the analysis of *Dirac Differential Operators*, the failure of the corpus's Cauchy–Riemann operator being exactly its one self-adjoint scalar coefficient. Finally the **unitary slice acts by inner $*$-automorphisms** $\mathrm{Ad}_u(T) = \rho(u)T\rho(u)^{-1}$ preserving the adjoint, and a **two-sided operator** has its adjoint at the dagger, $(\Phi^{\theta,c}_x)^{*} = \Phi^{\theta,c}_{x^{\dagger}}$, because the standard involutions commute pairwise; on the slice the Hermitian sandwich is unitary.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\rho(x)(s) = x\cdot s$ | One-sided action of the algebra on the module |
| $\rho(x)^{*} = \rho(x^{\dagger})$ | Adjoint of the action |
| $\rho(xy) = \rho(x)\rho(y)$, $\rho(x^{\dagger}) = \rho(x)^{*}$ | $\rho$ is a $*$-homomorphism |
| $\rho(v)^{*} = -\rho(v)$ | Vectors act by skew-adjoint operators |
| $U$ | Unitary slice, $\rho(u)$ unitary iff $u \in U$ |
| $\bigl(\sum_i\rho(a_i)T_i\bigr)^{*} = \sum_iT_i^{*}\rho(a_i^{\dagger})$ | Adjoint of a composite operator |
| $D = \sum_j\rho(e_j)\partial_j$, $\partial_j^{*} = -\partial_j$ | Flat Dirac-type operator, formally self-adjoint |
| $\mathrm{Ad}_u(T) = \rho(u)T\rho(u)^{-1}$ | Inner $*$-automorphism by the slice |
| $\bigl(\Phi^{\theta,c}_x\bigr)^{*} = \Phi^{\theta,c}_{x^{\dagger}}$ | Adjoint of a two-sided operator |

## Further Reading

- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the Clifford action on a Hermitian module and the skew-adjointness of the coefficients that makes the Dirac operator self-adjoint.
- Nicole Berline, Ezra Getzler and Michèle Vergne, *Heat Kernels and Dirac Operators*, Grundlehren der mathematischen Wissenschaften 298 (Springer, 1992), for the Clifford module with Hermitian structure as the data of a Dirac operator, and for the compatibility of the connection with the form.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras I*, Graduate Studies in Mathematics 15 (American Mathematical Society, 1997), for $*$-representations, the Hilbert-space adjoint and the structure of $*$-algebras of operators.
- John C. Baez and Javier P. Muniain, *Gauge Fields, Knots and Gravity*, Series on Knots and Everything 4 (World Scientific, 1994), for the Clifford action, the adjoint and the formal self-adjointness of the Dirac operator in a form close to the computation here.
- Pertti Lounesto, *Clifford Algebras and Spinors*, London Mathematical Society Lecture Note Series 286 (Cambridge University Press, 2nd ed. 2001), for the involutions of a Clifford algebra, their pairwise commutation and the adjoint of a multiplication.
