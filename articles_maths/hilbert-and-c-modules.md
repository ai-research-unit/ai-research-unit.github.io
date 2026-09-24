
# __Hilbert and C*-Modules__

## Introduction

A Hilbert module is the module analogue of a Hilbert space: the inner product takes its values not in the scalar field but in a $C^*$-algebra, and the norm is recovered from the $C^*$-norm of that value. The construction sits at the meeting point of this category with functional analysis. Everything algebraic that has been developed so far applies to the underlying module, and on top of it there is a completeness requirement and a metric structure which are invisible to the pure module theory; conversely, the algebra of operators on a Hilbert module reproduces the Morita theory of the preceding articles in a form adapted to $C^*$-algebras. The purpose of this article is to define Hilbert $A$-modules, to derive the elementary properties of the $A$-valued norm, and to explain the two ways in which the construction generalises the linear algebra of the earlier articles: it makes Morita equivalence available for $C^*$-algebras, and it turns the defining module of the biquaternion algebra into an equivalence bimodule between $\mathbb{B}$ and $\mathbb{C}$.

The conventions differ from the rest of the category in one respect, and the difference is stated at the outset. A **Hilbert $A$-module is taken to be a right $A$-module**. The scalar field of a $C^*$-algebra is $\mathbb{C}$, and all $C^*$-algebras in this article are complex, unital, and assumed to carry a norm unless stated otherwise. The base ring is therefore $\mathbb{C}$, not the commutative ring $R$ of the algebraic articles, and the $A$-valued inner product is conjugate-linear in the first variable and $A$-linear in the second. This is the standard convention of the subject and it is chosen so that the compatibility relation of §Morita Equivalence of $C^*$-Algebras reads $\langle x,y\rangle_A z=x\langle y,z\rangle_B$; the left-handed convention is the mirror image throughout. The symbol $\mathbb{K}$ denotes either $\mathbb{R}$ or $\mathbb{C}$, as elsewhere in the corpus.

## $C^*$-Algebras

Recall that a **$C^*$-algebra** is a complex Banach algebra $A$ with an involution ${}^*$ satisfying

$$
(ab)^*=b^*a^*, \qquad (\lambda a+\mu b)^*=\bar{\lambda}a^*+\bar{\mu}b^*, \qquad a^{**}=a, \qquad \|a^*a\|=\|a\|^2,
$$

the last identity being the $C^*$-identity. The $C^*$-identity makes the involution isometric, $\|a^*\|=\|a\|$, and forces the norm to be determined by the algebraic structure. An element $a$ is **self-adjoint** if $a^*=a$, **positive** if $a=b^*b$ for some $b$, and **unitary** if $a^*a=aa^*=1$. The set $A_+$ of positive elements is a cone, and $A_+$ defines a partial order by $a \geq b \iff a-b \in A_+$; this order is used to state that an inner product is positive definite.

Three families of examples are used below.

- $\mathbb{C}$ itself, with $z^*=\bar{z}$ and the modulus, is the basic commutative $C^*$-algebra.
- The matrix algebra $M_n(\mathbb{C})$ with conjugate transpose $a^*=\bar{a}^{\mathsf T}$ and the operator norm is a $C^*$-algebra; this is the finite-dimensional case relevant to the biquaternion algebra.
- The algebra $C(X)$ of continuous complex functions on a compact Hausdorff space $X$, with pointwise operations and $f^*(x)=\overline{f(x)}$, is a commutative $C^*$-algebra, and the Gelfand–Naimark theorem states that every commutative unital $C^*$-algebra is of this form.

The defining features of the subject are the identity $\|a^*a\|=\|a\|^2$ and the existence of an order structure. Both are used below: the first in the proof that the $A$-valued inner product induces a norm, the second in the statement of positivity.

## Hilbert $A$-Modules

### Definition

Let $A$ be a unital $C^*$-algebra. A **right Hilbert $A$-module** is a right $A$-module $E$ together with a map

