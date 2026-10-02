
# __The Signed Adjoint of the Left Multiplication on a Topological Ring__

## Introduction

The signed left multiplication is the one-sided operator $\ell_a(x) = a\,\alpha(x)$, the signed sandwich with the right parameter equal to $1$, and its adjoint with respect to the form of the category is again a signed left multiplication, now with the parameter replaced by its image under the twist $\delta = \sigma\alpha$: $\ell_a^\dagger = \ell_{\delta(a)}$. The class of signed one-sided operators is therefore closed under the adjoint, exactly as the class of reflections is, and the self-adjointness, the unitarity and the involutivity of the operator read off three conditions on the parameter, modulo the kernel of the parametrisation, which consists of the units inducing the grade involution. This article computes the adjoint, separates the three conditions, assembles the two-sided signed sandwich from the one-sided operator and its adjoint, and reads the whole thing through the topology.

The article assumes the topological ring and the bounded operators from *Topological Rings and Fields* and *Operators on a Topological Ring*; the signed left and right multiplications, their composition laws, their group and their fixed sets from *The Signed Left Multiplication on a Topological Ring*; the signed sandwich, its adjoint and its composition from *The Signed Adjoint Sandwich on a Topological Ring*; the reflection and its adjoint from *The Signed Adjoint of the Reflection on a Topological Ring*; the involution, the grade involution and the closedness of the fixed set from *Involutive Topological Rings and Fields*; and the operator adjoint and the form of the category from *The Involution on Bounded Operators of a Ring*.

Throughout, $R$ is a Hausdorff topological ring with a continuous involution $\sigma$, a continuous grade involution $\alpha$ commuting with $\sigma$, a continuous trace $\tau$ with $\tau\circ\alpha = \tau$ and the **form of the category** $\{x,y\} = \tau(x\sigma(y))$; $\delta = \sigma\alpha$; the **signed left multiplication** is

$$
\ell_a(x) = a\,\alpha(x) = L_a\alpha = \Sigma^\alpha_{a,1} ,
$$

the **signed right multiplication** is $\varrho_b(x) = \alpha(x)\,b = \alpha R_b = \Sigma^\alpha_{1,b}$, and the kernel of the parametrisation is $K = \{u\in R^\times : c_u = \alpha\}$, the units inducing the grade involution.

## The Adjoint of the Signed Left Multiplication

**Theorem (the explicit form).** With respect to the form of the category,

$$
\ell_a^\dagger = \ell_{\delta(a)} , \qquad \varrho_b^\dagger = \varrho_{\delta(b)} , \qquad \delta = \sigma\alpha ,
$$

so the adjoint of a signed left multiplication is the signed left multiplication by the $\delta$-image of the parameter, and the adjoint operation is an involution on each of the two signed one-sided families.

**Proof.** $\ell_a = L_a\alpha$, so $\ell_a^\dagger = \alpha^\dagger L_a^\dagger = \alpha L_{\sigma(a)}$ by $(L_a)^\dagger = L_{\sigma(a)}$ and $\alpha^\dagger = \alpha$ from $\tau\circ\alpha = \tau$. Applying this to $x$ gives $\alpha(\sigma(a)x) = \alpha(\sigma(a))\,\alpha(x) = \sigma(\alpha(a))\,\alpha(x) = \delta(a)\,\alpha(x) = \ell_{\delta(a)}(x)$. The computation for the signed right multiplication is the mirror image, and the double adjoint is immediate from $\delta^2 = \mathrm{id}$.

**Corollary (the untwisted case).** When $\alpha = \mathrm{id}$ the signed left multiplication is the left multiplication and $\delta = \sigma$; the adjoint is the left multiplication by the image of the parameter under the involution, which is *The Adjoint of the Left Multiplication on a Topological Ring*.

**Proof.** The formula specialises, since $\alpha = \mathrm{id}$ makes $\ell_a = L_a$ and $\delta = \sigma$.

**Corollary (the adjoint of the composition).** With the composition law $\ell_a\ell_b = \ell_{a\alpha(b)}$ of *The Signed Left Multiplication on a Topological Ring*, the adjoint of a product is the product of the adjoints in the reverse order,

