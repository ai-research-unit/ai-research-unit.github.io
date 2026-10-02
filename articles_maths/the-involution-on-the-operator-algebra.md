
# __The Involution on the Operator Algebra__

## Introduction

The algebra of bounded operators of a Banach algebra is an algebra without an involution, but a **form** on the algebra turns it into one: the **adjoint** of a bounded operator $T$ is the operator $T^\dagger$ determined by $\{Tx,y\} = \{x,T^\dagger y\}$, and the map $T \mapsto T^\dagger$ is additive, involutive and anti-multiplicative, so it is an anti-automorphism of the operator algebra of order two. The form of the category is the **trace pairing** $\{x,y\} = \tau(x\sigma(y))$ attached to a continuous $\sigma$-invariant trace $\tau$; when it is nondegenerate the adjoint exists and is unique, the adjointable operators form a closed subalgebra, and the left regular representation $a \mapsto L_a$ becomes a `*`-representation, $(L_a)^\dagger = L_{\sigma(a)}$. This article fixes the form of the category, defines the adjoint and proves that it is an order-two anti-automorphism of the operator algebra.

The article assumes the Banach algebra, the bounded operators, the operator norm and the left and right multiplications from *Operators on a Banach Algebra*; the involution, its continuity, the fixed and skew elements and the isometry of the involution from *Involutive Banach Algebras and the Gelfand–Naimark Theorem*; the self-adjoint and unitary elements from *Adjoints in a Banach Algebra*; the completeness and closed subalgebras of the operator algebra from *The Operator Algebra of a Banach Space*; and the trace, the pairing and the operator involution of the finite-dimensional case from *Frobenius Algebras* and *The Adjoint in an Involutive Algebra*. The signed and reflection adjoints are the articles that follow; the grade involution $\alpha$ appears there.

Throughout, $A$ is a unital Banach algebra over $\mathbb{C}$ with a **continuous involution** $\sigma$, $a^* = \sigma(a)$; $\tau : A \to \mathbb{C}$ is a **continuous $\sigma$-invariant trace**, $\tau(xy) = \tau(yx)$ and $\tau(\sigma(x)) = \tau(x)$, whose **trace pairing**

$$
\{x,y\} = \tau\bigl(x\,\sigma(y)\bigr) , \qquad x,y \in A ,
$$

is **nondegenerate** — this is the **form of the category**; $B(A)$ is the unital Banach algebra of bounded operators; $L_a(x) = ax$ and $R_b(x) = xb$; an operator $T \in B(A)$ is **adjointable** when there is $T^\dagger$ with $\{Tx,y\} = \{x,T^\dagger y\}$ for all $x,y$; and $\mathcal{A}(A)\subseteq B(A)$ is the set of adjointable operators.

## The Form of the Category

**Proposition (the form is sesquilinear and symmetric).** The trace pairing is conjugate-linear in the second variable, linear in the first, and

$$
\{x,y\} = \overline{\{y,x\}} , \qquad \{\sigma(x),\sigma(y)\} = \overline{\{x,y\}} ,
$$

and it is nondegenerate by hypothesis; it is the twisted pairing $\{x,y\} = \langle x,\sigma(y)\rangle$ of the plain pairing $\langle x,y\rangle = \tau(xy)$.

**Proof.** Conjugate-linearity in the second variable is the conjugate-linearity of $\sigma$ and the linearity of $\tau$; for symmetry, $\overline{\{y,x\}} = \overline{\tau(y\sigma(x))} = \tau(\sigma(y\sigma(x))) = \tau(x\sigma(y)) = \{x,y\}$, using the $\sigma$-invariance of $\tau$ and $\sigma(y\sigma(x)) = x\sigma(y)$; the last identity is the definition of the twisted pairing. $\square$

**Remark (the $\mathrm{C}^*$-specialisation).** When $A$ is a $\mathrm{C}^*$-algebra of operators on a Hilbert space $H$ with the trace class and $\tau$ the Hilbert–Schmidt trace, the form of the category is the Hilbert–Schmidt inner product $\{x,y\} = \operatorname{tr}(x y^*)$, and the adjoint of an operator is the usual Hilbert-space adjoint; the trace pairing is then positive definite and the theory of this article is the operator theory of *Operator Algebras* read through the form.

## The Adjoint

**Theorem (existence, uniqueness and the elementary laws).** Let $T \in B(A)$ be adjointable. Then $T^\dagger$ is unique, and the assignment $T \mapsto T^\dagger$ is additive, conjugate-linear when the scalar twist is present, involutive and anti-multiplicative:

$$
(S + T)^\dagger = S^\dagger + T^\dagger , \qquad (ST)^\dagger = T^\dagger S^\dagger , \qquad (T^\dagger)^\dagger = T , \qquad (\lambda T)^\dagger = \bar\lambda\,T^\dagger .
$$