$$
\langle \cdot, \cdot \rangle : E \times E \longrightarrow A
$$

such that for all $x,y,z \in E$ and $a,b \in A$:

1. $\langle x, ya+zb\rangle=\langle x,y\rangle a+\langle x,z\rangle b$;
2. $\langle x,y\rangle^*=\langle y,x\rangle$;
3. $\langle x,x\rangle \geq 0$ in $A$, and $\langle x,x\rangle=0$ implies $x=0$;
4. $E$ is complete in the norm $\|x\|=\|\langle x,x\rangle\|^{1/2}$.

The map is a **$A$-valued inner product**, or sesquilinear form. The first two axioms say that $\langle\cdot,\cdot\rangle$ is $A$-linear in the second variable and conjugate-linear in the first, as follows from 1 and 2 applied to a scalar and to $a^*$. The third states positive definiteness with respect to the order of $A$. The fourth, completeness, is the analytic requirement distinguishing a Hilbert module from the algebraic notion of a module with a form; an algebraic object satisfying 1–3 is a **pre-Hilbert $A$-module**.

A **left Hilbert $A$-module** is defined in the same way for a left $A$-module, with the inner product linear in the first variable and conjugate-linear in the second, written ${}_A\langle x,y\rangle$ to display the algebra of values. The passage between the two conventions is by the involution, ${}_A\langle x,y\rangle=\langle y,x\rangle_A^*$.

### Immediate consequences

The inner product is additive and conjugate-linear in the first variable:

$$
\langle xa+yb,z\rangle=a^*\langle x,z\rangle+b^*\langle y,z\rangle.
$$

This follows from axioms 1 and 2 and the involution identity $(a^*b)^*=b^*a$. Setting $z=0$ and $b=0$, then $y=x$ and $a=1$, in axiom 1 gives $\langle x,x\rangle=\langle x,x\rangle\cdot1$, and taking $x=y=0$ and $a=b=0$ in the display above gives $\langle 0,z\rangle=0$. Thus the inner product is sesquilinear over $A$ — conjugate-linear in the first variable, $A$-linear in the second — and compatible with the right action in both variables.

Two further identities are used repeatedly. For a self-adjoint element the order is compatible with the involution: if $a \geq 0$ then $a^*=a \geq 0$. And $\langle xa,xa\rangle=a^*\langle x,x\rangle a$, by axiom 1 applied in the second variable with $\langle xa,x\rangle=a^*\langle x,x\rangle$, which follows from axiom 2; this is the algebraic content of the compatibility of the form with the right action.

### The $A$-valued norm

**Theorem (Cauchy–Schwarz).** Let $E$ be a pre-Hilbert $A$-module. For all $x,y \in E$,

$$
\langle x,y\rangle^*\langle x,y\rangle \leq \|x\|^2 \langle y,y\rangle, \qquad \|\langle x,y\rangle\| \leq \|x\|\,\|y\|.
$$

The first inequality is in the order of $A$; the second is the numerical consequence.

*Proof.* For $a \in A$ and a real parameter, positivity of $\langle x a+y, x a+y\rangle$ expanded in the second variable gives

$$
0 \leq \langle xa+y, xa+y\rangle=a^*\langle x,x\rangle a+a^*\langle x,y\rangle+\langle y,x\rangle a+\langle y,y\rangle.
$$

Choose $a=-\langle x,x\rangle^{-1}\langle x,y\rangle$ when $\langle x,x\rangle$ is invertible, which cancels the two linear terms of the expansion, and approximate in general; the resulting inequality is the first statement. Taking norms and using the $C^*$-identity $\|a^*a\|=\|a\|^2$ and the inequality $\|u^* v\|\le\|u\|\|v\|$ gives $\|\langle x,y\rangle\|^2\leq\|x\|^2\|y\|^2$, whence the second. $\square$

