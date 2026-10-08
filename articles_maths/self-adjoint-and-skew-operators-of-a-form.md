# __Self-Adjoint and Skew Operators of a Form__

## Introduction

The adjoint operation $T \mapsto T^{*}$ of *The Form-Adjoint of an Operator* is an involution of the algebra of operators, and an involution splits the algebra into two eigenspaces: the **self-adjoint** operators with $T^{*} = T$ and the **skew-adjoint** operators with $T^{*} = -T$. The two eigenspaces are the two algebraic structures of the category: the skew operators close under the commutator and form the **Lie algebra** of the unitary group (*The Unitary Group of a Form and Its Lie Algebra*), and the self-adjoint operators close under the anticommutator and form a **Jordan algebra** (*The Hermitian Jordan Algebra of a Form*).

The article proves the two closures from one sign computation, states the correspondence between the self-adjoint operators and the Hermitian forms of the shape $Q_{T}(x) = h(Tx,x)$, and gives the algebraic substitute for the exponential map: the **Cayley transform**, which carries a skew operator to a unitary one by rational operations and needs no limit and no completion. The analytic exponential, the spectral theorem and the polar decomposition of the operators of a form are Part II: *The Spectra of Self-Adjoint Operators with Hermitian Adjoint*, *The Polar Decomposition of an Operator of the Form* and *Self-Adjoint and Skew Operators with Hermitian Adjoint*. The bilinear counterpart is the theory of *Hermitian and Skew-Hermitian Elements*, and the corresponding elements of an algebra with an involution are *Self-Adjoint Elements and the Positive Cone*. Throughout, $(A,*,h)$ is a sesqualgebra with a form over a base $(R,\varsigma)$, $h$ is nonsingular, $2$ is invertible in the fixed ring, and the operators are the $R$-linear endomorphisms of $A$ admitting an adjoint, with $T^{*}$ the adjoint for $h$.

## The Two Eigenspaces

**Proposition.** Every operator splits as

$$
T = \tfrac{1}{2}\bigl(T + T^{*}\bigr) + \tfrac{1}{2}\bigl(T - T^{*}\bigr) ,
$$

with the first summand self-adjoint and the second skew-adjoint; the splitting is the eigenspace decomposition of the involution $T \mapsto T^{*}$, and it is unique.

**Proof.** $\bigl(\tfrac{1}{2}(T+T^{*})\bigr)^{*} = \tfrac{1}{2}(T^{*}+T)$ by the additivity and the order-two property of the adjoint, and likewise for the difference; the two subspaces meet only at $0$ because an operator with $T^{*} = T = -T$ is $0$ when $2$ is invertible in the fixed ring. The uniqueness is the uniqueness of the eigenvector decomposition of an involution.

## The Sign Rule and the Two Algebras

**Definition.** An operator is of **sign** $\varepsilon \in \{1,-1\}$ when $T^{*} = \varepsilon T$; the operators of sign $+1$ are self-adjoint and those of sign $-1$ skew-adjoint.

**Proposition (the sign rule).** If $S$ has sign $\varepsilon$ and $T$ has sign $\delta$ then

$$
(ST + TS)^{*} = \varepsilon\delta\,(ST + TS), \qquad (ST - TS)^{*} = -\varepsilon\delta\,(ST - TS) .
$$

**Proof.** $(ST)^{*} = T^{*}S^{*} = \delta\varepsilon\,TS$ and $(TS)^{*} = \varepsilon\delta\,ST$; adding gives the first identity and subtracting gives the second, and the two signs $\varepsilon, \delta$ commute as central signs.

**Corollary (the Lie algebra).** The skew-adjoint operators close under the commutator, $[S,T] = ST - TS$, and form a Lie subalgebra $\mathfrak{u}(A,h)$ of the operators; the self-adjoint operators close under the anticommutator $S \circ T = \tfrac{1}{2}(ST + TS)$ and form a Jordan subalgebra.

