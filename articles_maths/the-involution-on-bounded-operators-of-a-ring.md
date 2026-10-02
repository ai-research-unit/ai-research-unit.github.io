
# __The Involution on Bounded Operators of a Ring__

## Introduction

The bounded operators of a topological ring form a topological ring, and a form on the ring turns it into an involutive one: the adjoint $T^\dagger$ defined by $\{Tx,y\} = \{x,T^\dagger y\}$ is additive, reverses the composition and has order two, so that the bounded operators carry an involution of their own, sitting on the operators and distinct from the involution of the elements. This article builds that involution: it fixes the algebra of bounded operators, defines the adjoint with respect to the form of the category, proves that the adjoint map is an order-two anti-automorphism of the operator algebra, identifies the self-adjoint and the skew operators and proves that the self-adjoint operators are closed, and studies the representation $a\mapsto L_a$ of the ring in its operators, proving that it is a `*`-representation — the adjoint of the left multiplication is the left multiplication by the image of the element under the involution — so that the involution of the elements and the involution of the operators agree on the image, the agreement being proved and not assumed.

The article assumes the topological ring, the linear topologies, the topology of bounded convergence and the bounded and continuous operators from *Topological Rings and Fields* and *Operators on a Topological Ring*; the left and right multiplications and the operator layer from *The Left and Right Multiplication Operators on a Topological Ring*; the continuous involution, the fixed and skew sets, the averaging map and the closedness of the fixed set from *Involutive Topological Rings and Fields*; and the trace and the twisted pairing of an involutive ring from *Involutive Rings* and the `- * Theory` articles of this category. The specific pairings — the residue pairing and the Hermitian valuation — are the subjects of *Adjoints under the Residue Pairing* and *The Adjoint under a Hermitian Valuation*; the adjoint of a single elementary operator is *The Adjoint of the Left Multiplication on a Topological Ring*; and the Haar pairing of a locally compact group is Part III, named only.

Throughout, $R$ is a Hausdorff topological ring with a continuous involution $\sigma$, $\tau$ is a continuous $\sigma$-invariant trace, the **form of the category** is the twisted pairing

$$
\{x,y\} = \tau\bigl(x\,\sigma(y)\bigr) ,
$$

$B(R)$ is the algebra of bounded endomorphisms of the additive group of $R$ with the topology of bounded convergence, and the **adjoint** of $T\in B(R)$ is the operator $T^\dagger$ defined by $\{Tx,y\} = \{x,T^\dagger y\}$ for all $x,y$, when it exists and is bounded.

## The Adjoint and the Operator Involution

**Definition.** An operator $T\in B(R)$ is **adjointable** if there is a bounded operator $T^\dagger$ with $\{Tx,y\} = \{x,T^\dagger y\}$ for all $x,y$; the adjointable operators form the subalgebra $B(R,\sigma)$ of $B(R)$.

**Theorem (the adjoint is a continuous operator-algebra involution).** On the adjointable operators the adjoint map $T\mapsto T^\dagger$ is additive, is involutive, $T^{\dagger\dagger} = T$, and reverses the composition,

$$
(ST)^\dagger = T^\dagger S^\dagger ,
$$

so it is an **anti-automorphism of order two** of $B(R,\sigma)$; when the form is continuous in each variable the adjoint map is continuous for the topology of bounded convergence.

**Proof.** Additivity is the bilinearity of the form. Involutivity: $\{Tx,y\} = \{x,T^\dagger y\}$ and, exchanging the roles, $\{T^\dagger x,y\} = \{x,T^\dagger{}^\dagger y\}$; the uniqueness of the adjoint under the nondegeneracy of the form gives $T^{\dagger\dagger} = T$. Anti-multiplicativity: $\{STx,y\} = \{Tx,S^\dagger y\} = \{x,T^\dagger S^\dagger y\}$, so $(ST)^\dagger = T^\dagger S^\dagger$ by uniqueness. Continuity: the adjoint is the operator whose matrix entries are $\{Te_i\text{-coefficients}\}$ read through the form, and continuity of the form makes the assignment $T\mapsto T^\dagger$ continuous in the bounded-convergence topology.

**Proposition (self-adjoint and skew operators).** An operator is **self-adjoint** if $T^\dagger = T$ and **skew** if $T^\dagger = -T$; the self-adjoint operators form a closed additive subspace of $B(R,\sigma)$ and the skew operators a closed additive subspace, and when $2$ is invertible in $B(R,\sigma)$ every operator is the sum of a self-adjoint and a skew one through the continuous averages $\tfrac12(T\pm T^\dagger)$.

