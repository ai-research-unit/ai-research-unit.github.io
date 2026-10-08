# __The Form-Adjoint of an Operator__

## Introduction

A Hermitian form pairs two elements and returns a scalar, and an operator acting on the first slot is carried by the pairing to an operator acting on the second: the **adjoint** of $T$ for $h$ is the operator $T^{*}$ with

$$
h(Tx, y) = h(x, T^{*}y) \qquad \text{for all } x, y \in A .
$$

This article constructs it for the form of *Sesqualgebras with a Form* and proves that its existence and its uniqueness are exactly the non-degeneracy of the form. The adjoint is the single instrument from which the operator theory of the category is built: the isometries are the solutions of $T^{*}T = 1$ (*Isometries and Unitary Operators of a Form*), the self-adjoint and skew operators are the eigenspaces of the involution $T \mapsto T^{*}$ (*Self-Adjoint and Skew Operators of a Form*), the multiplications of the algebra have their adjoints given by the involution (*The Form-Adjoint of the Multiplications*), and the unitary group is the stabiliser of the form (*Congruence and the Stabiliser of a Form*).

Three facts organise the article. The adjoint exists and is unique as soon as the form is **nonsingular**, that is, as soon as the Riesz map $y \mapsto h(\cdot, y)$ is an isomorphism; the assignment $T \mapsto T^{*}$ is then a $\varsigma$-semilinear anti-automorphism of order two of the algebra of operators, not an $R$-linear one, because the form carries the twist in its second slot. A **semilinear** operator admits no linear adjoint, and its adjoint is taken by the twisted rule $h(Sx,y) = \varsigma(h(x,S^{*}y))$, which makes the two adjoints of $S$ — against $h$ and against the transposed form — coincide, because $h$ is Hermitian. And the formula of the adjoint is read from the **Gram matrix** of the form in a basis; the two conventions of the slots give the two formulas $T^{*} = T^{\dagger}$ and $T^{*} = G^{-1}T^{\dagger}G$, and the article states both, because the corpus uses both.

The topological companion, in which the adjoint is taken on the bounded operators of a complete space, is *The Adjoint under a Hermitian Form* and *Adjoints of Bounded Sesquilinear Operators*; the algebraic original of the transposition is *The Transpose as an Adjoint*, and the adjoint in an involutive algebra is *The Adjoint in an Involutive Algebra*. Throughout, $(A,*,h)$ is a sesqualgebra with a form over a base $(R,\varsigma)$, $h$ is nonsingular, the operators are the $R$-linear endomorphisms of $A$, and $h^{\dagger}(x,y) = \varsigma(h(y,x))$ is the transposed form.

## Existence and Uniqueness

**Definition.** Let $h$ be nonsingular and let $T$ be an $R$-linear endomorphism of $A$. The **adjoint** of $T$ for $h$ is the endomorphism $T^{*}$ with $h(Tx,y) = h(x,T^{*}y)$ for all $x, y$.

**Proposition.** The adjoint exists and is unique if and only if $h$ is nonsingular; the two Riesz maps $x \mapsto h(x,\cdot)$ and $y \mapsto h(\cdot,y)$ are injective when $h$ is non-degenerate and are isomorphisms exactly when $h$ is nonsingular.

**Proof.** For fixed $T$ the map $y \mapsto h(Tx, y)$ is, for each $x$, an $R$-linear functional of $y$; the second Riesz map $y \mapsto h(\cdot,y)$ being an isomorphism, there is for each $x$ a unique $T^{*}y$ with $h(Tx,y) = h(x,T^{*}y)$. The assignment $y \mapsto T^{*}y$ is $R$-linear because the Riesz map is, so $T^{*}$ is an operator, and the uniqueness of the representing element gives the uniqueness of $T^{*}$. If the Riesz map fails to be onto, a functional of the form $h(Tx,\cdot)$ need not be represented, and the adjoint fails to exist.

**Corollary.** When the form is only non-degenerate and not nonsingular, the adjoint exists for every $T$ whose associated functionals are represented; the distinction is the one of the topological articles between an adjoint that exists and an adjoint that does not, and it is empty over a field in finite dimension.

## The Involution of the Operator Algebra

**Proposition.** The assignment $T \mapsto T^{*}$ is $\varsigma$-semilinear and an anti-automorphism of order two:

$$
(S + T)^{*} = S^{*} + T^{*}, \qquad (\lambda T)^{*} = \varsigma(\lambda)T^{*}, \qquad (ST)^{*} = T^{*}S^{*}, \qquad (T^{*})^{*} = T .
$$