**Theorem.** The $A$-valued norm $\|x\|=\|\langle x,x\rangle\|^{1/2}$ is a norm on $E$. It satisfies the parallelogram law

$$
\|x+y\|^2+\|x-y\|^2=2\|x\|^2+2\|y\|^2
$$

when the inner product is scalar-valued, that is for $A=\mathbb{C}$, and it fails in general.

*Proof.* Positive definiteness is axiom 3. Homogeneity in the complex scalars, $\|x\lambda\|=|\lambda|\,\|x\|$ for $\lambda\in\mathbb{C}$, holds because $\langle x\lambda,x\lambda\rangle=\bar\lambda\langle x,x\rangle\lambda=|\lambda|^2\langle x,x\rangle$, and the general estimate $\|xa\|\leq\|x\|\,\|a\|$ for $a\in A$ follows from the $C^*$-identity, $\|a^*\langle x,x\rangle a\|\leq\|a\|^2\|\langle x,x\rangle\|$, so that $E$ is a normed complex vector space. The triangle inequality follows from Cauchy–Schwarz:

$$
\|x+y\|^2=\|\langle x,x\rangle+\langle x,y\rangle+\langle y,x\rangle+\langle y,y\rangle\| \leq (\|x\|+\|y\|)^2.
$$

The parallelogram law fails in general because the cross terms need not cancel. For $A=\mathbb{C}^2$ and $E=A$ the elements $x=(1,0)$ and $y=(0,1)$ have $\|x\|=\|y\|=\|x+y\|=\|x-y\|=1$, so the left side is $2$ while the right side is $4$; for $A=C([0,1])$ and $E=A$ the elements $x=1$ and $y=t$ give $\|x\|^2=\|y\|^2=1$, $\|x+y\|^2=\|(1+t)^2\|=4$ and $\|x-y\|^2=\|(1-t)^2\|=1$, so the left side is $5$ while the right side is $4$, the norm of an element of $C([0,1])$ being its supremum. The law holds when the inner product is scalar-valued, and it can fail as soon as $A$ is larger than $\mathbb{C}$. $\square$

Completeness makes $E$ a Banach space over $\mathbb{C}$ and gives the norm its analytic content. In the finite-dimensional examples of §Examples and §The Defining Module of the Biquaternion Algebra completeness is automatic.

## Examples

**(a) The standard module.** For a unital $C^*$-algebra $A$, the module $E=A$ with

$$
\langle a,b\rangle_A=a^*b
$$

is a right Hilbert $A$-module. Axiom 1 is associativity, axiom 2 is $(a^*b)^*=b^*a$, and axiom 3 is positivity of $a^*a$; the norm is $\|a\|=\|a^*a\|^{1/2}=\|a\|$, so completeness is that of $A$. The module $A^n$ with the entrywise inner product $\langle (a_i),(b_i)\rangle=\sum_i a_i^*b_i$ is the standard finitely generated free Hilbert $A$-module, and it is complete.

**(b) Hilbert spaces.** For $A=\mathbb{C}$ the axioms reduce to those of a complex inner product space: $\langle x,ya\rangle=\langle x,y\rangle a$ is $\mathbb{C}$-linearity in the second variable, $\langle x,y\rangle^*=\langle y,x\rangle$ is conjugate symmetry, and positivity is the usual positivity. Hence a Hilbert $\mathbb{C}$-module is exactly a Hilbert space. The theory of this article therefore contains Hilbert space theory as the case of scalar values, and the $A$-valued theory is the generalisation in which the scalars carry a $C^*$-structure and an order.

**(c) Direct sums and summands.** The orthogonal direct sum $\bigoplus_i E_i$ of Hilbert $A$-modules is a Hilbert $A$-module, complete when the index set is finite. A direct summand of a Hilbert $A$-module, when it is closed and the projection is adjointable in the sense of §Operators, is again a Hilbert $A$-module. The finitely generated projective Hilbert $A$-modules — the direct summands of $A^n$ with adjointable projections — are the modules for which the algebraic theory of *Modules over an Algebra* and the analytic theory agree.

