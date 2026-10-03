
# __Self-Adjoint Operators of a Banach Algebra__

## Introduction

With the form of the category on a Banach algebra $A$, the operator algebra $B(A)$ acquires its own involution, and the operators fixed by it are the **self-adjoint operators**: those $T$ with $\{Tx,y\} = \{x,Ty\}$. When the form is positive definite the algebra of operators is an algebra of operators on a pre-Hilbert space, the adjoint is the Hilbert-space adjoint on the completion, and the self-adjoint operators have the whole spectral theory and order of the self-adjoint operators of a Hilbert space: their spectrum is real, their norm is the spectral radius, and the order they carry, $S \leq T$ iff $\{T-S\,x,x\} \geq 0$ for all $x$, is a partial order invariant under the unitary operators. This article develops the self-adjoint operators of a Banach algebra: their definition, the reality of the spectrum, the order and its invariance, and the Jordan structure of the self-adjoint part.

The article assumes the form of the category, the adjoint, the self-adjoint and skew operators and the adjointable algebra from *The Involution on the Operator Algebra*; the self-adjoint elements, the positive cone and the order of the algebra from *Hermitian and Self-Adjoint Elements of a Banach Algebra*; the reality of the spectrum and the norm formula from *The Spectrum of a Self-Adjoint Element*; the bounded operators, the operator norm, the strong and weak topologies and the self-adjoint operators of a Hilbert space from *Operator Algebras*; and the completeness of the operator algebra from *The Operator Algebra of a Banach Space*. The signed and reflection adjoints are the articles that follow.

Throughout, $A$ is a unital Banach algebra over $\mathbb{C}$ with a continuous involution $\sigma$ and the **form of the category** $\{x,y\} = \tau(x\sigma(y))$ attached to a continuous $\sigma$-invariant trace $\tau$; the form is assumed **positive definite**, $\{x,x\} > 0$ for $x \neq 0$, so that $A$ is a pre-Hilbert space whose completion is a Hilbert space $H$ onto which $A$ embeds; $B(A)$ is the algebra of bounded operators, $T^\dagger$ the adjoint with respect to the form, $\mathcal{A}(A)$ the adjointable operators; an operator is **self-adjoint** when $T^\dagger = T$, **positive** when it is self-adjoint and $\{Tx,x\} \geq 0$ for all $x$, and the **order** is $S \leq T$ iff $T - S$ is positive.

## The Self-Adjoint Operators

**Definition.** An adjointable operator $T$ is **self-adjoint** when $T^\dagger = T$; it is **positive** when it is self-adjoint and $\{Tx,x\} \geq 0$ for every $x \in A$; and the **order** is defined by $S \leq T$ iff $T - S$ is positive.

**Proposition (the pre-Hilbert structure and the embedding).** The form of the category is an inner product on $A$ when positive definite; the completion $H$ is a Hilbert space and the natural inclusion $\iota : A \hookrightarrow H$ is injective with dense image. Every adjointable operator $T$ has a bounded extension to $H$ and its adjoint $T^\dagger$ agrees with the Hilbert-space adjoint; hence $\mathcal{A}(A) \subseteq B(H)$ as a `*`-subalgebra, and the self-adjoint operators of $A$ are exactly the self-adjoint operators of $B(H)$ that preserve $A$.

**Proof.** The form is sesquilinear, conjugate-symmetric and, by hypothesis, positive definite, so it is an inner product; the completion is a Hilbert space and $A$ is dense in it. An adjointable $T$ satisfies $\lvert\{Tx,y\}\rvert \leq \lVert T^\dagger\rVert\lVert x\rVert\lVert y\rVert$ with $\lVert x\rVert = \{x,x\}^{1/2}$, so it is bounded for the pre-Hilbert norm and extends; the defining identity $\{Tx,y\} = \{x,T^\dagger y\}$ is the Hilbert-space adjoint identity on the dense subspace, hence on all of $H$. $\square$

**Theorem (reality of the spectrum and the norm).** A self-adjoint operator $T$ has real spectrum and $\lVert T\rVert = r(T)$; a positive operator has $\sigma(T) \subseteq [0,\infty)$ and $\lVert T\rVert$ is the largest point of the spectrum. The self-adjoint operators form a real Banach space closed under the functional calculus of the self-adjoint operators.

**Proof.** The operator $T$ is a self-adjoint bounded operator of the Hilbert space $H$ by the proposition, and the spectral theory of a self-adjoint operator of a Hilbert space gives real spectrum, $\lVert T\rVert = r(T)$ and, for a positive operator, non-negative spectrum; the functional calculus is the operator calculus of *Operator Algebras*. $\square$

## The Order

**Theorem (the order is a partial order).** The relation $S \leq T$ is reflexive, transitive and antisymmetric on the self-adjoint operators; it is invariant under the inner conjugations by the unitary operators and under the adjointable isometries,

$$
S \leq T \;\Longrightarrow\; U^\dagger S U \leq U^\dagger T U \quad (U \text{ unitary}) ,
$$

and the positive operators form a convex cone containing the operators $S^\dagger S$.

**Proof.** Positivity is a convex condition closed under sums and under non-negative scalar multiples, so its associated order is a partial order when the cone is proper, which positive definiteness of the form gives: if $T \geq 0$ and $-T \geq 0$ then $\pm\{Tx,x\} \geq 0$ for all $x$, so $\{Tx,x\} = 0$ and $T = 0$. For invariance, $\{U^\dagger TU\,x,x\} = \{TUx,Ux\}$; and $S^\dagger S \geq 0$ because $\{S^\dagger Sx,x\} = \{Sx,Sx\} \geq 0$. $\square$

