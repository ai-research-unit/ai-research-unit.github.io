
# __The Cartan Involution and the Cartan Decomposition__

## Introduction

Let $\mathrm{G}_0$ be a real semisimple Lie algebra with Killing form $\kappa$. A **Cartan involution** is an involution $\mathrm{J}$ of $\mathrm{G}_0$ such that the form

$$
\kappa_\mathrm{J}(x,y)=-\kappa(x,\mathrm{J} y)
$$

is positive definite. The involution splits the algebra into its eigenspaces,

$$
\mathrm{G}_0=\mathrm{K}\oplus\mathrm{P},\qquad \mathrm{K}=\{x:\mathrm{J} x=x\},\qquad \mathrm{P}=\{x:\mathrm{J} x=-x\},
$$

the **Cartan decomposition**; $\mathrm{K}$ is a subalgebra, $\mathrm{P}$ a module over it, and the pair $(\mathrm{G}_0,\mathrm{K})$ is the algebraic model of a symmetric pair. This article is the `- * Theory` entry of the category: it reads the Lie algebra with an involution on its elements, defines the Cartan involution and the Cartan decomposition, establishes the bracket relations, identifies $\mathrm{K}$ as the fixed subalgebra and records its role as the Lie algebra of a maximal compact subgroup, a compactness statement that belongs to a later Part and is named only. The involution as an operator on the algebra, the adjoint of the action and the self-adjointness of the Casimir operator belong to the `- * Operator Theory` group and are deferred; the Killing form is *The Killing Form Operator* and its structure theory is *Structure of Lie Algebras*.

The base is $\mathbb{R}$; the algebra $\mathrm{G}_0$ is finite-dimensional real semisimple, $\kappa$ is its Killing form, and $\mathrm{J}$ is an involution. The article uses the eigenspace decomposition of $\mathrm{J}$ and the bracket only; the definiteness of $\kappa_\mathrm{J}$ is stated as the defining condition, and no length, distance or geometric reading is taken from it.

## The Cartan Involution

**Definition.** An **involution** of a Lie algebra $\mathrm{G}_0$ is an automorphism $\mathrm{J}$ with $\mathrm{J}^2=\mathrm{id}$. A **Cartan involution** is an involution $\mathrm{J}$ of the real semisimple algebra $\mathrm{G}_0$ such that $\kappa_\mathrm{J}(x,y)=-\kappa(x,\mathrm{J} y)$ is positive definite.

**Proposition.** $\kappa_\mathrm{J}$ is a symmetric bilinear form, and it is invariant under $\mathrm{J}$:

$$
\boxed{\;\kappa_\mathrm{J}(\mathrm{J} x,\mathrm{J} y)=\kappa_\mathrm{J}(x,y),\qquad \kappa_\mathrm{J}(\mathrm{J} x,y)=\kappa_\mathrm{J}(x,\mathrm{J} y)\;}.
$$

**Proof.** Symmetry follows from the symmetry of $\kappa$ and $\mathrm{J}^2=\mathrm{id}$; the invariance under $\mathrm{J}$ is the same computation.

**Proposition.** If $\mathrm{J}$ is a Cartan involution then so is every conjugate $g\mathrm{J} g^{-1}$ by an automorphism $g$ that preserves the form up to the appropriate condition, and the Cartan involution is unique up to conjugacy when $\mathrm{G}_0$ is semisimple: any two differ by an inner automorphism.

**Proof.** The definiteness of $\kappa_\mathrm{J}$ is preserved by the conjugation when $g$ preserves $\kappa$; the uniqueness up to conjugacy is the standard theorem of the theory of real semisimple Lie algebras, recorded in *Real Forms of a Complex Lie Algebra*, and is quoted.

## The Cartan Decomposition

**Theorem.** A Cartan involution $\mathrm{J}$ decomposes the algebra as the direct sum of its two eigenspaces,

$$
\boxed{\;\mathrm{G}_0=\mathrm{K}\oplus\mathrm{P},\qquad \mathrm{J}=\mathrm{id}\text{ on }\mathrm{K},\qquad \mathrm{J}=-\mathrm{id}\text{ on }\mathrm{P}\;},
$$