**Proof.** The self-adjoint operators are the fixed set of the continuous involution $T\mapsto T^\dagger$ of the operator algebra, hence closed, and additive; the same for the skew set. The decomposition is the averaging of *Involutive Topological Rings and Fields* applied to the operator algebra, which is legitimate because the adjoint map is a continuous involution there by the theorem.

## The Left Regular Representation

**Theorem (the left multiplication is adjointable).** For every $a\in R$ the left multiplication $L_a$ is adjointable with respect to the form of the category, and

$$
(L_a)^\dagger = L_{\sigma(a)} , \qquad (R_b)^\dagger = R_{\sigma(b)} .
$$

Hence $a\mapsto L_a$ is a homomorphism of rings into $B(R,\sigma)$ and the adjoint of $L_a$ is the left multiplication by the image of $a$ under the element involution.

**Proof.** $\{L_a x,y\} = \tau(ax\,\sigma(y)) = \tau(x\,\sigma(y)\,a) = \tau(x\,\sigma(\sigma(a)y)) = \{x, L_{\sigma(a)}y\}$, using the cyclic invariance $\tau(uv) = \tau(vu)$ and $\sigma^2 = \mathrm{id}$. The right-handed computation is the mirror image, and the homomorphism property is $L_{ab} = L_aL_b$.

**Corollary (`*`-representation).** The map $a\mapsto L_a$ satisfies $(L_a)^\dagger = L_{a^{\sigma}}$, where $a^{\sigma} = \sigma(a)$; therefore the left regular representation is a `*`-representation of the involutive ring $(R,\sigma)$ in the involutive operator algebra $(B(R,\sigma),\dagger)$, and the involution of the elements and the involution of the operators agree on the image. The agreement is a theorem, not an assumption: the two structures are the element involution and the operator adjoint, and their coincidence here is what a `*`-representation means.

**Proof.** The formula is the theorem read with $a^\sigma = \sigma(a)$; anticomposition and involutivity are inherited, so the representation preserves both the multiplication and the involution.

**Proposition (fixed and inverted left multiplications).** The left multiplication is self-adjoint exactly when $a$ is self-adjoint, $L_a^\dagger = L_a \iff \sigma(a) = a$; it is unitary exactly when $a$ is unitary and the norm form is central, $L_a^\dagger L_a = \mathrm{id} \iff \sigma(a)a = 1$ with $\sigma(a)a$ central; and it is an involution exactly when $a^2 = 1$.

**Proof.** Self-adjointness: $L_{\sigma(a)} = L_a$ iff $\sigma(a) = a$ by the injectivity of $a\mapsto L_a$ on a ring with a unit. Unitarity: $L_a^\dagger L_a = L_{\sigma(a)a}$, the identity iff $\sigma(a)a = 1$ and the product is central. Involution: $L_a^2 = L_{a^2}$.

## Topological Compatibility

**Theorem (continuity and closedness).** If the multiplication of $R$ is continuous then every left and right multiplication is bounded and continuous; the self-adjoint operators are closed in $B(R,\sigma)$; and the set of adjointable operators is closed in $B(R)$ under the topology of bounded convergence when the form is continuous, so that $B(R,\sigma)$ is a complete involutive topological ring whenever $B(R)$ is complete.

**Proof.** Continuity of $L_a$ and $R_b$ is the continuity of the product; boundedness is that a left multiplication carries a bounded set to a bounded set, by the continuity of the product on a bounded set with a fixed factor. The closedness of the self-adjoint set and the adjointable set is the closed equalizer argument of *Involutive Topological Rings and Fields*, applied to the continuous involution of the operator algebra; completeness passes to the closed subalgebra $B(R,\sigma)$.

**Corollary (the adjoint and the completion).** If $R$ is complete then the operator involution is the restriction of the operator involution of the completion and the self-adjoint bounded operators are the closure of the self-adjoint bounded operators of the original, by *The Involution and the Completion of a Ring* applied to $B(R,\sigma)$.

**Proof.** The completion of $B(R,\sigma)$ is the completion of an involutive topological ring with a continuous involution, and its involution restricts to the given one; the fixed set of the completion is the closure of the fixed set when $2$ is invertible, by the quoted article.

