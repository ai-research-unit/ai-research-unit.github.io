
# __The Signed Left Multiplication on a Topological Vector Space__

## Introduction

The one-sided companion of the signed sandwich is the **signed left multiplication** $\Lambda^{\alpha}_{a} = L_{a} \circ \alpha$, the operator $x \mapsto a\alpha(x)$ on the algebra, obtained from the signed sandwich by taking the right factor to be the identity. It is the composite of the ordinary left multiplication with the grade involution, so the product of two signed left multiplications is an ordinary left multiplication, the set of signed and ordinary left multiplications is closed under composition, the inverse of an invertible signed left multiplication is again of the same kind with the parameter imaged by the grade involution, and the elements it fixes are computed from the equation $a\alpha(x) = x$. This article develops the signed left multiplication, its continuity, its composition laws, its relation to the unsigned one, and the fixed set.

The unsigned left and right multiplications and their laws are *The Left and Right Multiplication Operators on a Topological Vector Space*; the signed sandwich, of which this operator is the case $b = 1$, is *The Signed Sandwich on a Topological Vector Space*; the reflections it produces for involutive parameters are *Reflections as Signed Two-Sided Operators on a Topological Vector Space*; the pairing-based adjoint is *The Signed Adjoint of the Left Multiplication on a Topological Vector Space*; the module-level variant is *The Graded Action on a Module over a Topological Vector Space*. The linear-space sibling in Part I is *The Signed Left Multiplication on a Linear Space*. No form and no involution on the elements is used here.

Throughout, $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$, $E$ is an associative unital topological algebra over $\mathbb{K}$ with a jointly continuous multiplication, $\mathcal{L}(E)$ is its operator algebra, $\alpha$ is a continuous grade involution with $\alpha^{2} = \mathrm{id}$, and $L_{a}(x) = ax$, $R_{a}(x) = xa$ are the one-sided multiplications. The **signed left multiplication** is

$$
\Lambda^{\alpha}_{a} = L_{a} \circ \alpha, \qquad \Lambda^{\alpha}_{a}(x) = a\,\alpha(x) .
$$

## The Signed Left Multiplication

**Proposition (definition and continuity).** For every $a \in E$ the map $\Lambda^{\alpha}_{a}$ is a continuous linear operator on $E$; it is the signed sandwich with the right factor equal to the identity, $\Lambda^{\alpha}_{a} = \Theta^{\alpha}_{a,1}$, and

$$
\Lambda^{\alpha}_{a} = L_{a} \circ \alpha = \alpha \circ L_{\alpha(a)} ,
$$

so the signed left multiplication is the ordinary left multiplication by $\alpha(a)$ conjugated by $\alpha$.

**Proof.** $\Lambda^{\alpha}_{a}$ is a composite of continuous linear maps, hence continuous linear. The first identity is the definition of the sandwich with $b = 1$; for the second, $(\alpha \circ L_{\alpha(a)})(x) = \alpha(\alpha(a)x) = a\alpha(x) = \Lambda^{\alpha}_{a}(x)$.

**Proposition (composition).** For all $a, b \in E$,

$$
\Lambda^{\alpha}_{a}\Lambda^{\alpha}_{b} = L_{a\alpha(b)}, \qquad
L_{a}\Lambda^{\alpha}_{b} = \Lambda^{\alpha}_{ab}, \qquad
\Lambda^{\alpha}_{a}L_{b} = R_{\alpha(b)}\Lambda^{\alpha}_{a} .
$$

In particular the composite of two signed left multiplications is an ordinary left multiplication, and the set $\{L_{a} : a \in E\} \cup \{\Lambda^{\alpha}_{a} : a \in E\}$ is closed under composition.

**Proof.** $\Lambda^{\alpha}_{a}\Lambda^{\alpha}_{b}(x) = a\alpha(b\alpha(x)) = a\alpha(b)\alpha(\alpha(x)) = a\alpha(b)x = L_{a\alpha(b)}(x)$; $L_{a}\Lambda^{\alpha}_{b}(x) = ab\alpha(x) = \Lambda^{\alpha}_{ab}(x)$; $\Lambda^{\alpha}_{a}L_{b}(x) = a\alpha(x)\alpha(b) = R_{\alpha(b)}(\Lambda^{\alpha}_{a}(x))$. Closure is the three identities together.