**(d) Continuous fields.** For a compact Hausdorff space $X$ and $A=C(X)$, a finitely generated projective Hilbert $C(X)$-module corresponds to a continuous field of finite-dimensional Hilbert spaces on $X$; this is the $C^*$-algebraic form of the Serre–Swan theorem and is the standard source of non-complemented submodules, as in §Submodules and Complements. It is mentioned here only to record that the theory is not exhausted by the free modules of example (a).

**(e) The defining module.** For the biquaternion algebra $\mathbb{B}\cong M_2(\mathbb{C})$ and $S=\mathbb{C}^2$, the scalar-valued form $\langle u,v\rangle_{\mathbb{C}}=u^*v$ makes $S$ a right Hilbert $\mathbb{C}$-module, that is, a Hilbert space, and the $\mathbb{B}$-valued form ${}_{\mathbb{B}}\langle u,v\rangle=uv^*$ makes $S$ a left Hilbert $\mathbb{B}$-module; the conjugate transpose written ${}^*$ here is the Hermitian conjugation written ${}^\dagger$ in the quaternionic articles. Both forms are used in §The Defining Module of the Biquaternion Algebra.

## Operators

### Adjointable operators

Let $E$ and $F$ be Hilbert $A$-modules. A **bounded $A$-linear map** $T: E \to F$ is **adjointable** if there is a bounded $A$-linear map $T^*: F \to E$ with

$$
\langle Tx, y\rangle_F=\langle x, T^*y\rangle_E \qquad (x \in E,\ y \in F).
$$

An adjoint is unique when it exists. The adjointable maps form a Banach space $\mathcal{L}(E,F)$, and $\mathcal{L}(E)=\mathcal{L}(E,E)$ is a $C^*$-algebra under composition and the involution $T \mapsto T^*$; this is the **$C^*$-algebra of adjointable operators** on $E$. For $E=A^n$ with its standard form, $\mathcal{L}(E)\cong M_n(A)$, so the construction reproduces the matrix algebras of the algebraic theory.

The adjointable maps form a category closed under composition, but adjointability is a genuine restriction, as the next proposition shows.

**Proposition.** A bounded $A$-linear map between Hilbert $A$-modules need not be adjointable, and a closed submodule of a Hilbert $A$-module need not be a direct summand.

*Proof sketch.* Take $A=C([0,1])$ and $E=A$ with $\langle a,b\rangle=a^*b$, and let $N=\{a \in A : a(t)=0 \text{ for } t \in [0,\tfrac12]\}$. Then $N$ is a closed $A$-submodule, and $N^\perp=\{a\in A : a(t)=0 \text{ for } t>\tfrac12\}$, so $N+N^\perp$ is contained in the proper closed submodule $\{a : a(\tfrac12)=0\}$ and $E=N\oplus N^\perp$ fails. If the inclusion $\iota: N\hookrightarrow E$, which is bounded and $A$-linear, had an adjoint $\iota^*$, then $\iota^*(y)$ would be an element of $N$ with $y-\iota^*(y) \in N^\perp$ for every $y$; summing such a decomposition would give $E=N+N^\perp$, a contradiction. So a bounded $A$-linear map need not be adjointable, and a closed submodule need not be a direct summand. $\square$

The obstruction disappears for the finitely generated projective modules, which are exactly the self-dual modules of §Submodules and Complements, and in that case the operator theory is the matrix theory of the algebraic articles.

### Compact and rank-one operators

For $x \in E$ and $y \in F$ the **rank-one operator** $\theta_{x,y}: F \to E$ is

$$
\theta_{x,y}(z)=x\langle y,z\rangle_F.
$$