and the eigenspaces satisfy

$$
\boxed{\;[\mathrm{K},\mathrm{K}]\subseteq\mathrm{K},\qquad [\mathrm{K},\mathrm{P}]\subseteq\mathrm{P},\qquad [\mathrm{P},\mathrm{P}]\subseteq\mathrm{K}\;}.
$$

**Proof.** An involution of a vector space whose square is the identity is diagonalisable with eigenvalues $\pm1$ in characteristic not two, giving the direct sum; the bracket relations follow from applying $\mathrm{J}$ to $[x,y]$, which is an automorphism, and reading the sign according to the degrees of $x$ and $y$.

**Corollary.** $\mathrm{K}$ is a subalgebra of $\mathrm{G}_0$, $\mathrm{P}$ is a $\mathrm{K}$-module under the adjoint action, and the quotient $\mathrm{G}_0/\mathrm{K}$ is identified with $\mathrm{P}$ as a $\mathrm{K}$-module; the pair $(\mathrm{G}_0,\mathrm{K})$ is a **symmetric pair**, and the involution is the one of *Symmetric Pairs of a Lie Algebra*.

**Proposition.** The two summands are the kernels of the projectors $\tfrac12(\mathrm{id}\pm\mathrm{J})$, which are operators of the algebra commuting with the adjoint action; the map $x\mapsto\mathrm{J} x$ is the operator that multiplies $\mathrm{K}$ by $+1$ and $\mathrm{P}$ by $-1$.

**Proof.** The projectors are the standard spectral projectors of a diagonalisable involution, and they commute with every automorphism commuting with $\mathrm{J}$, in particular with the $\operatorname{ad}_x$ for $x$ in $\mathrm{K}$.

### The Brackets and the Symmetric Structure

**Theorem.** The bracket relations of the Cartan decomposition make $\mathrm{G}_0$ a $\mathbb{Z}/2$-graded Lie algebra with the even part $\mathrm{K}$ and the odd part $\mathrm{P}$, and the involution $\mathrm{J}$ is the grade involution of that grading.

**Proof.** The relations $[\mathrm{K},\mathrm{K}]\subseteq\mathrm{K}$, $[\mathrm{K},\mathrm{P}]\subseteq\mathrm{P}$, $[\mathrm{P},\mathrm{P}]\subseteq\mathrm{K}$ are exactly the axioms of a $\mathbb{Z}/2$-graded Lie algebra with even part $\mathrm{K}$, and $\mathrm{J}$ acts by $+1$ on the even part and $-1$ on the odd part, which is the grade involution.

**Corollary.** The symmetric pair $(\mathrm{G}_0,\mathrm{K})$ is the graded Lie algebra of *Graded Lie Algebras with an Involution*, and the structure of the pair is the structure of the grading.

## The Fixed Subalgebra and Maximal Compactness

**Definition.** The **fixed subalgebra** of the Cartan involution is $\mathrm{K}=\ker(\mathrm{J}-\mathrm{id})$, called the **maximal compact subalgebra** of $\mathrm{G}_0$.

**Proposition.** $\mathrm{K}$ is the largest subalgebra of $\mathrm{G}_0$ on which $\mathrm{J}$ acts as the identity, and it is a reductive subalgebra: its Killing form is the restriction of $\kappa$ up to the factor and its centre is contained in the centre of $\mathrm{K}$.

**Proof.** The fixed set of an automorphism is a subalgebra, and it is the largest on which the automorphism is the identity; the reductive statement is the standard property of the fixed algebra of a Cartan involution, recorded in *Real Forms of a Complex Lie Algebra*.

**Remark (forward reference).** The name *compact* records that $\mathrm{K}$ is the Lie algebra of a maximal compact subgroup of the adjoint group of $\mathrm{G}_0$; the compactness of that subgroup is a group-theoretic and topological condition, treated with the Lie groups, and is named here only. The Cartan decomposition is the algebraic shadow of the decomposition of a semisimple Lie group into a compact subgroup and a subspace, and the group statement is deferred.

