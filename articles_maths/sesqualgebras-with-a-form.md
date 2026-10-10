# __Sesqualgebras with a Form__

## Introduction

A **sesqualgebra with a form** is the object of this category: a unital associative algebra $A$ over a commutative ring $R$ with an involution $\varsigma$, equipped with a $\varsigma$-semilinear involution $*$ and a Hermitian form $h$ tied to the product by the **compatibility**

$$
h(xy,z) = h(y, x^{*}z) .
$$

The product, the involution and the form are the three data, and the compatibility is the only axiom that relates them. It says that the left multiplication by $x$ and the left multiplication by $x^{*}$ are adjoint for $h$: the involution of the algebra is the adjoint operation of the multiplications, and this single identity is the source of the whole operator theory of the category.

This article is the algebraic original of the Part II entry *Topological Sesqualgebras with a Form*: the same object read with no topology, no continuity and no completion, and with the section names kept so that a reference to a section resolves in either reading. It is the base of the category *Sesqualgebras with a degree-2 form*, the form layer of the category is built on it, and the two Part I articles that had cited the Part II entry for these statements have been repointed here: *Hermitian Forms on a Sesqualgebra* and *The Form on the Biquaternion Algebra as a General Plain Sesquilinear Form*. The layer without a form is *Sesqualgebras*, the sesquilinear product is *The Sesquilinear Product*, the scalar forms are *The Sesquilinear Form and the Conjugation*, the algebra-valued forms are *Hermitian Forms on a Sesqualgebra*, the Hermitian algebra with the dagger is *Hermitian Algebras*, and the topological reading is *Topological Sesqualgebras with a Form*. Throughout, $R$ is a commutative ring with $1$ and an involution $\varsigma$, $A$ is a unital associative $R$-algebra, $*$ is a $\varsigma$-semilinear involution of $A$, and $h : A \times A \to R$ is a form.

## The Object

### The Definition

**Definition.** A **$\varsigma$-sesquilinear form** on $A$ is a biadditive map $h : A \times A \to R$ with

$$
h(ax, y) = a\,h(x,y), \qquad h(x, ay) = \varsigma(a)\,h(x,y)
$$

for all $a \in R$ and all $x, y \in A$. The form is **Hermitian** when $h(y,x) = \varsigma(h(x,y))$ for all $x, y$, and **non-degenerate** when $h(x,y) = 0$ for every $y$ forces $x = 0$.

**Definition.** A **sesqualgebra with a form** is the quadruple $(A, *, h)$ with $A$ unital and associative, $*$ a $\varsigma$-semilinear involution, and $h$ a Hermitian form satisfying the **compatibility**

$$
h(xy, z) = h(y, x^{*}z) \qquad \text{for all } x, y, z \in A .
$$

Two of the three data are algebraic — the product and the involution — and the third is the degree-2 datum of the category. The compatibility is what forbids an arbitrary pairing, and it is the reason the form is not a decoration but a structure of the algebra.

### The Compatibility

**Proposition.** The compatibility is equivalent to

$$
h(x, yz) = h(y^{*}x, z) \qquad \text{for all } x, y, z \in A .
$$

**Proof.** Read the compatibility with the pair $(x,y)$ replaced by $(y^{*}, x)$: it becomes $h(y^{*}x, z) = h(x, y^{**}z) = h(x, yz)$, which is the second identity. The converse is the same substitution read backwards.

**Corollary.** The compatibility says that the left multiplication $L_x(y) = xy$ satisfies $h(L_xy, z) = h(y, L_{x^{*}}z)$, so $L_x$ and $L_{x^{*}}$ are adjoint with respect to $h$. The matching statement for the right multiplications, $h(yx,z) = h(y, zx^{*})$, is a *different* condition: it is the third identity refused above, it holds for the trace form $\tau(xy^{*})$, and it fails for the compatible form $\tau(xGy^{*})$ with $G = \operatorname{diag}(1,-1)$ on $\mathsf{M}_2$ (on $1728$ of the $4096$ triples of matrices with entries in $\{0,\pm1,\mathrm{i}\}$). What holds in general is that the adjoint of $R_x$ is the right multiplication by the **transpose** of $x$: the element $x^{t}$ is defined by $h(yx,z) = h(y, zx^{t})$, it exists and is unique when $h$ is nonsingular, in a basis with Gram matrix $G$ it is $x^{t} = Gx^{*}G^{-1}$, and $R_{x^{t}} = R_x^{*}$ always. The transpose is the involution $x^{*}$ exactly when the third identity holds, that is, for the trace form. The statements hold with or without non-degeneracy; non-degeneracy is what makes the adjoint unique.

