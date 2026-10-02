
# __The Adjoint of the Left Multiplication on an Involutive Banach Algebra__

## Introduction

The left multiplication $L_a$ is the archetype of the operators of a Banach algebra, and its adjoint with respect to the form of the category is again a left multiplication, that by the image of the parameter under the involution: $(L_a)^\dagger = L_{\sigma(a)}$. The formula carries three things at once: the explicit expression of the adjoint, the compatibility of the adjoint with the involution, and the fact that the left regular representation is a `*`-representation. From it follows the whole dictionary between the properties of the operator and the properties of the element — self-adjointness, skewness, unitarity, involutivity — and the adjoints of the right multiplication and of the unsigned sandwich. This article computes the adjoint of the left multiplication, proves the compatibility with the involution, derives the dictionary, and reads the whole thing through the topology.

The article assumes the form of the category, the adjoint and the self-adjoint and skew operators from *The Involution on the Operator Algebra*; the involutive Banach algebra, the isometry of the involution and the self-adjoint, skew and unitary elements from *Adjoints in a Banach Algebra* and *Involutive Banach Algebras and the Gelfand–Naimark Theorem*; the one-sided multiplications, their composition and their commutation from *Operators on a Banach Algebra*; the unsigned sandwich from *The Signed Sandwich on a Banach Algebra*; and the adjoint of the left multiplication of the abstract algebra from *The Adjoint of the Left Multiplication on an Algebra*. The signed versions are *The Signed Adjoint Sandwich on a Banach Algebra* and *The Signed Adjoint of the Left Multiplication on an Involutive Banach Algebra*.

Throughout, $A$ is a unital Banach algebra over $\mathbb{C}$ with a continuous involution $\sigma$, $a^* = \sigma(a)$, and the **form of the category** $\{x,y\} = \tau(x\sigma(y))$ attached to a continuous $\sigma$-invariant trace $\tau$; the adjoint $T^\dagger$ is defined by $\{Tx,y\} = \{x,T^\dagger y\}$; $L_a(x) = ax$ and $R_b(x) = xb$ are the one-sided multiplications; and the unsigned sandwich is $\Sigma_{a,b} = L_aR_b$, $\Sigma_{a,b}(x) = axb$.

## The Adjoint of the Left Multiplication

**Theorem (the explicit form).** For every $a,b \in A$ the one-sided multiplications are adjointable, with

$$
(L_a)^\dagger = L_{\sigma(a)} , \qquad (R_b)^\dagger = R_{\sigma(b)} .
$$

Hence the adjoint of a left multiplication is the left multiplication by the image of the parameter under the involution, and the adjoint of a right multiplication is the right multiplication by the image.

**Proof.** For all $x,y$, $\{L_ax,y\} = \tau(ax\sigma(y)) = \tau(x\sigma(y)a)$ by the cyclicity of the trace, and $\tau(x\sigma(y)a) = \tau(x\sigma(\sigma(a)y)) = \{x,L_{\sigma(a)}y\}$ by the $\sigma$-invariance and $\sigma^2 = \mathrm{id}$; thus $L_{\sigma(a)}$ satisfies the defining identity, and it is the adjoint by the nondegeneracy of the form. The right-handed computation is the mirror image. $\square$

**Corollary (compatibility with the involution and the `*`-representation).** The adjoint intertwines the left multiplication with the involution, and the left regular representation $a \mapsto L_a$ is a `*`-representation:

$$
(L_a)^\dagger = L_{a^*} , \qquad L_{ab} = L_aL_b , \qquad (L_{\sigma(a)})^\dagger = L_a .
$$

Hence the involution of the elements and the adjoint of the operators agree on the image of the regular representation, an agreement proved and not assumed.

**Proof.** The formula is the theorem with $a^* = \sigma(a)$; multiplicativity is associativity, $L_aL_b = L_{ab}$; and the last identity is the theorem applied twice, $(L_{\sigma(a)})^\dagger = L_{\sigma^2(a)} = L_a$. $\square$

