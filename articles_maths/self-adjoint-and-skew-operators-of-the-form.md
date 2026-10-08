# __Self-Adjoint and Skew Operators of the Form__

## Introduction

The adjoint $T \mapsto T^{\dagger}$ of *The Adjoint under a Hermitian Form* turns the algebra $B(A)$ of bounded operators on a sesqualgebra with a form into an algebra with involution, and an algebra with involution is cut in two by that involution. The operators fixed by the adjoint, $T^{\dagger} = T$, are **self-adjoint**; the operators negated by it, $T^{\dagger} = -T$, are **skew-adjoint**; and every operator is the sum of a self-adjoint and a skew-adjoint part, $T = \tfrac{1}{2}(T + T^{\dagger}) + \tfrac{1}{2}(T - T^{\dagger})$, as soon as $2$ is invertible in the base. The two halves carry the two algebraic structures of the operator theory: the skew-adjoint operators close under the commutator and form the **Lie algebra** of the unitary group of the form, and the self-adjoint operators close under the anticommutator and form the **special Jordan algebra** of the form. The involution is the only structure that the form imposes on the operators, so the whole operator theory — the unitary group, the symmetric space on which its complement acts, and the spectra — is encoded in this one splitting.

Three facts organise the article. The **decomposition** $T = \tfrac{1}{2}(T + T^{\dagger}) + \tfrac{1}{2}(T - T^{\dagger})$ is orthogonal for the involution, and the two parts obey a **sign rule**: if $S$ and $T$ have adjoint-signs $\epsilon$ and $\delta$ — the sign $+1$ for a self-adjoint operator and $-1$ for a skew-adjoint one — then the anticommutator $ST + TS$ has sign $\epsilon\delta$ and the commutator $ST - TS$ has sign $-\epsilon\delta$. The three familiar product relations are the three specialisations of that rule, and they are the reason the self-adjoint part is a Jordan algebra and the skew-adjoint part a Lie algebra. The **exponential and the Cayley transform** connect the two halves: the exponential of a skew-adjoint operator is unitary, so the Lie algebra integrates to the unitary group, which is the one-parameter form of the statement that the skew-adjoint operators are the infinitesimal unitaries; the Cayley transform $U = (1 - S)(1 + S)^{-1}$ is the algebraic form of the same statement, defined without a topology.

The article defines the adjoint-sign and the two parts, proves the sign rule and the two structures, develops the exponential and the Cayley transform, records the regular representation in which self-adjointness of the operator is self-adjointness of the element, and treats the indefinite case and three worked cases. The adjoint is *The Adjoint under a Hermitian Form*; the unitary group is *Unitary and Isometric Operators of the Form*; the conjugation by the fundamental symmetry is *The Fundamental Symmetry of the Form*; the positivity of the form is *Positivity and the Positive Cone of a Hermitian Form* and the positivity criterion for the operators is *The Spectra of Self-Adjoint Operators of the Form*, §*The Positivity Criterion*; the spectra are *The Spectra of Self-Adjoint Operators of the Form*; the bilinear counterparts are *Self-Adjoint and Skew Operators with Hermitian Adjoint* and *The Unitary Operators of a Sesqualgebra*. Throughout, $A$ is a sesqualgebra with a form in the sense of *Topological Sesqualgebras with a Form* over a base $(R,\varsigma)$ of one of the two classical kinds of *The Norm Defined by a Form*, with fixed field $k = R^{\varsigma}$ and $R$ complete, $h$ is Hermitian, compatible and **nonsingular**, the operators are the bounded $R$-linear maps of $A$, written $B(A)$, and **$2$ is invertible in $k$**, so that $\tfrac{1}{2}$ lies in the fixed field.

## The Adjoint Involution on the Operators

### The Operation

By *The Adjoint under a Hermitian Form*, §*The Anti-Automorphism*, the assignment $T \mapsto T^{\dagger}$ is a $\varsigma$-semilinear anti-automorphism of order two of the operator algebra: it is additive, it satisfies