**Proof.** The first is the sign rule at $\varepsilon = \delta = -1$; the second is the sign rule at $\varepsilon = \delta = +1$ combined with the bilinearity of the anticommutator, the commutativity $S \circ T = T \circ S$ and the Jordan identity, which is the associativity of the underlying product read in the symmetrised form.

**Remark.** The two structures are the two halves of the same involution, and the product of two skew operators is not skew but has the two parts $ST = \tfrac{1}{2}[S,T] + S \circ T$: the commutator remains in the Lie algebra and the anticommutator leaves it, which is the classical split of the theory of Lie and Jordan structures.

## The Quadratic Form of a Self-Adjoint Operator

**Definition.** The **quadratic form** of an operator $T$ is $Q_{T}(x) = h(Tx,x)$.

**Proposition.** The operator $T$ is self-adjoint exactly when $Q_{T}$ is real-valued, and then the polarisation of $Q_{T}$ is the form $h(Tx,y) + h(Ty,x)$; when the sesquilinear forms are determined by their diagonals — in particular over a field containing a scalar $\mathrm{i}$ with $\varsigma(\mathrm{i}) = -\mathrm{i}$ — the map $T \mapsto Q_{T}$ is an injective $R^{\varsigma}$-linear map from the self-adjoint operators onto the Hermitian forms carried by $T$ in this way.

**Proof.** If $T$ is self-adjoint then $Q_{T}(x) = h(Tx,x) = h(x,Tx) = \varsigma(h(Tx,x))$. Conversely, if $Q_{T}$ is real-valued for every $x$ then the sesquilinear form $B(x,y) = h((T - T^{*})x, y)$ has vanishing diagonal and is skew-Hermitian, so it vanishes when the diagonal determines the sesquilinear forms, giving $h(Tx,y) = h(x,Ty)$. The polarisation of $Q_{T}$ is computed as in *Polarisation and the Hermitian Square*: $Q_{T}(x+y) - Q_{T}(x) - Q_{T}(y) = h(Tx,y) + h(Ty,x)$. The assignment is additive in $T$, and its kernel is the zero operator on the self-adjoint part under the same hypothesis, by the non-degeneracy of $h$; over the trivial involution the kernel contains the skew operators, whose quadratic form vanishes as in the remark of *The Form-Adjoint of an Operator*.

**Corollary.** A self-adjoint operator is a Hermitian form of the layer, and the self-adjoint operators of the form are the same data as the Hermitian forms of the shape $h(T\cdot,\cdot)$; this is the algebraic identity between the Jordan algebra of the article and the forms of the category, and it is the exact statement that the positivity of the form and the positivity of the operator are two readings of one cone (*Positivity and the Hermitian Cone of a Hermitian Algebra with Hermitian Adjoint* in Part II).

## The Cayley Transform and the Exponential

**Proposition (the Cayley transform).** Let $S$ be skew-adjoint and suppose $1 + S$ invertible. Then

$$
U = (1 - S)(1 + S)^{-1}
$$

is unitary, and the assignment is inverted by $S = (1 - U)(1 + U)^{-1}$ when $1 + U$ is invertible.

**Proof.** With $S^{*} = -S$, $(1+S)^{*} = 1 - S$ and $(1-S)^{*} = 1+S$, so $U^{*} = \bigl((1+S)^{-1}\bigr)^{*}(1+S) = (1-S)^{-1}(1+S)$; then $U^{*}U = (1-S)^{-1}(1+S)(1-S)(1+S)^{-1}$ and $(1+S)(1-S) = 1 - S^{2} = (1-S)(1+S)$ because the powers of $S$ commute with each other, giving $U^{*}U = 1$. The inversion is the same computation solved for $S$.