**Corollary (the unsigned sandwich).** The unsigned sandwich $\Sigma_{a,b}(x) = axb$ is adjointable with

$$
(\Sigma_{a,b})^\dagger = \Sigma_{\sigma(a),\sigma(b)} ,
$$

the sandwich of the images, with the order of the parameters restored rather than reversed.

**Proof.** $\Sigma_{a,b} = L_aR_b$, so $(\Sigma_{a,b})^\dagger = R_b{}^\dagger L_a{}^\dagger = R_{\sigma(b)}L_{\sigma(a)} = \Sigma_{\sigma(a),\sigma(b)}$ by the anti-multiplicativity of the adjoint. $\square$

## The Dictionary

**Theorem (the properties of the operator and of the element).** For $a \in A$,

$$
L_a \text{ self-adjoint} \iff a = a^* ; \quad L_a \text{ skew} \iff a = -a^* ; \quad L_a \text{ unitary} \iff a \text{ unitary} ; \quad L_a \text{ an involution} \iff a^2 = 1, \ a = a^* .
$$

The same dictionary holds for the right multiplications, and it holds on the image of the regular representation in $\mathcal{A}(A)$.

**Proof.** The left regular representation is injective, since $L_a = L_b$ forces $a = L_a(1) = L_b(1) = b$. Hence $L_a$ is self-adjoint iff $L_{\sigma(a)} = L_a$, that is $\sigma(a) = a$, and the skew case is the same with the sign; $L_a$ is unitary iff $L_{\sigma(a)}L_a = L_{\sigma(a)a} = L_{a^*a} = \mathrm{id}$ and $L_aL_{\sigma(a)} = L_{aa^*} = \mathrm{id}$, that is $a^*a = aa^* = 1$; and $L_a$ is an involution iff $L_a^2 = L_{a^2} = \mathrm{id}$, that is $a^2 = 1$, with $a = a^*$ from self-adjointness. $\square$

**Corollary (unitary elements and the operator norm).** If $A$ is a $\mathrm{C}^*$-algebra with the form positive definite, the unitary elements give isometric operators, $\lVert L_u\rVert = 1$, and the self-adjoint elements give self-adjoint operators with real spectrum; the map $a \mapsto L_a$ is an isometric `*`-homomorphism when the form is the Hilbert–Schmidt form and the norm is the operator norm.

**Proof.** For a unitary $u$, $\lVert L_u x\rVert = \lVert ux\rVert \leq \lVert x\rVert$ and $\lVert x\rVert = \lVert u^*ux\rVert \leq \lVert u^*\rVert\lVert ux\rVert = \lVert L_ux\rVert$, giving $\lVert L_u\rVert = 1$; the self-adjoint case is the spectral theory of *Self-Adjoint Operators of a Banach Algebra*. $\square$

## The Topology and Examples

**Proposition (continuity).** The maps $a \mapsto L_a$ and $a \mapsto L_a^\dagger$ are bounded linear maps $A \to \mathcal{A}(A)$ of norm one when the involution is isometric; the adjointable operators form a closed subalgebra of $B(A)$, complete when $B(A)$ is; and the involution and the adjoint pass to the completion.

**Proof.** $\lVert L_a\rVert \leq \lVert a\rVert$ with equality by evaluating at $1$; the adjoint map is the composite $L$ with $\sigma$, of the same norm; the completeness is *The Involution on the Operator Algebra*. $\square$

**Example (the matrix algebra).** For $A = M_n(\mathbb{C})$ with the conjugate transpose and the trace form, $(L_X)^\dagger = L_{X^*}$ and $(R_Y)^\dagger = R_{Y^*}$; the self-adjoint left multiplications are those by Hermitian matrices, the unitary ones those by unitary matrices, and the regular representation embeds $M_n$ into its own Hilbert–Schmidt operators as a `*`-representation.

**Example (the function algebra).** For $A = C(X,\mathbb{C})$ with the form $\{f,g\} = \int f\bar g$, the adjoint of $L_f$ is $L_{\bar f}$, and the dictionary reads that multiplication by $f$ is self-adjoint, skew or unitary exactly when $f$ is real, purely imaginary or unimodular.