$$
(\lambda T)^{\dagger} = \varsigma(\lambda)\,T^{\dagger} , \qquad (ST)^{\dagger} = T^{\dagger}S^{\dagger} , \qquad (T^{\dagger})^{\dagger} = T ,
$$

and it is defined on all of $B(A)$ because $h$ is nonsingular. An assignment with these three properties is an **involution of the operator algebra** in the sense of Part I, the twist $\varsigma$ replacing the identity of the linear case.

**Definition.** An operator $T \in B(A)$ is **self-adjoint** for $h$ when $T^{\dagger} = T$, and **skew-adjoint** for $h$ when $T^{\dagger} = -T$. The **adjoint-sign** of an operator is $+1$ when it is self-adjoint, $-1$ when it is skew-adjoint, and undefined otherwise. An operator is **normal** when it commutes with its adjoint, $TT^{\dagger} = T^{\dagger}T$.

The distinction is the one of the definite layer: for a definite form the self-adjoint operators are the Hermitian ones and the skew-adjoint operators the anti-Hermitian ones. The indefinite case retains the definitions but loses the spectral consequences, as the last section shows.

### The Two Parts

**Theorem (the decomposition).** Every $T \in B(A)$ is the sum

$$
T = \tfrac{1}{2}(T + T^{\dagger}) + \tfrac{1}{2}(T - T^{\dagger})
$$

of a self-adjoint and a skew-adjoint operator, and the two summands are the only such decomposition of $T$ when $2$ is invertible in $k$.

*Proof.* The scalar $\tfrac{1}{2}$ lies in the fixed field $k = R^{\varsigma}$, so $\varsigma(\tfrac{1}{2}) = \tfrac{1}{2}$ and $(\tfrac{1}{2}T)^{\dagger} = \tfrac{1}{2}T^{\dagger}$; the adjoint of $\tfrac{1}{2}(T + T^{\dagger})$ is $\tfrac{1}{2}(T^{\dagger} + T)$, which is itself, and the adjoint of $\tfrac{1}{2}(T - T^{\dagger})$ is $\tfrac{1}{2}(T^{\dagger} - T)$, which is its negative. If $T = S + K$ with $S$ self-adjoint and $K$ skew-adjoint, then $T^{\dagger} = S - K$, so $S = \tfrac{1}{2}(T + T^{\dagger})$ and $K = \tfrac{1}{2}(T - T^{\dagger})$, which is the uniqueness. $\square$

**Remark (the decomposition is an involution splitting, and the summands are not ideals).** The theorem writes $B(A)$ as the sum of the two eigenspaces of the operator $T \mapsto T^{\dagger}$, for the eigenvalues $+1$ and $-1$, a direct sum because $2$ is invertible; but the summands are $k$-submodules and not ideals, and the projection $T \mapsto \tfrac{1}{2}(T \pm T^{\dagger})$ is $k$-linear but only $\varsigma$-semilinear over $R$; the whole difficulty of the subject is that the self-adjoint part is not closed under the product and the skew part is not either.

### Normal Operators

**Proposition (the normal operators).** For $T \in B(A)$ the following are equivalent: $T$ is normal; the two parts of $T$ commute, $[T + T^{\dagger}, T - T^{\dagger}] = 0$; and $h(Tx,Ty) = h(T^{\dagger}x,T^{\dagger}y)$ for all $x, y$.

*Proof.* The equality $TT^{\dagger} = T^{\dagger}T$ is equivalent, by the decomposition, to the commutativity of the sum and the difference $T \pm T^{\dagger}$, which expands to $[T+T^{\dagger}, T-T^{\dagger}] = -2[T,T^{\dagger}]$. The last clause is $h(T^{\dagger}Tx,y) = h(TT^{\dagger}x,y)$, and by the nonsingularity of $h$ this is $T^{\dagger}T = TT^{\dagger}$. $\square$

