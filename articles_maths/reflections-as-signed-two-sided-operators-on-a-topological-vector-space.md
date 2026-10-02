
# __Reflections as Signed Two-Sided Operators on a Topological Vector Space__

## Introduction

A **reflection** of a topological vector space with a continuous multiplication is an involutive automorphism of the algebra, and reading such an automorphism as a grade involution turns it into a signed two-sided operator: the signed inner sandwich $\Theta^{\alpha_r}_{r,r^{-1}}$ of a reflection $r$ with $\alpha_r = \mathrm{Ad}_r$ is the identity, so the reflection is fixed by its own signed sandwich, and for an arbitrary grade involution the adjoint of the signed inner sandwich of $r$ is the sandwich with the inverse of $\alpha(r)$. The choice of a reflection is the same datum as the choice of a grading of the algebra, and the algebra splits into the fixed part, a subalgebra, and the negated part. This article records the correspondences between reflections, involutive automorphisms and gradings, the trivial action of the signed sandwich of a reflection on itself, and the degenerate cases in which the distinctions collapse.

This article is the topological companion of *Reflections as Signed Two-Sided Operators on a Linear Space* in Part I. The grade involution and its signs are *The Signed Sandwich on a Topological Vector Space*; the one-sided signed operator is *The Signed Left Multiplication on a Topological Vector Space*; the inner automorphisms and the centrality criterion are *The Signed Sandwich on a Topological Vector Space* and *The Left and Right Multiplication Operators on a Topological Vector Space*; the self-adjointness and unitarity of the signed sandwiches belong to *The Signed Adjoint of the Reflection on a Topological Vector Space* and *The Signed Adjoint Sandwich on a Topological Vector Space*. No form and no involution on the elements is used here.

Throughout, $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$, $E$ is an associative unital topological algebra over $\mathbb{K}$ with a jointly continuous multiplication, and $\mathcal{L}(E)$ is its operator algebra. An **involutive automorphism** of $E$ is an algebra automorphism $\alpha$ with $\alpha^{2} = \mathrm{id}$; the **fixed part** and the **negated part** are

$$
E^{+} = \{x : \alpha(x) = x\}, \qquad E^{-} = \{x : \alpha(x) = -x\} .
$$

An element $r$ with $r^{2}$ central (in particular $r^{2} = 1$) is an **involution**, and the inner automorphism $\mathrm{Ad}_{r}(x) = rxr^{-1}$ that it defines is the **reflection** attached to $r$ when $r^{2} = 1$.

## Reflections and Involutive Automorphisms

**Proposition (the correspondence).** Let $\alpha$ be an involutive automorphism of $E$. Then $E^{+}$ is a subalgebra of $E$ containing $1$, the map $x \mapsto (x + \alpha(x))/2$ is a continuous projection onto $E^{+}$ with kernel $E^{-}$ when $2$ is invertible in $\mathbb{K}$, and

$$
E = E^{+} \oplus E^{-}
$$

as a topological direct sum; conversely an algebra grading $E = E_0 \oplus E_1$ with $E_{i}E_{j} \subseteq E_{i+j}$ defines an involutive automorphism, equal to $+1$ on $E_0$ and $-1$ on $E_1$. The two constructions are inverse to one another, so reflections, involutive automorphisms and gradings of $E$ are the same datum.

**Proof.** $\alpha(x + y) = \alpha(x) + \alpha(y)$ and, because $\alpha$ is multiplicative, $\alpha(xy) = \alpha(x)\alpha(y)$, so $E^{+}$ is closed under the product; it contains $1$ because $\alpha(1) = 1$. The averaging map is the projection of the idempotent $(1 + \alpha)/2$ and is continuous because $\alpha$ is; its kernel is $E^{-}$ and the sum is direct since $x = \alpha(x)$ and $x = -\alpha(x)$ force $2x = 0$. The converse is the definition of a grading, and the two constructions are inverse because $\alpha$ is the identity on $E_0$ and minus the identity on $E_1$.

**Proposition (continuity of the reflection and the splitting).** An involutive automorphism $\alpha$ of $E$ carries the fixed part $E^{+}$ onto itself and the negated part $E^{-}$ onto itself, $\alpha(E^{\pm}) = E^{\pm}$; $E^{+}$ is closed when $E$ is Hausdorff and $\alpha$ is continuous, and the direct sum $E = E^{+} \oplus E^{-}$ is topological.

**Proof.** $\alpha(x) = x$ implies $\alpha(\alpha(x)) = x$, and $\alpha(x) = -x$ implies $\alpha(\alpha(x)) = -x$. The fixed part is the kernel of the continuous map $\mathrm{id} - \alpha$, hence closed in a Hausdorff space; the topological direct-sum statement is the proposition above together with the continuity of the averaging projection.

## The Inner Reflections and the Sandwich