## The Commutant of the Regular Representation

**Theorem (the commutant).** For a unital involutive Banach algebra with a nondegenerate form, the operators commuting with the left regular representation are the right multiplications,

$$
\{T \in \mathcal{A}(A) : TL_a = L_aT \ \text{for all } a\} = \{R_b : b \in A\} ,
$$

so the commutant of $\{L_a\}$ is the algebra of the right multiplications, isomorphic to $A^{\mathrm{op}}$; symmetrically the commutant of the right multiplications is the algebra of the left multiplications, and the bicommutant of the regular representation is the whole adjointable algebra.

**Proof.** If $T$ commutes with every $L_a$ then $T(x) = T(L_x1) = L_xT(1) = x\,T(1) = R_{T(1)}(x)$, so $T = R_b$ with $b = T(1)$; conversely every right multiplication commutes with every left multiplication by associativity. The symmetric statement is the mirror image, and the bicommutant follows by applying the first statement twice. $\square$

**Corollary (the adjoint and the commutant).** The commutant is closed under the adjoint, since $(R_b)^\dagger = R_{\sigma(b)}$ is again a right multiplication, and the bicommutant theorem of *Involutive Operator Algebras and the Commutant* identifies the weak closure of the regular representation with the operators of the form $R_b$; the regular representation is irreducible exactly when the right multiplications are the only operators commuting with it, that is when $A$ is a division-like algebra.

## Summary

For an involutive Banach algebra with the form of the category, the one-sided multiplications are adjointable with $(L_a)^\dagger = L_{\sigma(a)}$ and $(R_b)^\dagger = R_{\sigma(b)}$, the unsigned sandwich with $(\Sigma_{a,b})^\dagger = \Sigma_{\sigma(a),\sigma(b)}$, and the left regular representation $a \mapsto L_a$ is a `*`-representation: the involution of the elements is the adjoint of the operators on its image. The dictionary between the operator and the element holds on the image: $L_a$ is self-adjoint, skew, unitary or an involution exactly when $a$ is self-adjoint, skew, unitary or an involutive self-adjoint element; unitary elements give isometric left multiplications when $A$ is a $\mathrm{C}^*$-algebra. The regular representation is bounded with norm one for an isometric involution, the adjointable operators form a closed subalgebra of $B(A)$, and the whole structure passes to the completion. The signed versions are the articles that follow.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\sigma$, $a^*=\sigma(a)$ | The involution of the Banach algebra |
| $\{x,y\}=\tau(x\sigma(y))$, $T^\dagger$ | The form of the category and the adjoint |
| $L_a(x)=ax$, $R_b(x)=xb$ | The one-sided multiplications |
| $(L_a)^\dagger = L_{\sigma(a)}$ | The adjoint of the left multiplication |
| $(\Sigma_{a,b})^\dagger=\Sigma_{\sigma(a),\sigma(b)}$ | The adjoint of the unsigned sandwich |
| $a \mapsto L_a$ | A `*`-representation, injective |
| Dictionary | Self-adjoint/skew/unitary/involution on the element |
| $\{T : TL_a = L_aT\} = \{R_b\}$ | Commutant of the regular representation |

## Further Reading

- Charles E. Rickart, *General Theory of Banach Algebras* (Van Nostrand, 1960), for the left regular representation and the adjoints with respect to a form.
- Theodore W. Palmer, *Banach Algebras and the General Theory of ${}^*$-Algebras, Volume II* (Cambridge University Press, 2001), for the `*`-representations and the involutive Banach algebras.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume I* (Academic Press, 1983), for the left and right multiplications and their adjoints.
- Nathan Jacobson, *Structure of Rings*, American Mathematical Society Colloquium Publications 37 (1964), for the left regular representation and the involutions.
- F. R. Gantmacher, *The Theory of Matrices, Volume I* (Chelsea, 1959), for the matrix case and the trace form.