The proposition is the form-layer reason the spectral theorem is stated for normal operators: a normal operator is $A + \mathrm{i}B$ with $A, B$ commuting self-adjoint operators, and a commuting family of self-adjoint operators is what the definite spectral theorem diagonalises.

## The Two Structures

### The Sign Rule

**Theorem (the sign rule).** Let $S, T \in B(A)$ have adjoint-signs $\epsilon, \delta \in \{+1,-1\}$. Then

$$
(ST + TS)^{\dagger} = \epsilon\delta\,(ST + TS) , \qquad (ST - TS)^{\dagger} = -\epsilon\delta\,(ST - TS) .
$$

*Proof.* By the anti-multiplicativity, $(ST)^{\dagger} = T^{\dagger}S^{\dagger} = \delta T \cdot \epsilon S = \epsilon\delta\,TS$, and $(TS)^{\dagger} = \epsilon\delta\,ST$. Adding and subtracting give the two assertions. $\square$

**Corollary (the three product relations).** The anticommutator of two self-adjoint operators is self-adjoint, the commutator of two self-adjoint operators is skew-adjoint, the anticommutator of a self-adjoint and a skew-adjoint operator is skew-adjoint, their commutator is self-adjoint, the anticommutator of two skew-adjoint operators is self-adjoint, and their commutator is skew-adjoint.

*Proof.* The six cases are the sign rule read at the four sign choices. $\square$

### The Skew-Adjoint Part is a Lie Algebra

**Theorem (the Lie algebra).** The skew-adjoint operators form a real Lie algebra under the commutator $[S,T] = ST - TS$, and in the definite complete case this Lie algebra is the Lie algebra of the unitary group $U(A,h)$.

*Proof.* The commutator of two skew-adjoint operators is skew-adjoint by the sign rule at $\epsilon = \delta = -1$; the commutator is bilinear and alternating, and the Jacobi identity is the associativity of the product. For the second clause, in the definite complete case the exponential $e^{tS}$ of a skew-adjoint operator is unitary for every real $t$ by the next section, so the Lie algebra exponentiates into $U(A,h)$; conversely a unitary one-parameter group has skew-adjoint generator, obtained by differentiating $h(e^{tS}x, e^{tS}y) = h(x,y)$ at $t = 0$. $\square$

**Remark (what the Lie algebra is not).** The Lie algebra is real: multiplying a skew-adjoint operator by a scalar $\lambda$ gives a skew-adjoint operator only when $\varsigma(\lambda) = \lambda$, that is when $\lambda \in k$, so the Lie algebra is a Lie algebra over the fixed field $k$ and not an $R$-module of operators closed under scalars. Over the sesquilinear base every operator is $A + \mathrm{i}B$ with $A$ and $B$ self-adjoint, so the complexification of the skew-adjoint operators is the whole operator algebra; over the collapsed base the complexification is only the part they span, the difference between the two bases being the difference between $\mathfrak{u}(n)$ and $\mathfrak{so}(n)$ at the level of the scalar field. In both cases the passage from the Lie algebra to the unitary group is the passage from $k$ to the circle of the scalars of modulus one, exactly as for the scalar field.

### The Self-Adjoint Part is a Jordan Algebra

**Theorem (the Jordan algebra).** The self-adjoint operators form a **special Jordan algebra** under the circle product

$$
S \circ T = \tfrac{1}{2}(ST + TS) ,
$$

that is, the circle product is commutative, it is $R$-bilinear, and it satisfies the Jordan identity.

*Proof.* The anticommutator of two self-adjoint operators is self-adjoint by the sign rule at $\epsilon = \delta = +1$, so the circle product stays in the self-adjoint part; it is manifestly symmetric and bilinear. The Jordan identity is inherited from the associative law: it is a linearisation of $(ST)S^{2} = S(TS^{2})$ and holds in every algebra that is associative, which is the meaning of a special Jordan algebra. $\square$