Hence the adjoint is an anti-automorphism of the algebra $\mathcal{A}(A)$ of order two, an isomorphism $\mathcal{A}(A) \to \mathcal{A}(A)^{\mathrm{op}}$, and the adjointable operators form a subalgebra of $B(A)$.

**Proof.** Uniqueness and additivity are the nondegeneracy of the form: $\{x,(S+T)^\dagger y\} = \{(S+T)x,y\} = \{Sx,y\} + \{Tx,y\} = \{x,S^\dagger y\} + \{x,T^\dagger y\}$, and the form is conjugate-linear in the second argument. For the product, $\{x,(ST)^\dagger y\} = \{STx,y\} = \{Tx,S^\dagger y\} = \{x,T^\dagger S^\dagger y\}$. The order two is $\{x,Ty\} = \{T^\dagger x,y\} = \{x,(T^\dagger)^\dagger y\}$, and the compatibility with the scalars is the conjugation. $\square$

**Theorem (self-adjoint and skew operators).** An operator $T$ is **self-adjoint** when $T^\dagger = T$ and **skew** when $T^\dagger = -T$; the self-adjoint operators form a real linear subspace and the skew operators the real subspace $i\mathcal{A}(A)^+$; every adjointable $T$ decomposes as

$$
T = \tfrac12(T + T^\dagger) + \tfrac12(T - T^\dagger) ,
$$

and the self-adjoint and the skew operators are closed when the adjoint is continuous. The self-adjoint operators are exactly the operators fixed by the involution, and they are the analogue in $\mathcal{A}(A)$ of the self-adjoint elements of $A$.

**Proof.** The decomposition is formal and the parts are self-adjoint and skew by the involutivity and conjugate-linearity; closedness is the closedness of the fixed set of a continuous map, the adjoint being continuous for the topology of bounded convergence when $\sigma$ and $\tau$ are. $\square$

**Theorem (the left regular representation is a `*`-representation).** The left and right multiplications are adjointable, with

$$
(L_a)^\dagger = L_{\sigma(a)} , \qquad (R_b)^\dagger = R_{\sigma(b)} ,
$$

and the map $a \mapsto L_a$ is a `*`-representation of $(A,\sigma)$ in $\mathcal{A}(A)$: $L_{ab} = L_aL_b$, $L_{a^*} = (L_a)^\dagger$. Hence the involution of the elements and the adjoint of the operators agree on the image of the regular representation, an agreement proved and not assumed.

**Proof.** $\{L_ax,y\} = \tau(ax\sigma(y)) = \tau(x\sigma(y)a) = \tau(x\sigma(\sigma(a)y)) = \{x,L_{\sigma(a)}y\}$ by the cyclicity of $\tau$ and $\sigma^2 = \mathrm{id}$; the right-handed computation is the mirror. Multiplicativity is associativity and the adjoint formula is the computation. $\square$

## The Adjointable Operators

**Proposition (closure and completion).** The adjointable operators form a subalgebra $\mathcal{A}(A)$ of $B(A)$, closed under the adjoint; it is a closed subalgebra when the adjoint is continuous, and it is complete when $B(A)$ is, so the involution descends to the completion of $\mathcal{A}(A)$. The adjoint is continuous for the topology of bounded convergence.

**Proof.** Closure under products, sums and the adjoint is the theorem; the adjoint map $T \mapsto T^\dagger$ is the composite of the transpose with the form, continuous when the form is continuous and nondegenerate, and a closed $\dagger$-stable subalgebra is complete after completion with its involution extended by continuity. $\square$

**Example (the matrix algebra).** For $A = M_n(\mathbb{C})$ with $\sigma$ the conjugate transpose and $\tau$ the trace, the trace pairing is the Hilbert–Schmidt inner product, the adjoint of an operator $T$ on $M_n$ is the Hilbert–Schmidt adjoint, and the self-adjoint operators are the operators fixed by it; the left regular representation is the `*`-representation of $M_n$ on itself.

**Example (the group algebra).** For the group algebra of a finite group with $\tau(\sum a_g u_g) = a_1$ and the involution $u_g^* = u_{g^{-1}}$, the trace pairing is nondegenerate and the adjoint of the left multiplication by a group element is the left multiplication by its inverse. The trace pairing is the base of the operator theory of the group algebra, *Group Algebras*.

## The Transpose, the Form and the Matrix Model

**Definition.** An operator $T$ has a **transpose** $T^{\mathsf t}$ relative to the plain pairing $\langle x,y\rangle = \tau(xy)$ when $\langle Tx,y\rangle = \langle x,T^{\mathsf t}y\rangle$; the adjoint is then the twist of the transpose by the involution.