$$
(\ell_a\ell_b)^\dagger = \ell_b^\dagger\ell_a^\dagger = \ell_{\delta(b)}\ell_{\delta(a)} = \ell_{\delta(b)\alpha(\delta(a))} ,
$$

and $\alpha(\delta(a)) = \sigma(a)$, so $(\ell_a\ell_b)^\dagger = \ell_{\delta(b)\sigma(a)}$; in the commutative case this is $\ell_{\delta(b\alpha(a))}$, and in general the order in the product is the reverse one.

**Proof.** The anti-multiplicativity of the adjoint gives $(\ell_a\ell_b)^\dagger = \ell_b^\dagger\ell_a^\dagger$, and $\ell_b^\dagger\ell_a^\dagger = \ell_{\delta(b)}\ell_{\delta(a)} = \ell_{\delta(b)\alpha(\delta(a))}$ by the composition law; $\alpha\delta = \delta\alpha$ gives $\alpha(\delta(a)) = \alpha\sigma(\alpha(a)) = \sigma(a)$. The commutative specialisation is $\delta(b)\sigma(a) = \sigma(a)\delta(b) = \delta(b\alpha(a))$.

## Self-Adjointness, Unitarity and Involutivity

**Theorem (the three conditions).** The signed left multiplication satisfies

$$
\ell_a^\dagger = \ell_a \iff \delta(a) = a , \qquad \ell_a^\dagger\ell_a = \mathrm{id} \iff \delta(a)\alpha(a)\in K , \qquad \ell_a^2 = \mathrm{id} \iff a\alpha(a)\in K ,
$$

and when the grade involution is not inner, $K = \{1\}$, so unitarity is $\delta(a)\alpha(a) = 1$ and involutivity is $a\alpha(a) = 1$.

**Proof.** The parametrisation $u\mapsto\ell_u$ is injective: $\ell_u = \ell_v$ means $u\alpha(x) = v\alpha(x)$ for all $x$, and $\alpha$ is surjective, so $u = v$. Hence $\ell_a^\dagger = \ell_{\delta(a)}$ equals $\ell_a$ exactly when $\delta(a) = a$. For unitarity, $\ell_a^\dagger\ell_a = \ell_{\delta(a)}\ell_a = \ell_{\delta(a)\alpha(a)}$, which is the identity exactly when $\delta(a)\alpha(a)\in K$, where $K$ is the set of units $u$ with $\ell_u = \mathrm{id}$; for involutivity, $\ell_a^2 = \ell_{a\alpha(a)}$, which is the identity exactly when $a\alpha(a)\in K$.

**Corollary (the skew case).** The signed left multiplication is skew, $\ell_a^\dagger = -\ell_a$, exactly when $\delta(a) = -a$; a skew signed left multiplication is never unitary.

**Proof.** The first statement is the injectivity of the parametrisation applied to the skew equation; a skew operator $T$ with $-T = T^\dagger$ has $T^\dagger T = -T^2$, which is the identity only under $T^2 = -\mathrm{id}$, incompatible with $T^2 = \mathrm{id}$ except in the degenerate case.

**Remark (the two faces of the involution).** The self-adjoint signed left multiplications are the parameters with $\delta(a) = a$, the Hermitian parameters; the unitary ones are the parameters with $\delta(a)\alpha(a)\in K$; the involutive ones are the parameters with $a\alpha(a)\in K$. The three sets are the one-sided analogues of the three sets of the reflection, and for $K = \{1\}$ they meet in the self-adjoint elements of order two.

## The Fixed Sets and the Generated Group

**Proposition (the fixed set of a signed left multiplication).** The fixed set of $\ell_a$ is the closed set

$$
R^{\ell_a} = \{ x : a\,\alpha(x) = x \} ,
$$

which contains $0$ and is the fixed set of the composite automorphism $\alpha$ when $a = 1$; the self-adjointness of $\ell_a$ makes the fixed set the fixed set of a set of constraints involving $\delta$, and the fixed element $x$ is one with $\alpha(x) = a^{-1}x$.

**Proof.** The equation $a\alpha(x) = x$ defines the fixed set, closed as an equalizer; for $a=1$ it is $R^\alpha$; for a unit $a$ it is $\alpha(x) = a^{-1}x$, from *The Signed Left Multiplication on a Topological Ring*.