**Remark (the geometric reading).** The pair of structures is the standard pair attached to a group with an involution: the Lie algebra is the skew-adjoint part and the Jordan algebra the self-adjoint part, and the unitary group acts on the self-adjoint part, whose orbit at the identity is the symmetric space of the group. The reading of that space for the layer is the business of the geometry of the form and is not developed here.

## The Exponential and the Cayley Transform

### The One-Parameter Unitary Group

**Theorem (the exponential of a skew-adjoint operator).** Let $A$ be a Banach sesqualgebra with a form in the definite complete case, and let $S$ be skew-adjoint. Then the series $e^{S} = \sum_{n \geq 0} S^{n}/n!$ converges in $B(A)$, the operator $e^{S}$ is unitary, and $t \mapsto e^{tS}$ is a group homomorphism from the additive line into $U(A,h)$ with

$$
(e^{S})^{\dagger} = e^{-S} = (e^{S})^{-1} .
$$

*Proof.* The series converges in the operator norm because the operator norm makes $B(A)$ a Banach algebra. The adjoint operation is continuous and additive, so $(e^{S})^{\dagger} = \sum (S^{\dagger})^{n}/n! = e^{S^{\dagger}} = e^{-S}$. The two series $e^{S}$ and $e^{-S}$ multiply to $e^{S - S} = 1$ because $S$ and $-S$ commute, so $e^{S}$ is invertible with inverse $e^{-S}$; since its adjoint is its inverse, it is unitary. The group law $e^{(s+t)S} = e^{sS}e^{tS}$ is the commutativity of $sS$ and $tS$. $\square$

**Corollary (the infinitesimal characterisation).** Let the form be definite and the object complete. Then $S$ is skew-adjoint if and only if $t \mapsto e^{tS}$ is unitary for every real $t$.

*Proof.* One implication is the theorem. For the other, suppose $e^{tS}$ is unitary for every real $t$; then $h(e^{tS}x, e^{tS}y) = h(x,y)$ for all $x,y$, and differentiating with respect to $t$ at $t = 0$ gives $h(Sx,y) + h(x,Sy) = 0$, that is $h(Sx,y) = h(x,-Sy)$; by the nonsingularity of $h$ this is $S^{\dagger} = -S$. $\square$

### The Cayley Transform

**Theorem (the Cayley transform).** Let $S$ be skew-adjoint and suppose $1 + S$ invertible. Then

$$
U = (1 - S)(1 + S)^{-1}
$$

is unitary, and it is the unique operator with $1 + U$ invertible and $S = (1 - U)(1 + U)^{-1}$.

*Proof.* The factors $1 - S$ and $(1 + S)^{-1}$ commute, being functions of $S$; their adjoints are $(1 + S)^{\dagger} = 1 - S$ and $((1+S)^{-1})^{\dagger} = (1 - S)^{-1}$, so $U^{\dagger} = (1 - S)^{-1}(1 + S)$. Then $U^{\dagger}U = (1-S)^{-1}(1+S)(1-S)(1+S)^{-1} = (1-S)^{-1}(1-S)(1+S)(1+S)^{-1} = 1$, using the commutation, and similarly $UU^{\dagger} = 1$. For the inversion, $1 - U = 2S(1+S)^{-1}$ and $1 + U = 2(1+S)^{-1}$, whose ratio is $S$. $\square$

**Remark (why the Cayley transform is the algebraic form of the exponential).** The two constructions are the two ends of the same dictionary between the Lie algebra and the group: the exponential needs a topology and a complete norm, while the Cayley transform is algebraic and exists as soon as $1 + S$ is invertible. The transform is the form-layer analogue of the Cayley transform of a Hermitian operator and is the reason the skew-adjoint operators and the unitary operators of the layer can be called the same object with and without a scale.