**Remark (a third identity is not a consequence).** The identity $h(xy,z) = h(x, zy^{*})$ is sometimes taken for a third equivalent form of the compatibility. It is not: the trace form $\tau(xy^{*})$ of the matrix algebra satisfies it because $(zy^{*})^{*} = yz^{*}$ and the trace is cyclic, and it holds when $A$ is commutative, but the compatible non-degenerate form $\tau(xGy^{*})$ with $G = \operatorname{diag}(1,-1)$ on $\mathsf{M}_2$ fails it on $307\,008$ of the $531\,441$ triples of matrices with entries in $\{-1,0,1\}$. The identity is an extra hypothesis on the pair, and it is not used in this category.

## The Radical Is an Ideal

**Definition.** The **left radical** and the **right radical** of $h$ are

$$
\operatorname{rad}_l(A) = \{x : h(x,y) = 0 \ \text{for all } y \in A\}, \qquad
\operatorname{rad}_r(A) = \{x : h(y,x) = 0 \ \text{for all } y \in A\} .
$$

**Proposition.** For a Hermitian form the two radicals coincide as sets, and the common radical is a **left ideal** of $A$. Its image under the involution is a **right ideal**. The radical is two-sided if and only if it is $*$-invariant.

**Proof.** If $h$ is Hermitian then $h(x,y) = \varsigma(h(y,x))$ with $\varsigma$ an involution, so $h(x,y) = 0$ is equivalent to $h(y,x) = 0$ and the two sets coincide. If $x \in \operatorname{rad}$ and $a \in A$ then $h(ax, y) = h(x, a^{*}y) = 0$ for every $y$ by the second identity, so $ax \in \operatorname{rad}$ and the radical is a left ideal. For the image, $h(y, x^{*}a) = \varsigma(h(x^{*}a, y)) = \varsigma(h(a, xy)) = 0$ for every $y$ by the compatibility, so $\operatorname{rad}^{*}$ is a right ideal. Finally $\operatorname{rad}^{*} = \operatorname{rad}$ exactly when the radical is invariant under the involution, and then it is both a left and a right ideal.

**Remark.** The radical is not a right ideal in general, and two-sidedness needs an extra hypothesis. The hypothesis used by *Hermitian Algebras* is the associativity of the form, $h(xy,z) = h(x,yz)$, which makes the common radical two-sided directly. In the example below the radical is the set of the matrices with the first column zero — a left ideal and not a right ideal — and its image under the dagger is the set of the matrices with the first row zero, a right ideal.

## Full Type and Nondegeneracy

Non-degeneracy is one property of the pair $(A,h)$; the objects of full type of *Topological Sesqualgebras* are another, and the two are independent.

**Definition.** The object is of **full type** when it is faithful over $R$, the products of its elements span it, and no non-zero element annihilates it on the left or on the right.

**Proposition.** An object of full type has a **non-degenerate** form if and only if its left annihilator vanishes, and then its right annihilator vanishes as well.

**Proof.** $\operatorname{rad} = \{x : h(x,A) = 0\}$ is contained in the left annihilator $\{x : xA = 0\}$, and it contains it when the products of the elements span $A$, because $ax = 0$ for all $a$ gives $h(x,y) = 0$ for every $y$ in that span. The statement for the right annihilator follows from the coincidence of the two radicals.

The converse of the second clause fails and is refused: a free module of rank one with its zero form has a vanishing annihilator and is not of full type. The pair of hypotheses and the examples that separate them are the subject of this article and of the topological entry, *Topological Sesqualgebras with a Form*.

## The Collapse at the Trivial Involution

At $\varsigma = \mathrm{id}$ the form is $R$-bilinear; at $* = \mathrm{id}$ the compatibility reads $h(xy,z) = h(y,xz)$, which says that the left multiplications are self-adjoint for a **symmetric** bilinear form.

**Proposition.** When $\varsigma = \mathrm{id}$, $* = \mathrm{id}$ and $A$ is commutative, the sesquilinear object is exactly a commutative algebra with a symmetric associative form, and the compatibility is the associativity of the form.

**Proof.** With both involutions trivial the form is symmetric bilinear and the compatibility reads $h(xy,z) = h(y,xz)$; the second identity reads $h(x,yz) = h(yx,z) = h(xy,z)$ by commutativity, so the form is associative in the sense of *Bilinear Forms*. The category collapses to the bilinear layer of *Algebras with a degree-2 form*; the non-commutative case is *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint*.

## Examples

### The Matrix Algebra

Let $A = M_n(\mathbb{C})$ with $*$ the conjugate transpose and $\varsigma$ the complex conjugation, and let $\tau$ be the trace. Then $h(X,Y) = \tau(XY^{*})$ is a non-degenerate Hermitian form, and the compatibility is the cyclicity of the trace, $\tau(XYZ^{*}) = \tau(YZ^{*}X)$. The radical vanishes and the object is of full type.