It is adjointable with $\theta_{x,y}^*=\theta_{y,x}$, and it is $A$-linear by axiom 1. The closed linear span of the rank-one operators is the **compact operator** algebra $\mathcal{K}(E) \subseteq \mathcal{L}(E)$, a closed two-sided ideal. For $E=A^n$, the rank-one operators are the matrix units up to scaling and $\mathcal{K}(E)=M_n(A)=\mathcal{L}(E)$; for $E=A$ the algebra $\mathcal{K}(A)$ is the closed span of the maps $a \mapsto b\langle c,a\rangle=b c^* a$, which is all of $A$ acting by left multiplication. Thus $\mathcal{K}(A)\cong A$.

The rank-one and compact operators are the algebraic part of the theory, and the $C^*$-algebraic Morita equivalence of §Morita Equivalence of $C^*$-Algebras is formulated with them.

## Submodules and Complements

A **Hilbert submodule** of $E$ is a closed $A$-submodule. Unlike the Hilbert-space case, the orthogonal complement

$$
N^\perp=\{x \in E : \langle x,y\rangle=0 \text{ for all } y \in N\}
$$

need not satisfy $E=N \oplus N^\perp$. The reason is that the sum $N+N^\perp$ can fail to be all of $E$, and even when it is, the projection onto $N$ along $N^\perp$ need not be adjointable; the module structure of $E$ does not force the existence of a bounded adjointable module projection.

Two classes of modules remove the difficulty.

- $E$ is **self-dual** if every bounded $A$-linear map $E \to A$ is of the form $y \mapsto \langle x, y\rangle$ for some $x \in E$. For a self-dual $E$ every closed submodule is a direct summand, by a Riesz-representation argument.
- $E$ is **finitely generated projective** if it is a direct summand of $A^n$ for some $n$. Such a module is self-dual: $A^n$ is self-dual, since a bounded $A$-linear map $A^n\to A$ is given by an inner product with an element of $A^n$ by the standard module computation, and self-duality passes to direct summands with adjointable projections.

Hence for finitely generated projective Hilbert $A$-modules the theory is formally parallel to that of Hilbert spaces: closed submodules are complemented, adjoints exist, and the operator algebra is the matrix algebra. For general Hilbert modules none of these hold, and the failure is measured by the module-theoretic invariants of the earlier articles.

## Morita Equivalence of $C^*$-Algebras

The algebraic Morita equivalence of *Morita Equivalence* has a $C^*$-algebraic refinement in which the equivalence is implemented by a Hilbert bimodule, and the refinement is the reason Hilbert modules occur in this category.

### Imprimitivity bimodules

Let $A$ and $B$ be $C^*$-algebras. An **$A$-$B$-imprimitivity bimodule** is a vector space $E$ which is simultaneously

- a left Hilbert $A$-module with inner product ${}_A\langle\cdot,\cdot\rangle$,
- a right Hilbert $B$-module with inner product $\langle\cdot,\cdot\rangle_B$,
- an $(A,B)$-bimodule with the two actions commuting,

such that the two inner products are **compatible**:

$$
{}_A\langle x,y\rangle\, z=x\,\langle y,z\rangle_B \qquad (x,y,z \in E),
$$

and both are **full**:

$$
\overline{\operatorname{span}}\{{}_A\langle x,y\rangle : x,y \in E\}=A, \qquad \overline{\operatorname{span}}\{\langle x,y\rangle_B : x,y \in E\}=B.
$$

The compatibility relation is the statement that the left inner product acts as a left multiplication operator and the right inner product as a right multiplication operator, so that each is recoverable from the other.

**Theorem (Rieffel).** If $E$ is an $A$-$B$-imprimitivity bimodule, then

$$
A \cong \mathcal{K}(E_B), \qquad B \cong \mathcal{K}({}_A E),
$$

and the categories of nondegenerate \*-representations of $A$ and of $B$ are equivalent. The algebras $A$ and $B$ are then said to be **Morita equivalent** as $C^*$-algebras.