**Proposition (the reflection is fixed by its signed sandwich).** Let $r$ be an involution and let $\alpha_r = \mathrm{Ad}_{r}$ be the involutive automorphism it defines. Then

$$
\Theta^{\alpha_r}_{r,r^{-1}} = \mathrm{id} ,
$$

so the signed inner sandwich of a reflection is the identity, and the reflection is fixed and unitary for its own signed sandwich.

**Proof.** $\Theta^{\alpha_r}_{r, r^{-1}}(x) = r\alpha_r(x)r^{-1} = r(rxr^{-1})r^{-1} = x$, using $r^{2} = 1$ and the definition of $\alpha_r$.

**Proposition (the signed sandwich by a reflection).** For an involution $r$ and an arbitrary grade involution $\alpha$,

$$
\Theta^{\alpha}_{r, r^{-1}} = \mathrm{Ad}_{r} \circ \alpha = \alpha \circ \mathrm{Ad}_{\alpha(r)} ,
$$

and the inner sandwich $\Phi_{r, r^{-1}} = \mathrm{Ad}_{r}$ is the reflection itself; the signed sandwich is the composite of the reflection with the grade involution, and it reduces to $\mathrm{Ad}_{r}$ when $\alpha = \mathrm{id}$.

**Proof.** This is the definition $\Theta^{\alpha}_{a,b} = \Phi_{a,b}\alpha$ of the signed sandwich with $\Phi_{r,r^{-1}} = \mathrm{Ad}_{r}$, and the second form is the relation $\Theta^{\alpha}_{a,b} = \alpha\Phi_{\alpha(a),\alpha(b)}$.

**Corollary (the correspondence with the signed inner sandwiches).** The map $r \mapsto \mathrm{Ad}_{r}$ from the involutions of $E$ to the involutive automorphisms is surjective onto the inner ones, with fibres the cosets of the centre; an involutive automorphism is inner exactly when it is $\mathrm{Ad}_{r}$ for some involution $r$, and then the corresponding signed inner sandwich is $\mathrm{Ad}_{r}\alpha$.

**Proof.** An inner automorphism is $\mathrm{Ad}_{r}$ for an invertible $r$, and it is an involution, $\mathrm{Ad}_{r}^{2} = \mathrm{Ad}_{r^{2}} = \mathrm{id}$, exactly when $r^{2}$ is central; normalising $r$ by a central scalar recovers $r^{2} = 1$ when the scalars permit, and the fibre statement is the kernel computation of the regular representation.

## Conjugation and the Degenerate Cases

**Proposition (conjugation of reflections).** For an invertible $u$ and an involutive automorphism $\alpha$, the conjugate $u\alpha u^{-1}$, $x \mapsto u\alpha(u^{-1}xu)u^{-1}$, is an involutive automorphism; if $\alpha = \mathrm{Ad}_{r}$ with $r$ an involution then $u\alpha u^{-1} = \mathrm{Ad}_{uru^{-1}}$ with $uru^{-1}$ again an involution, so the inner reflections form the orbit of $\mathrm{Ad}$ under conjugation by the units. The fixed and negated parts of the conjugate are $uE^{+}$ and $uE^{-}$.

**Proof.** $\alpha^{2} = \mathrm{id}$ gives $(u\alpha u^{-1})^{2} = u\alpha^{2}u^{-1} = \mathrm{id}$, and multiplicativity is preserved by conjugation; if $\alpha = \mathrm{Ad}_{r}$ then $u\mathrm{Ad}_{r}u^{-1}(x) = uru^{-1}xuru^{-1} = \mathrm{Ad}_{uru^{-1}}(x)$, and $(uru^{-1})^{2} = ur^{2}u^{-1} = 1$. The fixed-part statement is the computation $u\alpha u^{-1}(ux) = u\alpha(x)$ for $x \in E^{\pm}$.

**Proposition (the degenerate cases).** A reflection $\alpha$ is the identity exactly when $E^{-} = 0$; it is minus the identity exactly when $E^{+} = 0$, which is impossible when $E$ is unital and $2 \neq 0$; and the two-sided signed sandwich of a reflection with a central involution reduces to the grade involution alone, $\Theta^{\alpha}_{z, z} = z^{2}\alpha = \alpha$ for central $z$ with $z^{2} = 1$. The reflection attached to an involution $r$ is trivial exactly when $r$ is central, in which case $\mathrm{Ad}_{r} = \mathrm{id}$ and the signed internal sandwich is the identity for that reason.