### The Trace Pairing of a Functional

Let $\varphi : A \to R$ be $R$-linear and put $h_{\varphi}(x,y) = \varphi(y^{*}x)$. The compatibility is automatic, $h_{\varphi}(xy,z) = \varphi(z^{*}xy) = h_{\varphi}(y,x^{*}z)$, and $h_{\varphi}$ is Hermitian exactly when $\varphi(z^{*}) = \varsigma(\varphi(z))$ on the span of the products. This is the general compatible form of *The Sesquilinear Form and the Conjugation*, of which the trace form is the case $\varphi = \tau$. For $A = \mathsf{M}_2$ and the rank-one functional $\varphi(Z) = Z_{11}$ the form is degenerate with radical the left ideal of the matrices whose first column is zero.

### The Biquaternion Algebra

On $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with the dagger of *Hermitian Algebras*, the form $h(\tilde P, \tilde Q) = \operatorname{Sc}(\tilde P\tilde Q^{\dagger})$ is Hermitian and non-degenerate and the compatibility holds. The two-slot analysis of the biquaternion forms is *The Form on the Biquaternion Algebra as a General Plain Sesquilinear Form*.

## What Belongs Elsewhere

- The **topology of the layer** — the continuity of the involution and of the form and the joint continuity of the product — is *Topological Sesqualgebras with a Form* and the category *Topology on Sesqualgebras*; nothing of it is used here.
- The **positivity of the form**, the **norm defined by a form** and the **completion** are *Positivity and the Positive Cone of a Hermitian Form*, *The Norm Defined by a Form* and *The Completion of a Sesqualgebra with a Form* in Part II.
- The **scalar classification** of the forms into Hermitian, skew-Hermitian and alternating, and the correspondence with the functional, are *The Sesquilinear Form and the Conjugation*.
- The **inertia and the signature** of the form are *The Indefinite Case and the Signature*, and the **congruence classification** is *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint*.
- The **operator theory** of the pair is the rest of this category: the adjoint is *The Form-Adjoint of an Operator*, the group is *Isometries and the Unitary Group of a Form*, the Lie and the Jordan structures are *The Unitary Group of a Form and Its Lie Algebra* and *The Hermitian Jordan Algebra of a Form*.

## Summary

- A **sesqualgebra with a form** is a unital associative algebra with a $\varsigma$-semilinear involution $*$ and a Hermitian form tied by the compatibility $h(xy,z) = h(y,x^{*}z)$.
- The compatibility is equivalent to $h(x,yz) = h(y^{*}x,z)$; it says that $L_x$ and $L_{x^{*}}$ are adjoint for $h$. The identity $h(xy,z) = h(x,zy^{*})$ is not equivalent to it and is an extra hypothesis.
- The two radicals coincide for a Hermitian form; the common radical is a left ideal, its image under $*$ is a right ideal, and it is two-sided exactly when it is $*$-invariant, which holds in particular when the form is associative.
- An object of full type has a non-degenerate form exactly when its left annihilator vanishes; the converse fails and is refused.
- At the trivial base involution and the trivial algebra involution the object collapses to a commutative algebra with a symmetric associative form, the layer of *Algebras with a degree-2 form*.
- Every $R$-linear functional $\varphi$ produces the compatible form $h_{\varphi}(x,y) = \varphi(y^{*}x)$; the trace form of the matrix algebra is the case $\varphi = \tau$.
- The continuity, the positivity, the norm and the completion of the layer are Part II; the operator theory is the rest of this category.

## Summary of Notation

| symbol | meaning |
|---|---|
| $R$, $\varsigma$ | the commutative base ring and its involution |
| $A$ | a unital associative $R$-algebra |
| $*$ | the $\varsigma$-semilinear involution of $A$ |
| $h$ | the Hermitian form of the pair |
| $L_x$, $R_x$ | the left and the right multiplication by $x$ |
| $\operatorname{rad}_l$, $\operatorname{rad}_r$ | the left and the right radical |
| $\operatorname{rad}$ | the common radical of a Hermitian form |
| $h_{\varphi}$ | the compatible form $\varphi(y^{*}x)$ of a functional |
| $\tau$ | the trace of the matrix algebra |
| $\operatorname{Sc}$ | the scalar part of a biquaternion |

## Further Reading

- Winfried Scharlau, *Quadratic and Hermitian Forms* (Springer, 1985), for sesquilinear and Hermitian forms, their radicals and their isometry groups.
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings*, Grundlehren der mathematischen Wissenschaften 294 (Springer, 1991), for forms over a ring with an involution and the adjoint involution.
- Nathan Jacobson, *Structure and Representations of Jordan Algebras*, American Mathematical Society Colloquium Publications 39 (1968), for the quadratic and sesquilinear forms attached to an algebra with an involution.