## The Regular Representation

### The Left and the Right Multiplications

**Theorem (the multiplications).** Let $h$ be compatible and nonsingular, and let $m_{x}(z) = xz$ and $R_{b}(z) = zb^{*}$, the left multiplication and the right multiplication of *The Adjoint under a Hermitian Form*, §*The Multiplications*. Then

$$
m_{x}^{\dagger} = m_{x^{*}} , \qquad R_{b}^{\dagger} = R_{b^{*}} ,
$$

so on a unital object $m_{x}$ is self-adjoint exactly when $x = x^{*}$ and skew-adjoint exactly when $x = -x^{*}$, and $R_{b}$ is self-adjoint exactly when $b = b^{*}$ and skew-adjoint exactly when $b = -b^{*}$.

*Proof.* The adjoint formulas are those of *The Adjoint under a Hermitian Form*, §*The Multiplications*. On a unital object the map $x \mapsto m_{x}$ is injective, since $m_{x}(1) = x$, so $m_{x}^{\dagger} = m_{x}$ is $m_{x^{*}} = m_{x}$, that is $x^{*} = x$; the other three assertions are identical. $\square$

### The Hermitian and the Skew Part of the Algebra

**Proposition (the Hermitian part and the skew part).** On a unital object every element is the sum

$$
x = \tfrac{1}{2}(x + x^{*}) + \tfrac{1}{2}(x - x^{*})
$$

of a **Hermitian** element and a **skew** element, $m_{x}$ is the sum of the corresponding multiplications, and $m_{x}$ is normal exactly when the Hermitian and the skew parts of $x$ commute.

*Proof.* The involution $*$ is an involution of the algebra, so the decomposition is the algebraic case of the decomposition of an operator and its two parts are invariant under $*$; the second clause is the additivity of $x \mapsto m_{x}$. For the last, $m_{x}$ is normal when $m_{x}m_{x^{*}} = m_{x^{*}}m_{x}$, which by the injectivity of $m$ is $xx^{*} = x^{*}x$; expanding $x$ in its Hermitian and skew parts gives $[\tfrac{1}{2}(x+x^{*}), \tfrac{1}{2}(x-x^{*})] = 0$. $\square$

**Remark (the element and the operator).** The proposition is the exact point where the involution of the algebra and the involution of the operators meet: for a Hermitian element $x$ the element $e^{\mathrm{i}x}$ is unitary when $\mathrm{i}$ lies in the base, while by the theorem $e^{m_{x}}$ is a unitary operator exactly when $m_{x}$ is skew-adjoint, that is when $x$ is skew; and the two exponentials agree on the left multiplications, $e^{m_{x}} = m_{e^{x}}$.

## The Indefinite Case

### The $J$-Self-Adjoint Operators

Let the form be indefinite with fundamental decomposition $A = A^{+}\oplus A^{-}$, symmetry $J$ and companion $\langle\cdot,\cdot\rangle = h(J\cdot,\cdot)$, as in *The Fundamental Symmetry of the Form*. By *The Adjoint under a Hermitian Form*, §*The Adjoints under a Companion Form*, the two adjoints of an operator are related by

$$
T^{\dagger} = J\,T^{*}\,J ,
$$

where $T^{*}$ is the companion adjoint. The transport of the two definitions is immediate.

**Theorem (the transport of the splitting).** With the notation above, $T$ is $h$-self-adjoint if and only if $JT$ is companion-self-adjoint, and $T$ is $h$-skew-adjoint if and only if $JT$ is companion-skew-adjoint.

*Proof.* The equality $T = JT^{*}J$ is equivalent, after multiplying by $J$ on the left, to $JT = T^{*}J$, and the companion self-adjointness of $JT$ is $(JT)^{*} = T^{*}J^{*} = T^{*}J$, using the companion self-adjointness of $J$. The skew case is the same computation with the two sides negated. $\square$