The theorem is the $C^*$-algebraic counterpart of the Morita theorems of *Morita Equivalence*: the imprimitivity bimodule plays the role of the progenerator, and the compact-operator algebras $\mathcal{K}$ play the role of the endomorphism algebras $\operatorname{End}$, the equivalence of module categories being implemented by the same balanced-product construction as before. For $A=B=\mathbb{C}$ and $E=\mathbb{C}$ the bimodule is trivial; for $A=M_n(\mathbb{C})$, $B=\mathbb{C}$, the module $E=\mathbb{C}^n$ with the forms of §Examples (e) makes $M_n(\mathbb{C})$ and $\mathbb{C}$ Morita equivalent. The standard algebraic statement that $A$ and $M_n(A)$ are Morita equivalent is the case $E=A^n$.

### The finite-dimensional case

Every finite-dimensional $C^*$-algebra is a direct sum of matrix algebras,

$$
A \cong \prod_{i=1}^{r} M_{n_i}(\mathbb{C}),
$$

and $\prod_i M_{n_i}(\mathbb{C})$ is Morita equivalent, as a $C^*$-algebra, to the commutative algebra $\mathbb{C}^r$: the imprimitivity bimodule is $\bigoplus_i \mathbb{C}^{n_i}$, with $\mathbb{C}^{n_i}$ carrying the $M_{n_i}(\mathbb{C})$-$\mathbb{C}$-bimodule structure of §Examples (e). Hence every finite-dimensional $C^*$-algebra is Morita equivalent to a commutative one, namely the algebra of functions on its finite spectrum. This is the $C^*$-algebraic form of the reduction of a semisimple algebra to its basic algebra in *Morita Equivalence*, and it is sharp: the Morita class records only the number $r$ of simple summands, not the sizes $n_i$.

## The Defining Module of the Biquaternion Algebra

Let $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}\cong M_2(\mathbb{C})$ and let

$$
S=\mathbb{C}^2
$$

be its defining module, on which $\mathbb{B}$ acts by matrix multiplication. The module $S$ carries two forms:

$$
\langle u,v\rangle_{\mathbb{C}}=u^*v \in \mathbb{C}, \qquad {}_{\mathbb{B}}\langle u,v\rangle=uv^* \in \mathbb{B},
$$

writing vectors as columns and $u^*=\bar{u}^{\mathsf{T}}$ for the conjugate transpose. The first is the standard $\mathbb{C}$-valued inner product making $S$ a right Hilbert $\mathbb{C}$-module, equivalently a Hilbert space; it is the Hermitian form $u^{\dagger}v$ of *The Defining Module of the Biquaternion Algebra*, written here with the $C^*$-involution ${}^*$ of this article in place of the symbol ${}^\dagger$ of the quaternionic articles, which denotes the same conjugate transpose. The second is its $\mathbb{B}$-valued companion $uv^{\dagger}$, the form that makes $S$ a left Hilbert $\mathbb{B}$-module. The invariant bilinear form $u^{\mathsf T}\epsilon v$ of that article is a different form, alternating rather than Hermitian, and is not an inner product.

The following properties are verified directly.

- **$\mathbb{C}$-linearity.** $\langle u,v\lambda\rangle_{\mathbb{C}}=\langle u,v\rangle_{\mathbb{C}}\lambda$ and $\langle u\lambda,v\rangle_{\mathbb{C}}=\lambda^*\langle u,v\rangle_{\mathbb{C}}$ for $\lambda \in \mathbb{C}$, so the first form is a right Hilbert $\mathbb{C}$-inner product.
- **$\mathbb{B}$-linearity.** ${}_{\mathbb{B}}\langle a u,v\rangle=a\,{}_{\mathbb{B}}\langle u,v\rangle$ for $a \in \mathbb{B}$, and ${}_{\mathbb{B}}\langle u,v\rangle^*={}_{\mathbb{B}}\langle v,u\rangle$, so the second form is a left Hilbert $\mathbb{B}$-inner product.
- **Positivity.** $u^*u=\|u\|^2 \geq 0$ in $\mathbb{C}$ and $uu^* \geq 0$ in $\mathbb{B}$, with equality only for $u=0$.
- **Compatibility.** ${}_{\mathbb{B}}\langle u,v\rangle w=(uv^*)w=u(v^*w)=u\langle v,w\rangle_{\mathbb{C}}$ for all $u,v,w \in S$.
- **Fullness.** The span of $\{u^*v\}$ is $\mathbb{C}$, and the span of $\{uv^*\}$ is the whole of $M_2(\mathbb{C})=\mathbb{B}$, since the rank-one matrices span.