**Theorem (the subgroup generated and the adjoint).** The signed left multiplications with unit parameter and the grade involution generate a subgroup of the group of additive automorphisms, in which $\alpha$ acts on the parameters by $\ell_u\mapsto\ell_{\alpha(u)}$ and in which the adjoint acts as an anti-automorphism,

$$
\ell_u^\dagger\ell_v^\dagger = \ell_{\delta(u)}\ell_{\delta(v)} = (\ell_v\ell_u)^\dagger = \ell_{\delta(u)\alpha(\delta(v))} = \ell_{\delta(u)\sigma(v)} ,
$$

so the group is closed under the involution $T\mapsto T^\dagger$ given by the form of the category, and the unitary elements of the group are the signed left multiplications with $\delta(u)\alpha(u)$ in the kernel.

**Proof.** The generators and their relations are from *The Signed Left Multiplication on a Topological Ring*; the anti-automorphism is the anti-multiplicativity of the adjoint together with $\ell^\dagger = \ell\delta$, and the two forms of the product agree because $\alpha(\delta(v)) = \alpha\sigma(\alpha(v)) = \sigma(v)$; the unitary statement is the three-conditions theorem.

## Relation to the Signed Sandwich

**Theorem (the assembly of the sandwich).** The signed sandwich is the composite of a signed left multiplication, a signed right multiplication and the grade involution,

$$
\Sigma^\alpha_{a,b} = \ell_a\circ\varrho_{\alpha(b)}\circ\alpha , \qquad \Sigma^\alpha_{a,b}(x) = a\,\alpha(x)\,b ,
$$

and its adjoint is assembled from the one-sided adjoints and the self-adjointness of the grade involution,

$$
\bigl(\Sigma^\alpha_{a,b}\bigr)^\dagger = \alpha^\dagger\,\varrho_{\alpha(b)}^\dagger\,\ell_a^\dagger = \alpha\,\varrho_{\delta(\alpha(b))}\,\ell_{\delta(a)} ,
$$

which evaluates to $\Sigma^\alpha_{\delta(a),\delta(b)}$, recovering the adjoint of *The Signed Adjoint Sandwich on a Topological Ring* from the one-sided case.

**Proof.** $\ell_a(\varrho_{\alpha(b)}(\alpha(x))) = a\,\alpha(\alpha(\alpha(x))\alpha(b)) = a\,\alpha(x)\,b$ by $\alpha^2 = \mathrm{id}$, giving the assembly. The adjoint is the anti-multiplicative composite with $\alpha^\dagger = \alpha$, $(L_a)^\dagger = L_{\sigma(a)}$ and the mirror for the right; evaluating gives $\delta(a)\alpha(x)\delta(b)$, which is the signed sandwich of the two $\delta$-images.

**Corollary (the one-sided operators are the degenerate sandwiches).** The signed left and right multiplications are the signed sandwiches with one parameter equal to $1$, and the adjoint of a one-sided operator is a one-sided operator, so the one-sided families are closed under the adjoint while the two-sided family is closed up to the twist.

**Proof.** $\ell_a = \Sigma^\alpha_{a,1}$ and $\varrho_b = \Sigma^\alpha_{1,b}$ by the definitions; the adjoint of $\Sigma^\alpha_{a,1}$ is $\Sigma^\alpha_{\delta(a),\delta(1)} = \Sigma^\alpha_{\delta(a),1} = \ell_{\delta(a)}$.

## Topological Compatibility and Examples

**Theorem (continuity and closedness).** The signed left multiplication is bounded and continuous, the adjoint map is continuous in the topology of bounded convergence, and the sets of self-adjoint, unitary and involutive signed left multiplications are closed in the topology of the parameter when $R^\times$ is open.

**Proof.** $\ell_a$ is the composite of the continuous $L_a$ and $\alpha$, hence bounded and continuous; the adjoint map is continuous by *The Involution on Bounded Operators of a Ring*; the three conditions are closed because $\delta$, the middle factor and the composition are continuous and $K$ is closed.

**Example (the matrix ring).** $R = M_n(k)$ with the grade involution $\alpha(A) = A^{\top}$ and the involution the transpose; $\delta = \sigma\alpha = \mathrm{id}$, so $\ell_A^\dagger = \ell_A$ and every signed left multiplication is self-adjoint; the unitary ones satisfy $\alpha(A)A = I$, that is $A^{\top}A = I$, the orthogonal matrices.