**Proof.** Additivity and the semilinearity are read from $h((\lambda T)x, y) = \lambda h(Tx,y) = \lambda h(x,T^{*}y)$ and $h(x, \varsigma(\lambda)T^{*}y) = \varsigma(\varsigma(\lambda))h(x,T^{*}y)$, using that the first slot is $R$-linear and the second $\varsigma$-semilinear. For the product, $h(STx, y) = h(Tx, S^{*}y) = h(x, T^{*}S^{*}y)$. For the last, $h(T^{*}x, y) = \varsigma(h(y, T^{*}x)) = \varsigma(h(Ty, x)) = h(x, Ty)$, so $(T^{*})^{*} = T$.

**Corollary.** The adjoint operation makes the algebra of operators an algebra with a $\varsigma$-semilinear involution in the sense of *Involutive Algebras*; the topological counterpart of the same statement, with the adjoint of a bounded operator, is *Involutions of the Operator Algebra*.

## Self-Adjoint, Skew and Normal Operators

**Definition.** An operator is **self-adjoint** when $T^{*} = T$, **skew-adjoint** when $T^{*} = -T$, **normal** when $TT^{*} = T^{*}T$, and **unitary** when $T^{*}T = TT^{*} = 1$. The **quadratic form of $T$** is the function $Q_{T}(x) = h(Tx,x)$.

**Proposition.** The first two of the following are equivalent always; when the sesquilinear forms are determined by their diagonals — in particular over a field containing a scalar $\mathrm{i}$ with $\varsigma(\mathrm{i}) = -\mathrm{i}$ — they are also equivalent to the third:

- $T$ is self-adjoint;
- $h(Tx, y) = h(x, Ty)$ for all $x, y$;
- $Q_{T}$ is real-valued, $Q_{T}(x) = \varsigma(Q_{T}(x))$ for every $x$.

**Proof.** The first two are the definition of the adjoint. If $T$ is self-adjoint then $Q_{T}(x) = h(Tx,x) = h(x,Tx) = \varsigma(h(Tx,x)) = \varsigma(Q_{T}(x))$. Conversely, let $B(x,y) = h\bigl((T - T^{*})x, y\bigr)$; the reality of $Q_{T}$ says that $h((T-T^{*})x,x) = 0$ for every $x$, that is $B(x,x) = 0$, and $B$ is skew-Hermitian, $B(y,x) = -\varsigma(B(x,y))$. A sesquilinear form with vanishing diagonal vanishes as soon as the diagonal determines the sesquilinear forms, so $B = 0$ and $T = T^{*}$.

**Remark (the diagonal sees only the trace form).** Over a base in which no polarising scalar is available the third condition is strictly weaker. On $\mathbb{R}$ with the trivial involution, the operator $T(x_{1},x_{2}) = (x_{2},-x_{1})$ — the rotation by a right angle — is skew and has the identically vanishing quadratic form $Q_{T} = 0$, while it is not self-adjoint: the diagonal recovers only the trace form $h(Tx,y) + h(Ty,x)$ of $T$, never the skew-Hermitian part.

**Corollary.** Every operator decomposes as $T = \tfrac{1}{2}(T + T^{*}) + \tfrac{1}{2}(T - T^{*})$ into a self-adjoint and a skew-adjoint part when $2$ is invertible in the fixed ring, and the two parts are the eigenspaces of the involution $T \mapsto T^{*}$.

## The Semilinear Operator and the Two Adjoints

**Definition.** An operator $S$ is **$\varsigma$-semilinear** when $S(\lambda x) = \varsigma(\lambda)Sx$; its **twisted adjoint** is the semilinear operator $S^{*}$ with

$$
h(Sx, y) = \varsigma\bigl(h(x, S^{*}y)\bigr) .
$$

**Proposition.** A semilinear operator admits no adjoint in the linear sense, and it admits exactly one twisted adjoint when $h$ is nonsingular; the twisted adjoint is again $\varsigma$-semilinear and of order two.

**Proof.** If $S$ is $\varsigma$-semilinear then $y \mapsto h(Sx,y)$ is $\varsigma$-linear and not $R$-linear, so the linear equation $h(Sx,y) = h(x,Uy)$ has no solution in general; the twisted equation asks for the representing element of the $\varsigma$-linear functional $\varsigma\circ h(Sx,\cdot)$, and it has a unique solution by nonsingularity. The last clause is read as in the linear case.

**Corollary (the two adjoints coincide).** The twisted adjoint of $S$ is the same operator as the adjoint of $S$ taken against the transposed form $h^{\dagger}$, because $h$ is Hermitian; this is the algebraic form of the identity of *The Adjoint under a Hermitian Form*, and it is the reason the corpus's semilinear operators carry one adjoint and not two.

## The Adjoint and the Gram Matrix

Let $A$ be free of finite rank over the base with basis $e_{1},\dots,e_{n}$ and **Gram matrix** $G$, $G_{ij} = h(e_{i},e_{j})$, and let an operator be represented by its matrix $T$ acting on the coordinates: the operator is the multiplication $x \mapsto Tx$ read in the basis. The adjoint depends on the convention of the slots, and the two formulas are stated for the multiplicative operators, in which the operator matrix and the coordinate matrix coincide.