## Worked Case: $\mathrm{sl}(2,\mathbb{R})$

Let $\mathrm{G}_0=\mathrm{sl}(2,\mathbb{R})$ with basis $e,h,f$ and $[h,e]=2e$, $[h,f]=-2f$, $[e,f]=h$. The Cartan involution is $\mathrm{J}(x)=-x^{t}$, the negative transpose, which fixes

$$
\mathrm{K}=\left\{\begin{pmatrix}0&b\\-b&0\end{pmatrix}\right\}=\langle e-f\rangle,
$$

a one-dimensional algebra, and negates the complementary space $\mathrm{P}=\langle h,\ e+f\rangle$ of dimension two; the pair $(\mathrm{G}_0,\mathrm{K})$ is the symmetric pair of the upper half-plane, whose group theory belongs to a later Part. The form $\kappa_\mathrm{J}(x,y)=-\kappa(x,\mathrm{J} y)$ is positive definite on $\mathrm{G}_0$, as the theory requires; the decomposition is an eigenspace decomposition of the involution and no metric reading is taken.


## Summary

A **Cartan involution** of a real semisimple Lie algebra $\mathrm{G}_0$ is an involution $\mathrm{J}$ with $\kappa_\mathrm{J}(x,y)=-\kappa(x,\mathrm{J} y)$ positive definite; it is unique up to inner automorphisms. Its **Cartan decomposition** $\mathrm{G}_0=\mathrm{K}\oplus\mathrm{P}$ is the eigenspace decomposition for the eigenvalues $+1$ and $-1$, with $\mathrm{K}$ a subalgebra, $\mathrm{P}$ a module over it, and the brackets $[\mathrm{K},\mathrm{K}]\subseteq\mathrm{K}$, $[\mathrm{K},\mathrm{P}]\subseteq\mathrm{P}$, $[\mathrm{P},\mathrm{P}]\subseteq\mathrm{K}$ making $\mathrm{G}_0$ a $\mathbb{Z}/2$-graded Lie algebra whose grade involution is $\mathrm{J}$. The fixed subalgebra $\mathrm{K}$ is the **maximal compact subalgebra**, the Lie algebra of a maximal compact subgroup of the adjoint group, a compactness statement named and deferred to the Lie groups. The pair $(\mathrm{G}_0,\mathrm{K})$ is a symmetric pair, treated in *Symmetric Pairs of a Lie Algebra* and *Graded Lie Algebras with an Involution*. For $\mathrm{sl}(2,\mathbb{R})$ the involution is the negative transpose, $\mathrm{K}$ is one-dimensional and $\mathrm{P}$ two-dimensional. The operator layer of the involution, its adjoints and the Casimir operator under the involution belong to the `- * Operator Theory` group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{G}_0$ | a real semisimple Lie algebra |
| $\kappa$ | the Killing form |
| $\mathrm{J}$ | a Cartan involution |
| $\kappa_\mathrm{J}(x,y)=-\kappa(x,\mathrm{J} y)$ | the associated positive definite form |
| $\mathrm{K}=\ker(\mathrm{J}-\mathrm{id})$ | the fixed subalgebra, the maximal compact subalgebra |
| $\mathrm{P}=\ker(\mathrm{J}+\mathrm{id})$ | the complement |
| $(\mathrm{G}_0,\mathrm{K})$ | the symmetric pair |

## Further Reading

- Sigurdur Helgason, *Differential Geometry, Lie Groups and Symmetric Spaces*, Graduate Studies in Mathematics 34 (American Mathematical Society, 2001), for the Cartan involution and the Cartan decomposition.
- Anthony W. Knapp, *Lie Groups Beyond an Introduction*, Progress in Mathematics 140 (Birkhäuser, 2nd ed. 2002), for the Cartan decomposition and the maximal compact subalgebra.
- Nicolas Bourbaki, *Lie Groups and Lie Algebras*, Chapters 4–6 (Springer, 2002), for involutions and symmetric pairs.
- Jean-Pierre Serre, *Complex Semisimple Lie Algebras* (Springer, 2001), for the real forms and their involutions.