**Example (the polynomial ring).** $R = k[x]$ with $f(x)\mapsto f(-x)$ and the identity involution; $\delta = \alpha$ and $\ell_f^\dagger = \ell_{\alpha(f)}$; a signed left multiplication is self-adjoint exactly when $f$ is even, and unitary exactly when $f(-x)f(x) = 1$, that is $f = \pm1$.

**Example (a field with the conjugation).** $R = \mathbb{C}$ with $\sigma$ the conjugation, $\alpha = \mathrm{id}$ and the trace $\tau(Z) = Z + \bar Z$; the form is the real inner product, $\delta = \sigma$, and $\ell_Z^\dagger = \ell_{\bar Z}$; the unitary signed left multiplications are those with $|Z| = 1$, the circle.

**Example (the group algebra).** For $k[G]$ with the form $B(u,v) = \sum_g u_gv_{\sigma(g)}$, the signed left multiplication with parameter $a$ and the adjoint $\ell_{\sigma(a)}$ recover *The Signed Adjoint of the Left Multiplication on a Topological Group* when the group is discrete.

## Summary

The signed left multiplication $\ell_a(x) = a\alpha(x) = \Sigma^\alpha_{a,1}$ has adjoint $\ell_a^\dagger = \ell_{\delta(a)}$ with respect to the form of the category, where $\delta = \sigma\alpha$, and the signed right multiplication has adjoint $\varrho_b^\dagger = \varrho_{\delta(b)}$; the one-sided signed families are therefore closed under the adjoint, and the adjoint is an anti-automorphism of the generated one-sided family. The parametrisation $u\mapsto\ell_u$ is injective, and the operator is self-adjoint exactly when $\delta(a) = a$; it is unitary exactly when $\delta(a)\alpha(a)\in K$ and an involution exactly when $a\alpha(a)\in K$, where $K$ is the set of units inducing the grade involution, trivial when the grade involution is not inner, so that unitarity is then $\delta(a)\alpha(a) = 1$ and involutivity is $a\alpha(a) = 1$. The two-sided signed sandwich is assembled as $\Sigma^\alpha_{a,b} = \ell_a\varrho_{\alpha(b)}\alpha$, and its adjoint is recovered from the one-sided adjoints and the self-adjointness of the grade involution as $\Sigma^\alpha_{\delta(a),\delta(b)}$. Topologically the operators are bounded and continuous, the adjoint map is continuous, and the three sets are closed.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\ell_a(x) = a\alpha(x) = L_a\alpha = \Sigma^\alpha_{a,1}$ | The signed left multiplication |
| $\varrho_b(x) = \alpha(x)b = \alpha R_b = \Sigma^\alpha_{1,b}$ | The signed right multiplication |
| $\delta = \sigma\alpha$ | The twist |
| $\ell_a^\dagger = \ell_{\delta(a)}$, $\varrho_b^\dagger = \varrho_{\delta(b)}$ | The adjoints |
| $\ell_a\ell_b = \ell_{a\alpha(b)}$ | The composition law |
| $K = \{u : c_u = \alpha\}$ | Kernel of the parametrisation |
| $\delta(a) = a$ | Self-adjointness |
| $\delta(a)\alpha(a)\in K$ | Unitarity |
| $a\alpha(a)\in K$ | Involutivity |
| $\Sigma^\alpha_{a,b} = \ell_a\varrho_{\alpha(b)}\alpha$ | Assembly of the sandwich |

## Further Reading

- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the one-sided operators of a ring with involution and the symmetric and unitary elements.
- Nathan Jacobson, *Structure of Rings*, American Mathematical Society Colloquium Publications 37 (1964), for the regular representation and its one-sided operators.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the unitary group and the one-sided operators of an involutive algebra.
- Nicolas Bourbaki, *Algebra I*, Chapters 1–3 (Springer, 1998), for adjoints under a sesquilinear form and the composition of adjoints.
- Seth Warner, *Topological Fields* (North-Holland, 1989), for the continuous one-sided operators and the closed sets of a topological ring.