**Remark (the splitting is transported, the structure is not).** The signature rule is transported by the theorem: the $h$-self-adjoint operators are the $J$-self-adjoint operators of the bilinear layer, and the Lie and Jordan structures of the two halves are the companion ones with $J$ inserted. What is **not** transported is the spectral consequence: a $J$-self-adjoint operator of an indefinite form can have non-real spectrum, so the definite statements of the next article require the definiteness and cannot be read off from the transport alone.

## Worked Cases

### The Field

**Example (the field).** Let $A = \mathbb{C}$ with $h(z,w) = z\overline{w}$, so that $\varsigma$ is the conjugation and $k = \mathbb{R}$. The operators are the multiplications $T_{\lambda}$, with $T_{\lambda}^{\dagger} = T_{\overline{\lambda}}$. Hence

$$
T_{\lambda} \text{ is self-adjoint} \iff \lambda \in \mathbb{R} , \qquad T_{\lambda} \text{ is skew-adjoint} \iff \lambda \in \mathrm{i}\mathbb{R} .
$$

The skew-adjoint operators are the line $\mathrm{i}\mathbb{R}$, which is the Lie algebra of the circle $U(1)$, and the self-adjoint operators are the line $\mathbb{R}$; the exponential of $\mathrm{i}\theta$ is the point $e^{\mathrm{i}\theta}$ of the circle, and the Cayley transform of $\mathrm{i}t$ is the point $(1-\mathrm{i}t)(1+\mathrm{i}t)^{-1} = (\mathrm{i}+t)/(\mathrm{i}-t)$ of the same circle. The example is the smallest in which the Lie algebra, the group and both transforms are visible at once, and its skew-adjoint operators are the purely imaginary scalars, which carry no real part.

### The Matrices

**Example (the matrices).** Let $A = M_{n}(\mathbb{C})$ with the conjugate transpose and the trace form $h(X,Y) = \operatorname{tr}(XY^{*})$, and let $m_{Z}$ be the multiplication by $Z$ on the left. By the regular representation, $m_{Z}$ is self-adjoint exactly when $Z$ is Hermitian and skew-adjoint exactly when $Z$ is skew-Hermitian; the skew-adjoint multiplications therefore form the Lie algebra $\mathfrak{u}(n)$ of the unitary group $U(n)$, and the self-adjoint ones the Jordan algebra of the Hermitian matrices. The exponential of $m_{Z}$ is the multiplication by $e^{Z}$, which is unitary exactly when $Z$ is skew-Hermitian, and the identification of the operator algebra with $\mathbb{C}^{n^{2}}$ through the trace form carries the adjoint of the layer to the conjugate transpose of the operator, so the splitting of the layer is the classical one. The example is the model of the article and the smallest in which the Lie algebra is not abelian.

### The Hyperbolic Plane

**Example (the hyperbolic plane).** On $A = \mathbb{R}^{2}$ with the indefinite form $h(x,y) = x_{1}y_{1} - x_{2}y_{2}$ of signature $(1,1)$, the operators are the $2 \times 2$ real matrices and the adjoint is $T^{\dagger} = J T^{T}J$ with $J = \operatorname{diag}(1,-1)$, so $T$ is self-adjoint exactly when $T^{T}J = JT$. The matrix

$$
T = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}
$$

satisfies this relation and is therefore self-adjoint, while its characteristic polynomial is $\lambda^{2} + 1$ and its spectrum is $\{\mathrm{i}, -\mathrm{i}\}$: a self-adjoint operator of an indefinite form with a purely imaginary spectrum. The example is the smallest witness that the splitting of the operators and the reality of the spectrum are independent, and it is the obstruction to reading the definite spectral theorem in the indefinite case.

## Summary