**Proposition.** With the dagger in the first slot and the form $h_{G}(x,y) = \tau(x^{\dagger}Gy)$, the adjoint of the multiplication by $T$ is the multiplication by

$$
T^{*} = G^{-1}T^{\dagger}G, \qquad \text{and the multiplication by } T \text{ is an isometry} \iff T^{\dagger}GT = G ,
$$

the equation of the indefinite unitary group of $G$; for $G = 1$ it is $T^{*} = T^{\dagger}$, the conjugate transpose of the definite case, and the form is then the canonical form of *Hermitian Algebras*.

**Proof.** $h_{G}(Tx,y) = \tau(x^{\dagger}T^{\dagger}Gy)$ and $h_{G}(x,T^{*}y) = \tau(x^{\dagger}GT^{*}y)$, and the two agree for all $x,y$ exactly when $T^{\dagger}G = GT^{*}$, that is $T^{*} = G^{-1}T^{\dagger}G$. The isometry statement is the substitution $T^{\dagger}GT = G$. The verification by recomputation on the left multiplications by the $2\times2$ matrices over $\mathbb{Z}[\mathrm{i}]$ confirms both formulas ($4096$ triples, no failure).

**Remark (the other convention).** With the dagger in the second slot and the form $h(x,y) = \tau(xGy^{\dagger})$ the Gram matrix leaves the adjoint of a multiplication invisible: $T^{*} = T^{\dagger}$, and the isometry equation is $T^{\dagger}T = 1$. The two conventions occur in the corpus — the blade form $\operatorname{Sc}(x^{\dagger}y)$ is of the first kind, the trace form $\tau(xy^{*})$ of the second — and the placement of the dagger decides whether the Gram matrix enters the adjoint.

**Remark (the operator and the matrix).** The formulas are statements about the multiplication operators, and they do not extend to the arbitrary operators of the algebra of operators: an operator of a general shape is not the left multiplication by a matrix, and for such an operator the equation $U^{*}U = 1$ of the next article remains the definition while the matrix equation $U^{\dagger}GU = G$ does not apply. The two readings coincide exactly on the multiplicative operators, which is the class used in *The Form-Adjoint of the Multiplications*.

## Summary

- The **adjoint** of $T$ for $h$ is defined by $h(Tx,y) = h(x,T^{*}y)$; it exists and is unique exactly when $h$ is nonsingular.
- The assignment $T \mapsto T^{*}$ is a $\varsigma$-semilinear anti-automorphism of order two of the operator algebra: $(ST)^{*} = T^{*}S^{*}$, $(\lambda T)^{*} = \varsigma(\lambda)T^{*}$, $(T^{*})^{*} = T$.
- $T$ is self-adjoint exactly when $h(Tx,y) = h(x,Ty)$, equivalently when $Q_{T}(x) = h(Tx,x)$ is Hermitian; every operator splits into a self-adjoint and a skew-adjoint part when $2$ is invertible.
- A semilinear operator has no linear adjoint; its twisted adjoint $h(Sx,y) = \varsigma(h(x,S^{*}y))$ exists and coincides with the adjoint against the transposed form, because $h$ is Hermitian.
- In a basis with Gram matrix $G$ and the dagger in the first slot the adjoint is $T^{*} = G^{-1}T^{\dagger}G$ and the isometry equation is $T^{\dagger}GT = G$; with the dagger in the second slot it is $T^{*} = T^{\dagger}$ and $T^{\dagger}T = 1$.
- The bounded and the completed adjoint are *The Adjoint under a Hermitian Form* in Part II; the bilinear original is *The Transpose as an Adjoint* and the involutive-algebra reading is *The Adjoint in an Involutive Algebra*.

## Summary of Notation

| symbol | meaning |
|---|---|
| $T^{*}$ | the adjoint of $T$ for $h$ |
| $h^{\dagger}$ | the transposed form $h^{\dagger}(x,y) = \varsigma(h(y,x))$ |
| $Q_{T}(x) = h(Tx,x)$ | the quadratic form of an operator |
| $G$ | the Gram matrix of the form in a basis |
| $h_{G}(x,y) = \tau(x^{\dagger}Gy)$ | the form with the dagger in the first slot |
| $\varsigma$ | the involution of the base ring |

## Further Reading

- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings*, Grundlehren der mathematischen Wissenschaften 294 (Springer, 1991), for the adjoint involution of a form over a ring with an involution.
- Nathan Jacobson, *Structure and Representations of Jordan Algebras*, American Mathematical Society Colloquium Publications 39 (1968), for the adjoint with respect to a form and the operators attached to it.
- Jean Dieudonné, *La géométrie des groupes classiques*, Ergebnisse der Mathematik 5 (Springer, 1955), for the adjoint, the transvection and the classical groups.