**Proposition (invertibility).** The signed left multiplication $\Lambda^{\alpha}_{a}$ is invertible in $\mathcal{L}(E)$ if and only if $a$ is invertible in $E$, and then

$$
(\Lambda^{\alpha}_{a})^{-1} = \Lambda^{\alpha}_{\alpha(a)^{-1}} = \Lambda^{\alpha}_{\alpha(a^{-1})} .
$$

The set of invertible signed left multiplications is a group under composition isomorphic to $E^{\times}$.

**Proof.** If $a$ is invertible then $\Lambda^{\alpha}_{\alpha(a)^{-1}}\Lambda^{\alpha}_{a} = L_{\alpha(a)^{-1}\alpha(a)} = L_{1} = \mathrm{id}$ and likewise on the other side, using the composition law. Conversely, if $\Lambda^{\alpha}_{a}$ is invertible then $L_{a} = \Lambda^{\alpha}_{a}\alpha^{-1}$ is invertible as a composite of invertible maps, and a left multiplication $L_{a}$ is invertible exactly when $a$ is a unit, by the one-sided invertibility argument of the sandwich article; hence $a$ is invertible. The group statement is that $a \mapsto \Lambda^{\alpha}_{a}$ is a bijection onto the set of signed left multiplications with $\Lambda^{\alpha}_{a}\Lambda^{\alpha}_{b} = L_{a\alpha(b)}$, which is the twisted multiplication.

## The Fixed Elements

**Definition.** The **fixed set** of the signed left multiplication is

$$
\mathrm{Fix}(\Lambda^{\alpha}_{a}) = \{x \in E : a\alpha(x) = x\} .
$$

**Proposition (the fixed set is a closed affine set).** $\mathrm{Fix}(\Lambda^{\alpha}_{a})$ is closed; it is the preimage of $0$ under the continuous map $x \mapsto a\alpha(x) - x$, and it is a subspace exactly when $0$ is fixed, that is when $a\alpha(0) = 0$, which always holds; consequently the fixed set is a closed subspace of $E$.

**Proof.** The fixed set is the kernel of the continuous linear map $\mathrm{id} - \Lambda^{\alpha}_{a}$, hence a closed subspace; the apparent linearity is correct because $\Lambda^{\alpha}_{a}$ is linear and fixes $0$.

**Proposition (the fixed set in the invertible case).** If $a$ is invertible then $\mathrm{Fix}(\Lambda^{\alpha}_{a}) = \{x : \alpha(x) = a^{-1}x\}$, the graph of the action of $a^{-1}$ under the involution, and its dimension equals the dimension of the fixed points of the automorphism $a^{-1}\alpha$ of $E$, namely

$$
\dim \mathrm{Fix}(\Lambda^{\alpha}_{a}) = \dim\ker(\mathrm{id} - a^{-1}\alpha) .
$$

For $a = 1$ the fixed set of $\Lambda^{\alpha}_{1} = \alpha$ is the fixed part $E^{+}$ of the grading, and $\Lambda^{\alpha}_{1}$ is an involution with $E = E^{+} \oplus E^{-}$.

**Proof.** $a\alpha(x) = x$ is $\alpha(x) = a^{-1}x$ when $a$ is invertible, and the fixed points of the automorphism $a^{-1}\alpha$ are the kernel of $\mathrm{id} - a^{-1}\alpha$; the finite-dimensional dimension statement follows. For $a = 1$ the equation is $\alpha(x) = x$, i.e. $x \in E^{+}$, and $\Lambda^{\alpha}_{1} = \alpha$ with the splitting of the reflection article.

**Corollary (the fixed set of the sandwich).** The signed sandwich $\Theta^{\alpha}_{a,b}$ fixes $x$ exactly when $a\alpha(x)b = x$; for invertible $a, b$ this is $\alpha(x) = a^{-1}xb^{-1}$, and the fixed set is the set of points of $E$ mapped to themselves by the automorphism $x \mapsto a^{-1}xb^{-1}$ composed with $\alpha$.

**Proof.** Immediate from the definition and the invertibility of the factors.

## Examples