## Examples

**Example (the matrix algebra).** $R = M_n(A)$ over a commutative involutive base, $\sigma$ the transpose, $\tau$ the trace; the form is $\{X,Y\} = \mathrm{tr}(X\,Y^{\mathrm t})$ and the adjoint of $L_X$ is $L_{X^{\mathrm t}}$; the self-adjoint operators are the left multiplications by the symmetric matrices, and $X\mapsto L_X$ is a `*`-representation with the transpose on the elements.

**Example (the group algebra of a finite group).** With the form $B(u,v) = \sum_g u_gv_{\sigma(g)}$ of *The Signed Adjoint of the Left Multiplication on a Topological Group*, the adjoint of $L_a$ is $L_{\sigma(a)}$ and the same `*`-representation holds; the two computations agree because the group algebra is a ring with the involution extended linearly.

**Example (a valued field).** For $R = \mathcal{O}$ with the residue pairing of *Adjoints under the Residue Pairing* the adjoint of $L_a$ is the right multiplication $R_{\sigma(a)}$, showing that a change of form changes the adjoint and that the operator involution is form-dependent, while the element involution is not.

**Example (the degenerate form).** If the form is degenerate, the adjoint need not exist or need not be unique, and the operator involution degenerates into a relation; the article works with the nondegenerate form of the category and notes the degenerate case at the boundary.

## Summary

On the bounded operators of a topological ring with a continuous involution $\sigma$ and a continuous $\sigma$-invariant trace, the form of the category $\{x,y\} = \tau(x\sigma(y))$ defines the adjoint $T^\dagger$ by $\{Tx,y\} = \{x,T^\dagger y\}$; on the adjointable operators the adjoint map is additive, involutive and anti-multiplicative, an order-two anti-automorphism of the operator algebra and continuous for the topology of bounded convergence, so the self-adjoint and the skew operators are closed additive subspaces and, when $2$ is invertible, every operator is the continuous average of a self-adjoint and a skew one. The left and right multiplications are adjointable, with $(L_a)^\dagger = L_{\sigma(a)}$ and $(R_b)^\dagger = R_{\sigma(b)}$, so the left regular representation $a\mapsto L_a$ is a `*`-representation: the involution of the elements and the adjoint of the operators agree on the image, an agreement that is proved and not assumed. The left multiplication is self-adjoint exactly for the self-adjoint elements, unitary exactly for the unitary elements with central norm, and an involution exactly for the involutive elements. The adjointable operators form a closed subalgebra, complete when $B(R)$ is, and the involution passes to the completion. The specialisations to the residue pairing, to the Hermitian valuation and to the signed and reflection operators are the articles that follow.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$, $\sigma$, $\tau$ | Topological ring, continuous involution, $\sigma$-invariant trace |
| $\{x,y\} = \tau(x\sigma(y))$ | The form of the category, the twisted pairing |
| $B(R)$, $B(R,\sigma)$ | Bounded operators; the adjointable ones |
| $T^\dagger$, $\{Tx,y\} = \{x,T^\dagger y\}$ | The adjoint |
| $(ST)^\dagger = T^\dagger S^\dagger$, $T^{\dagger\dagger} = T$ | Anti-automorphism of order two |
| $T^\dagger = T$, $T^\dagger = -T$ | Self-adjoint and skew operators |
| $(L_a)^\dagger = L_{\sigma(a)}$, $(R_b)^\dagger = R_{\sigma(b)}$ | Adjoints of the multiplications |
| $a\mapsto L_a$, $(L_a)^\dagger = L_{a^\sigma}$ | The `*`-representation |
| $a^\sigma = \sigma(a)$ | The element involution carried to the operators |

## Further Reading

- Jacques Dixmier, *Von Neumann Algebras* (North-Holland, 1981), for the adjoint operation on an algebra of operators and the `*`-representation.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume I* (Academic Press, 1983), for the involution of an operator algebra, the self-adjoint and skew operators and the strong and weak topologies.
- Nicolas Bourbaki, *Algebra I*, Chapters 1–3 (Springer, 1998), for the adjoint under a sesquilinear form and the `*`-representation of a ring with involution.
- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the regular representation of a ring with involution and its symmetric elements.
- Seth Warner, *Topological Fields* (North-Holland, 1989), for the topology of bounded convergence and the continuous operators of a topological ring.