**Proof.** $\alpha = \mathrm{id}$ is $E = E^{+}$, i.e. $E^{-} = 0$; $\alpha = -\mathrm{id}$ is $E = E^{-}$, which would give $1 = -1$ and hence $2 = 0$, excluded. For central $z$, $\Phi_{z,z}(x) = z^{2}x = x$ and $\Theta^{\alpha}_{z,z} = \Phi_{z,z}\alpha = \alpha$. If $r$ is central then $\mathrm{Ad}_{r} = \mathrm{id}$ by the kernel computation, and the converse is that $\mathrm{Ad}_{r} = \mathrm{id}$ iff $r$ is central.

## Examples

**Example (the matrix algebra).** On $E = M_{n}(\mathbb{K})$ an involution is a matrix with $r^{2} = 1$, possibly not diagonalisable, and the reflection is the conjugation $X \mapsto rXr^{-1}$; the fixed part is the centraliser of $r$, the negated part is the $-1$ eigenspace of $\mathrm{Ad}_{r}$, and $\mathrm{Ad}_{r}$ is the identity exactly when $r$ is a scalar matrix.

**Example (the operator algebra with an involutive operator).** Let $F$ be a topological vector space and let $T \in \mathcal{L}(F)$ with $T^{2} = \mathrm{id}$. Then $\alpha(A) = TAT$ is an involutive automorphism of $\mathcal{L}(F)$, the fixed and negated parts are the operators commuting, respectively anticommuting, with $T$ in the appropriate sense, and the signed inner sandwich of $T$ is the identity: $\Theta^{\alpha}_{T,T}(X) = T(TXT)T = X$.

**Example (the commutative case).** On $E = C(K)$ the involution $\alpha(f) = f \circ \sigma$ for a continuous involutive homeomorphism $\sigma$ of $K$ is a reflection, the fixed part is the subalgebra of $\sigma$-invariant functions, and the negated part consists of the functions with $f \circ \sigma = -f$; the signed sandwich $\Theta^{\alpha}_{g,h}(f) = g\,(f \circ \sigma)\,h$ is multiplication by $gh$ composed with the reflection on $f$.

## Summary

A reflection of a unital topological algebra is an involutive continuous automorphism, equivalently a grading $E = E^{+} \oplus E^{-}$ with $E^{+}$ a closed subalgebra and $E^{-}$ the negated part; the two constructions are inverse, so reflections, involutive automorphisms and gradings are the same datum. An involution $r$ with $r^{2} = 1$ defines the inner reflection $\alpha_r = \mathrm{Ad}_{r}$, and the signed inner sandwich of the reflection is the identity, $\Theta^{\alpha_r}_{r,r^{-1}} = \mathrm{id}$, so the reflection is fixed by its own signed sandwich; for an arbitrary grade involution the signed sandwich by a reflection is $\mathrm{Ad}_{r}\alpha = \alpha\mathrm{Ad}_{\alpha(r)}$, the composite of the reflection with the grade involution. The inner reflections are the conjugates of the inner ones and are classified by the involutions modulo the centre, with the trivial case exactly the central involutions; the reflection is the identity only when the negated part vanishes, and minus the identity only when the fixed part vanishes, which the unit forbids. The matrix algebra, the operator algebra with an involutive operator and the commutative algebra $C(K)$ with an involutive homeomorphism are the standard examples. The self-adjointness and the unitarity of these operators with respect to the pairing of the category are *The Signed Adjoint of the Reflection on a Topological Vector Space*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\alpha$, $\alpha^{2} = \mathrm{id}$ | Involutive automorphism, a reflection |
| $E^{+}$, $E^{-}$ | Fixed and negated parts |
| $E = E^{+} \oplus E^{-}$ | Topological direct sum of the grading |
| $r$, $r^{2} = 1$ | Involution of $E$ |
| $\mathrm{Ad}_{r}(x) = rxr^{-1}$ | Inner reflection |
| $\alpha_r = \mathrm{Ad}_{r}$ | Grade involution attached to $r$ |
| $\Theta^{\alpha_r}_{r,r^{-1}} = \mathrm{id}$ | A reflection is fixed by its own signed sandwich |
| $\mathrm{Ad}_{ur} = u\mathrm{Ad}_{r}u^{-1}$ | Conjugation of reflections |
| $Z(E)$ | Centre; inner reflections classified modulo it |

## Further Reading

- Nicolas Bourbaki, *Topological Vector Spaces, Chapters 1–5* (Springer, 1987), for the topological algebras, the involutive automorphisms and the gradings.
- Charles E. Rickart, *General Theory of Banach Algebras* (Van Nostrand, 1960), for the involutive automorphisms, the inner ones and the centralities.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras I* (Academic Press, 1983), for the involutive automorphisms of an operator algebra and the gradings they define.
- Helmut H. Schaefer and Manfred P. Wolff, *Topological Vector Spaces* (Springer, second edition, 1999), for the involutions of a topological vector space and the splitting they induce.
- John B. Conway, *A Course in Functional Analysis* (Springer, second edition, 1990), for the involutions and the two-sided operators.