**Example (the matrix algebra).** On $E = M_{n}(\mathbb{K})$ with $\alpha(X) = TXT$ for $T = \mathrm{diag}(1, -1, \dots, -1)$ the signed left multiplication $\Lambda^{\alpha}_{A}(X) = ATXT$ acts by $X \mapsto A(TXT)$; its fixed set is the set of $X$ with $ATXT = X$, which for invertible $A$ is the fixed space of the linear map $X \mapsto T A^{-1} X T$; when $A = 1$ the fixed set is the space of matrices commuting with $T$ in the graded sense.

**Example (the operator algebra).** On $E = \mathcal{L}(F)$ with $\alpha(A) = TAT$ the signed left multiplication by $A$ is $\Lambda^{\alpha}_{A}(X) = ATXT$; on the fixed part of the grading it is $AX$, on the negated part $-AX$, so it is the left multiplication with a sign depending on the parity of the argument. This is the one-sided instance of the signed sandwich on the operator algebra.

**Example (the commutative case).** On $E = C(K)$ with $\alpha(f) = f \circ \sigma$ and $a = g$ the signed left multiplication is $\Lambda^{\alpha}_{g}(f) = g\,(f \circ \sigma)$, the multiplication operator by $g$ composed with the reflection of the commutative algebra; its fixed set is $\{f : g (f \circ \sigma) = f\}$.

## Summary

On a unital topological algebra $E$ with a continuous grade involution $\alpha$ the signed left multiplication $\Lambda^{\alpha}_{a} = L_{a}\alpha$, $\Lambda^{\alpha}_{a}(x) = a\alpha(x)$, is a continuous operator, it is the signed sandwich with right factor one, and it equals $\alpha L_{\alpha(a)}$; two of them compose by $\Lambda^{\alpha}_{a}\Lambda^{\alpha}_{b} = L_{a\alpha(b)}$ into an ordinary left multiplication, mixed products give $\Lambda^{\alpha}_{ab}$ and $R_{\alpha(b)}\Lambda^{\alpha}_{a}$, and the set of signed and ordinary left multiplications is closed under composition. It is invertible exactly when $a$ is, with inverse $\Lambda^{\alpha}_{\alpha(a)^{-1}}$, and the invertible ones form a group isomorphic to $E^{\times}$ with the twisted multiplication. Its fixed set is the closed subspace $\{x : a\alpha(x) = x\}$, which for invertible $a$ is the fixed space of the automorphism $a^{-1}\alpha$, and for $a = 1$ is the fixed part $E^{+}$ of the grading; the fixed set of the general signed sandwich is the analogous set of solutions of $a\alpha(x)b = x$. The signed adjoint and the self-adjointness criterion of these one-sided operators are *The Signed Adjoint of the Left Multiplication on a Topological Vector Space*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Lambda^{\alpha}_{a} = L_{a}\alpha$ | Signed left multiplication, $x \mapsto a\alpha(x)$ |
| $\Lambda^{\alpha}_{a} = \Theta^{\alpha}_{a,1} = \alpha L_{\alpha(a)}$ | Sandwich and conjugate forms |
| $\Lambda^{\alpha}_{a}\Lambda^{\alpha}_{b} = L_{a\alpha(b)}$ | Composition law |
| $(\Lambda^{\alpha}_{a})^{-1} = \Lambda^{\alpha}_{\alpha(a)^{-1}}$ | Inverse |
| $\mathrm{Fix}(\Lambda^{\alpha}_{a}) = \{x : a\alpha(x) = x\}$ | Fixed subspace, closed |
| $a^{-1}\alpha$ | Automorphism whose fixed space is the fixed set, for invertible $a$ |
| $E^{+}$ | Fixed part of $\alpha$, the case $a = 1$ |

## Further Reading

- Nicolas Bourbaki, *Topological Vector Spaces, Chapters 1–5* (Springer, 1987), for the left and right multiplications and the involutive automorphisms of a topological algebra.
- Helmut H. Schaefer and Manfred P. Wolff, *Topological Vector Spaces* (Springer, second edition, 1999), for the one-sided operators and the fixed-point subspaces.
- Charles E. Rickart, *General Theory of Banach Algebras* (Van Nostrand, 1960), for the one-sided multiplications and their groups.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras I* (Academic Press, 1983), for the one-sided operators on an operator algebra.
- John B. Conway, *A Course in Functional Analysis* (Springer, second edition, 1990), for the multiplication operators and their fixed points.