**Remark (the exponential).** Over $\mathbb{R}$ or $\mathbb{C}$ the exponential of a skew operator is unitary, and the identity is the origin of the correspondence between the Lie algebra and the group; the series is analytic and needs a topology, so in this algebraic layer the Cayley transform is the substitute, and the exponential is *The Lie Algebra and the Exponential Map* in Part II. The two maps agree to first order, $U = 1 - 2S + \dots$, which is the statement that the Lie algebra is the tangent space of the group at the identity.

## Examples

### The Trace Form

On $M_n(\mathbb{C})$ with $h(X,Y) = \tau(XY^{*})$ the self-adjoint operators are the Hermitian matrices, the skew operators the skew-Hermitian ones, the Jordan algebra is the real vector space of the Hermitian matrices with the anticommutator, and the Lie algebra is $\mathfrak{u}(n)$ with the commutator.

### The Indefinite Case

With the form of signature $(p,q)$ on $\mathbb{R}^{n}$ the sign rule gives the Lie algebra $\mathfrak{o}(p,q)$ of the skew operators for the form $h(Tx,x) = 0$; the self-adjoint operators are the forms of the layer and the Cayley transform produces the elements of $\operatorname{SO}(p,q)$ from them, the framework of *The Orthogonal Lie Algebra*.

### The Biquaternions

On $\mathbb{B}$ with the dagger, $Q_{T}(\tilde Q) = \operatorname{Sc}(T\tilde Q\tilde Q^{\dagger})$ is the Hermitian reading of an operator and the self-adjoint operators are the Hermitian forms of the algebra; the sandwich operators $\Theta_x$ of *The Form-Adjoint of the Multiplications* are self-adjoint exactly when $x$ is self-adjoint, and the structure is *The Hermitian Sandwich in the Biquaternion Algebra with Hermitian Adjoint*.

## Summary

- The involution $T \mapsto T^{*}$ splits the operators into the **self-adjoint** and the **skew-adjoint** parts, $T = \tfrac12(T+T^{*}) + \tfrac12(T-T^{*})$, and the splitting is unique when $2$ is invertible.
- The **sign rule** $(ST \pm TS)^{*} = \pm\varepsilon\delta(ST \pm TS)$ makes the skew operators a **Lie algebra** under the commutator and the self-adjoint operators a **Jordan algebra** under the anticommutator.
- An operator is self-adjoint exactly when its quadratic form $Q_{T}(x) = h(Tx,x)$ is Hermitian; the map $T \mapsto Q_{T}$ identifies the self-adjoint operators with the Hermitian forms of the shape $h(T\cdot,\cdot)$.
- The **Cayley transform** $U = (1-S)(1+S)^{-1}$ carries a skew operator to a unitary one by rational operations, and inverts; it is the algebraic substitute for the exponential, which belongs to Part II.
- The spectra, the polar decomposition and the functional calculus of these operators are Part II.

## Summary of Notation

| symbol | meaning |
|---|---|
| $T^{*}$ | the adjoint of $T$ for $h$ |
| $[S,T] = ST - TS$ | the commutator, giving the Lie algebra of the skew operators |
| $S \circ T = \tfrac12(ST+TS)$ | the anticommutator, giving the Jordan algebra of the self-adjoint operators |
| $Q_{T}(x) = h(Tx,x)$ | the quadratic form of an operator |
| $\mathfrak{u}(A,h)$ | the Lie algebra of the skew-adjoint operators |
| $U = (1-S)(1+S)^{-1}$ | the Cayley transform of a skew operator |

## Further Reading

- Nathan Jacobson, *Structure and Representations of Jordan Algebras*, American Mathematical Society Colloquium Publications 39 (1968), for the Jordan algebra of the self-adjoint elements of an algebra with an involution.
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings*, Grundlehren der mathematischen Wissenschaften 294 (Springer, 1991), for the algebra with an involution attached to a form and its two eigenspaces.
- Jean Dieudonné, *La géométrie des groupes classiques*, Ergebnisse der Mathematik 5 (Springer, 1955), for the Cayley transform, the reflections and the classical groups.