**Proposition (the Jordan structure).** The self-adjoint operators form a real **Jordan algebra** under the symmetrised product $S \bullet T = \tfrac12(ST + TS)$, and the positive operators are closed under the Jordan product and the functional calculus; the invertible positive operators form a convex cone in the unit group, and the order is the Loewner order when $A$ is a $\mathrm{C}^*$-algebra of operators.

**Proof.** For self-adjoint $S,T$ the symmetrised product is self-adjoint, and the Jordan identities are the associativity of the operator product read in the symmetrisation; positivity under the symmetrised product and the calculus is the operator statement of the same facts. $\square$

## Examples

**Example (the matrix algebra).** For $A = M_n(\mathbb{C})$ with the Hilbert–Schmidt form, the self-adjoint operators on $M_n$ are the operators fixed by the Hilbert–Schmidt adjoint, the positive ones are the operators sending the positive semidefinite matrices to themselves, and the order is the order of the Hilbert–Schmidt operators; the self-adjoint part is a Jordan algebra of dimension $n^4$.

**Example (the function algebra).** For $A = C(X,\mathbb{C})$ with the form $\{f,g\} = \int_X f\bar g\,d\mu$ for a positive measure $\mu$, the self-adjoint operators are the multiplication operators by real-valued functions together with their Hilbert–Schmidt perturbations; the order is the pointwise order on the multipliers, and the positive operators are the multiplication by non-negative functions.

**Example (the operator algebra).** For $A = B(H)$ with the Hilbert–Schmidt form, the self-adjoint operators are the operators on the Hilbert–Schmidt space fixed by the Hilbert–Schmidt adjoint; they include all the left and right multiplications by self-adjoint operators of $B(H)$, and the order restricts to the Loewner order on those.

## Comparison with the Hilbert-Space Case

**Theorem (the $\mathrm{C}^*$ case).** Let $A$ be a $\mathrm{C}^*$-algebra of operators on a Hilbert space and let the form be the Hilbert–Schmidt form $\{x,y\} = \operatorname{tr}(xy^*)$. Then the completion is the Hilbert–Schmidt space, the adjointable operators are the bounded operators on it, and the self-adjoint operators of $A$ are exactly those fixed by the Hilbert–Schmidt adjoint; the order is the Loewner order and the positive operators are the $\dagger$-invariant operators with a non-negative quadratic form.

**Proof.** The form is the Hilbert–Schmidt inner product, so the adjoint is the Hilbert–Schmidt adjoint and the theory of this article applies; positivity and the order are the operator statements of *Operator Algebras*. $\square$

**Proposition (the orders and the norms).** In the Hilbert–Schmidt case the operator norm dominates the form norm on a finite-dimensional $A$, $\lVert T\rVert_2 \leq \sqrt{n}\,\lVert T\rVert$ with $\lVert T\rVert_2 = \{Tx,x\}^{1/2}$ and $n = \dim A$, and $S \leq T$ implies $\lVert S\rVert_2 \leq \lVert T\rVert_2$; the order is invariant under the unitary operators and the positive operators contain the squares $S^\dagger S$.

**Proof.** In finite dimension $\lVert T\rVert_2^2 = \operatorname{tr}(T^*T) \leq \lVert T\rVert^2\operatorname{tr}(1) = n\lVert T\rVert^2$; the monotonicity of the form norm on the positive operators and the invariance of the order are the general statements proved above. $\square$

## Summary

With the form of the category on a Banach algebra $A$ positive definite, the adjointable operators form a `*`-subalgebra of the algebra $B(H)$ of bounded operators on the completion $H$, and the self-adjoint operators of $A$ are the self-adjoint operators of $B(H)$ that preserve $A$. A self-adjoint operator has real spectrum and $\lVert T\rVert = r(T)$, a positive operator has non-negative spectrum, and the order $S \leq T$ iff $T-S$ is positive is a partial order invariant under the unitary operators and under the adjointable isometries; the positive operators contain the squares $S^\dagger S$. The self-adjoint operators form a real Jordan algebra under the symmetrised product, the positive operators are closed under the Jordan product and the functional calculus, and when $A$ is a $\mathrm{C}^*$-algebra the order is the Loewner order. The algebra-side self-adjoint elements and order are *Hermitian and Self-Adjoint Elements of a Banach Algebra*, and the operator spectral theory in full is *Operator Algebras*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\{x,y\} = \tau(x\sigma(y))$ | The form of the category, positive definite here |
| $H$ | The completion of $A$ as a Hilbert space |
| $T^\dagger = T$ | Self-adjoint operator |
| $\{Tx,x\} \geq 0$ | Positive operator |
| $S \leq T$ iff $T-S$ positive | The order (Loewner in the $\mathrm{C}^*$ case) |
| $S\bullet T = \tfrac12(ST+TS)$ | Symmetrised (Jordan) product |
| $S^\dagger S \geq 0$ | Positivity of the squares |
| $\{x,y\} = \operatorname{tr}(xy^*)$ | Hilbert–Schmidt form, the $\mathrm{C}^*$-specialisation |

## Further Reading

- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume I* (Academic Press, 1983), for the self-adjoint operators, the order and the spectral theory.
- Jacques Dixmier, *Von Neumann Algebras* (North-Holland, 1981), for the operator order and the comparison theory.
- Gérard J. Murphy, *$\mathrm{C}^*$-Algebras and Operator Theory* (Academic Press, 1990), for the positive operators and the functional calculus.
- John B. Conway, *A Course in Functional Analysis* (Springer, second edition, 1990), for the self-adjoint operators of a Hilbert space and the Loewner order.
- Paul R. Halmos, *A Hilbert Space Problem Book* (Springer, second edition, 1982), for the operator order and its invariance.