**Proposition (transpose and adjoint).** If $T$ has a transpose $T^{\mathsf t}$ then $T$ is adjointable and

$$
T^\dagger = \sigma\,T^{\mathsf t}\,\sigma ,
$$

so the adjoint is the transpose conjugated by the involution; the transpose is linear and multiplicative, $(ST)^{\mathsf t} = T^{\mathsf t}S^{\mathsf t}$, and the adjoint inherits its anti-multiplicativity through the twist.

**Proof.** $\{Tx,y\} = \tau(Tx\,\sigma(y)) = \langle Tx,\sigma(y)\rangle = \langle x,T^{\mathsf t}\sigma(y)\rangle = \tau(x\,T^{\mathsf t}\sigma(y))$; and $\{x,\sigma(T^{\mathsf t}\sigma(y))\} = \tau(x\,\sigma(\sigma(T^{\mathsf t}\sigma(y)))) = \tau(x\,T^{\mathsf t}\sigma(y))$, so $T^\dagger = \sigma T^{\mathsf t}\sigma$. The multiplicativity of the transpose is the associativity of the product, and the twist by the anti-automorphism $\sigma$ reverses the order, giving the anti-multiplicativity of the adjoint. $\square$

**Example (the matrix model).** For $A = M_n(\mathbb{C})$ with $\sigma$ the conjugate transpose and $\tau$ the trace, the plain pairing is $\langle X,Y\rangle = \operatorname{tr}(XY)$ and the transpose of an operator is the ordinary matrix transpose of the operator on the matrix space; the adjoint is its conjugate transpose, and the two coincide for real matrices.

## Summary

The form of the category of the operator theory on a Banach algebra $A$ with a continuous involution $\sigma$ and a continuous $\sigma$-invariant trace $\tau$ is the trace pairing $\{x,y\} = \tau(x\sigma(y))$, nondegenerate by hypothesis and sesquilinear; it defines the adjoint $T^\dagger$ by $\{Tx,y\} = \{x,T^\dagger y\}$. The adjoint is unique, additive, conjugate-linear and anti-multiplicative, $(ST)^\dagger = T^\dagger S^\dagger$ and $(T^\dagger)^\dagger = T$, so it is an order-two anti-automorphism of the algebra of adjointable operators, an isomorphism onto its opposite; the self-adjoint ($T^\dagger = T$) and skew ($T^\dagger = -T$) operators are real subspaces of the adjointable operators, closed when the adjoint is continuous, and every adjointable operator is their average. The left and right multiplications are adjointable with $(L_a)^\dagger = L_{\sigma(a)}$ and $(R_b)^\dagger = R_{\sigma(b)}$, so the left regular representation is a `*`-representation, and the adjointable operators form a closed subalgebra that is complete with $B(A)$. The signed, reflection and graded adjoints are the articles that follow.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A$, $\sigma$, $a^* = \sigma(a)$ | Banach algebra with a continuous involution |
| $\tau$, $\tau(xy) = \tau(yx) = \tau(\sigma(x))$ | Continuous $\sigma$-invariant trace |
| $\{x,y\} = \tau(x\sigma(y))$ | The form of the category (trace pairing), nondegenerate |
| $T^\dagger$, $\{Tx,y\} = \{x,T^\dagger y\}$ | The adjoint of an operator |
| $(ST)^\dagger = T^\dagger S^\dagger$, $(T^\dagger)^\dagger = T$ | Anti-multiplicativity and order two |
| $T^\dagger = T$, $T^\dagger = -T$ | Self-adjoint and skew operators |
| $\mathcal{A}(A)$ | The adjointable operators, a closed subalgebra |
| $(L_a)^\dagger = L_{\sigma(a)}$ | The regular representation is a `*`-representation |
| $T^{\mathsf t}$, $T^\dagger = \sigma T^{\mathsf t}\sigma$ | Transpose for the plain pairing; the adjoint |

## Further Reading

- Charles E. Rickart, *General Theory of Banach Algebras* (Van Nostrand, 1960), for the operators of a Banach algebra and the adjoints with respect to a form.
- Theodore W. Palmer, *Banach Algebras and the General Theory of ${}^*$-Algebras, Volume II* (Cambridge University Press, 2001), for the involutive Banach algebras and the operator involution.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume I* (Academic Press, 1983), for the Hilbert-space adjoint and the self-adjoint and skew operators.
- F. R. Gantmacher, *The Theory of Matrices, Volume I* (Chelsea, 1959), for the trace form, the adjoint of an operator and the Kronecker structure.
- Béla Bollobás, *Linear Analysis* (Cambridge University Press, second edition, 1999), for the bounded operators, the topologies and the completeness of the operator algebra.