Therefore $S$ is a $\mathbb{B}$-$\mathbb{C}$-imprimitivity bimodule, and by Rieffel's theorem

$$
\mathbb{B} \cong \mathcal{K}(S_{\mathbb{C}})=\mathcal{L}(S_{\mathbb{C}})=M_2(\mathbb{C}), \qquad \mathbb{C} \cong \mathcal{K}({}_\mathbb{B}S)=\mathbb{C}.
$$

The biquaternion algebra and the complex field are Morita equivalent as $C^*$-algebras, with the defining module as the equivalence bimodule. This refines the algebraic statement of *Morita Equivalence* that $\mathbb{B}\cong M_2(\mathbb{C})$ is Morita equivalent to $\mathbb{C}$: the algebraic equivalence uses the same module $S$, and the $C^*$-structure endows it with the two inner products that make the equivalence an imprimitivity. The compact operators on $S$ are all the operators, because $S$ is finite-dimensional, and this is why $\mathcal{K}=\mathcal{L}$ here; in infinite dimensions the two differ, and the difference is precisely the non-self-duality of general Hilbert modules.

## Summary

A Hilbert $A$-module over a $C^*$-algebra $A$ is a right $A$-module with an $A$-valued inner product that is $A$-linear in the second variable, conjugate-linear in the first, positive definite, and complete in the norm $\|x\|=\|\langle x,x\rangle\|^{1/2}$. The $C^*$-identity and the order structure of $A$ give the Cauchy–Schwarz inequality $\langle x,y\rangle^*\langle x,y\rangle\leq\|x\|^2\langle y,y\rangle$ and the norm inequalities $\|xa\|\leq\|x\|\|a\|$ and $\|\langle x,y\rangle\|\leq\|x\|\|y\|$, and make the norm a genuine norm. The standard modules are $A$ with $\langle a,b\rangle=a^*b$ and $A^n$ with the entrywise form; for $A=\mathbb{C}$ the theory is that of Hilbert spaces, so the construction is a strict generalisation in which the scalars carry an order. Adjointability is a genuine restriction: a bounded $A$-linear map need not have an adjoint, and a closed submodule need not be complemented, the obstructions disappearing precisely for the finitely generated projective or self-dual modules. The adjointable operators form a $C^*$-algebra $\mathcal{L}(E)$, the compact operators $\mathcal{K}(E)$ form a closed ideal, and for $E=A^n$ both are $M_n(A)$.