The adjoint of *The Adjoint under a Hermitian Form* splits the operator algebra into a **self-adjoint** and a **skew-adjoint** part, $T = \tfrac{1}{2}(T + T^{\dagger}) + \tfrac{1}{2}(T - T^{\dagger})$, the two parts being the eigenspaces of the involution $T \mapsto T^{\dagger}$ for the eigenvalues $+1$ and $-1$. The two parts obey the **sign rule**: the anticommutator of operators with adjoint-signs $\epsilon$ and $\delta$ has sign $\epsilon\delta$ and the commutator has sign $-\epsilon\delta$, so the **skew-adjoint** operators form a Lie algebra — the Lie algebra of the unitary group — and the **self-adjoint** operators a special Jordan algebra under the circle product. The **exponential** of a skew-adjoint operator is unitary, and $S$ is skew-adjoint exactly when $t \mapsto e^{tS}$ is unitary for every real $t$; the **Cayley transform** $U = (1-S)(1+S)^{-1}$ is the same statement without a topology. In the **regular representation** self-adjointness of the operator is self-adjointness of the element, and the splitting of the operator algebra is the splitting of the algebra into its Hermitian and skew parts. In the **indefinite case** the splitting is transported to the companion, $T^{\dagger} = JT^{*}J$, but the spectral consequences are not: a self-adjoint operator of an indefinite form can have non-real spectrum, as the hyperbolic plane shows.

## Summary of Notation

| symbol | meaning |
|---|---|
| $T^{\dagger} = T$ | a self-adjoint operator of the form |
| $T^{\dagger} = -T$ | a skew-adjoint operator of the form |
| $T = \tfrac{1}{2}(T+T^{\dagger}) + \tfrac{1}{2}(T-T^{\dagger})$ | the decomposition into a self-adjoint and a skew-adjoint part |
| $(ST)^{\dagger} = T^{\dagger}S^{\dagger}$ | the anti-multiplicativity of the adjoint |
| $\epsilon, \delta \in \{+1,-1\}$ | the adjoint-signs of two operators |
| $(ST+TS)^{\dagger} = \epsilon\delta(ST+TS)$ | the sign rule for the anticommutator |
| $(ST-TS)^{\dagger} = -\epsilon\delta(ST-TS)$ | the sign rule for the commutator |
| $S \circ T = \tfrac{1}{2}(ST+TS)$ | the circle product of the special Jordan algebra |
| $[S,T] = ST-TS$ | the commutator of the Lie algebra of the skew part |
| $e^{S}$, $(e^{S})^{\dagger} = e^{-S}$ | the exponential of a skew-adjoint operator is unitary |
| $U = (1-S)(1+S)^{-1}$ | the Cayley transform of a skew-adjoint operator |
| $m_{x}^{\dagger} = m_{x^{*}}$, $R_{b}^{\dagger} = R_{b^{*}}$ | the regular representation |
| $T^{\dagger} = JT^{*}J$ | the transport of the splitting to the companion |

## Further Reading

- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras I* (Academic Press, 1983), for the self-adjoint, normal and unitary operators and the two halves of an algebra with involution.
- John B. Conway, *A Course in Functional Analysis* (2nd ed., Springer, 1990), for the exponential of an operator, the one-parameter unitary groups and the Cayley transform.
- Israel Gohberg, Peter Lancaster and Leiba Rodman, *Indefinite Linear Algebra and Applications* (Birkhäuser, 2005), for the $J$-self-adjoint and $J$-unitary operators and the transport between the two adjoints.
- János Bognár, *Indefinite Inner Product Spaces* (Springer, 1974), for the relation between a self-adjoint operator of an indefinite form and its spectrum.
- Harald Upmeier, *Jordan Algebras in Analysis, Operator Theory, and Quantum Mechanics* (American Mathematical Society, 1987), for the special Jordan algebra of the self-adjoint part and its relation to the symmetric space.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society Colloquium Publications 44, 1998), for the involutions of an algebra, their two eigenspaces and the Hermitian and skew elements.