Morita equivalence of $C^*$-algebras is implemented by imprimitivity bimodules: an $A$-$B$-bimodule, left Hilbert over $A$ and right Hilbert over $B$, with compatible and full inner products, gives $A\cong\mathcal{K}(E_B)$ and $B\cong\mathcal{K}({}_AE)$ and an equivalence of representation categories. Every finite-dimensional $C^*$-algebra is Morita equivalent to the commutative algebra $\mathbb{C}^r$ of functions on its finite spectrum, the imprimitivity bimodule being the direct sum of the defining modules of the matrix factors. The defining module $S=\mathbb{C}^2$ of the biquaternion algebra $\mathbb{B}\cong M_2(\mathbb{C})$ carries the $\mathbb{C}$-valued form $u^*v$ and the $\mathbb{B}$-valued form $uv^*$, which are compatible because $(uv^*)w=u(v^*w)$ and full because the rank-one matrices span; hence $S$ is a $\mathbb{B}$-$\mathbb{C}$-imprimitivity bimodule and $\mathbb{B}$ is Morita equivalent to $\mathbb{C}$ as a $C^*$-algebra, refining the algebraic Morita equivalence of the preceding articles.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A$, $B$ | unital complex $C^*$-algebras |
| $\mathbb{C}$ | the complex numbers, the scalar field of a $C^*$-algebra |
| ${}^*$ | involution of a $C^*$-algebra |
| $A_+$ | cone of positive elements; $a\geq b$ iff $a-b \in A_+$ |
| $M_n(\mathbb{C})$ | matrix $C^*$-algebra |
| $C(X)$ | commutative $C^*$-algebra of continuous functions on a compact $X$ |
| $E$, $F$ | right Hilbert $A$-modules (right modules by the convention of this article) |
| $\langle x,y\rangle$ | $A$-valued inner product, $A$-linear in the second variable |
| ${}_A\langle x,y\rangle$ | left Hilbert $A$-valued inner product |
| $\|x\|=\|\langle x,x\rangle\|^{1/2}$ | the $A$-valued norm |
| $A^n$ | standard free Hilbert $A$-module |
| $N^\perp$ | orthogonal complement of a submodule |
| $\mathcal{L}(E,F)$, $\mathcal{L}(E)$ | bounded adjointable operators, and their $C^*$-algebra |
| $\mathcal{K}(E)$ | compact operators, the closed span of the rank-one operators |
| $\theta_{x,y}(z)=x\langle y,z\rangle$ | rank-one operator |
| ${}_A\langle x,y\rangle z=x\langle y,z\rangle_B$ | imprimitivity compatibility |
| $\mathcal{K}(E_B)\cong A$, $\mathcal{K}({}_AE)\cong B$ | Rieffel's Morita equivalence |
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $S=\mathbb{C}^2$ | defining module of $\mathbb{B}$, a $\mathbb{B}$-$\mathbb{C}$-imprimitivity bimodule |
| $u^*=\bar{u}^{\mathsf{T}}$ | conjugate transpose of a vector, the Hermitian conjugation written ${}^\dagger$ in the quaternionic articles |

## Further Reading

- William Arveson, *An Invitation to $C^*$-Algebras* (Springer, 1976), for the elementary theory of $C^*$-algebras used in the first section.
- Bruce Blackadar, *K-Theory for Operator Algebras* (Cambridge, 2nd ed. 1998), for Hilbert modules, compact operators and imprimitivity bimodules.
- Bruce Blackadar, *Operator Algebras: Theory of $C^*$-Algebras and von Neumann Algebras* (Springer, 2006), for the general theory of $C^*$-algebras.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Vol. I* (Academic Press, 1983), for $C^*$-algebras, positivity and the order structure.
- E. Christopher Lance, *Hilbert $C^*$-Modules: A Toolkit for Operator Algebraists* (Cambridge, 1995), for the standard reference on Hilbert $C^*$-modules, adjointability and self-duality.
- Gerard J. Murphy, *$C^*$-Algebras and Operator Theory* (Academic Press, 1990), for the Gelfand–Naimark theory and the basic examples.
- Iain Raeburn and Dana P. Williams, *Morita Equivalence and Continuous-Trace $C^*$-Algebras* (American Mathematical Society, 1998), for imprimitivity bimodules and the Morita theory of $C^*$-algebras.
- Marc A. Rieffel, "Induced representations of $C^*$-algebras", *Advances in Mathematics* **13** (1974), 176–257, for the original imprimitivity theorem.
- Jean-Pierre Serre, "Modules projectifs et espaces fibrés à fibre vectorielle", *Séminaire Dubreil–Pisot* (1957–58), for the algebraic antecedent of the projective-module classification used in example (d).
