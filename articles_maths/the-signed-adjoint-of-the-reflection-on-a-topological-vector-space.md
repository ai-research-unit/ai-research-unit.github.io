
# __The Signed Adjoint of the Reflection on a Topological Vector Space__

## Introduction

A reflection of a topological vector space is a continuous linear involution $r$ whose fixed hyperplane is closed, and read as a signed two-sided operator it carries the grade involution $\alpha_{r}(x) = rxr^{-1}$ that it defines. Its signed inner conjugation acts trivially, $\mathrm{Sd}^{\alpha_{r}}_{r,r^{-1}} = \mathrm{id}$, so the reflection is **self-adjoint and unitary for its own signed structure**; for an arbitrary grade involution $\alpha$ the adjoint of the signed inner conjugation of $r$ is $\mathrm{Sd}^{\alpha}_{\alpha(r)^{-1},\alpha(r)}$, the two-sided operator with the image of $r$, and the two-sided operator is **unitary always** while being **self-adjoint exactly when $\alpha(r) = r$**, the reflection being fixed by the grade involution. The degenerate cases, in which $r = \mathrm{id}$ or the grade involution moves $r$, are recorded and their collapse described.

This article develops the adjoint of a reflection read as a signed operator. The reflection and its fixed hyperplane are *Reflections as Signed Two-Sided Operators on a Topological Vector Space*; the grade involution attached to an involution is *The Signed Two-Sided Operator on a Topological Vector Space*; the adjoint computation of the signed family is *The Signed Adjoint Two-Sided Operator on a Topological Vector Space*, of which this is the case of the inner conjugation; the trace form is *The Adjoint of the Left Multiplication on a Topological Vector Space*. The pairing-based self-adjointness of a reflection — the orthogonal reflection — belongs to Part III. The forms are Part III.

Throughout, $E$ is a Hausdorff locally convex algebra over $\mathbb{K}$ with a unit and jointly continuous multiplication, $\tau$ is a continuous trace and $\langle x, y\rangle = \tau(xy)$ the trace form of the category, assumed non-degenerate, ${}^{\dagger}$ is the trace-adjoint, $r \in E$ is a **reflection**, that is an involution $r^{2} = 1$ with $r \neq 1$ and with the fixed hyperplane of the action closed, $\alpha_{r}(x) = rxr^{-1}$ is the grade involution it defines, $\mathrm{Sd}^{\alpha}_{a,b}(x) = a\alpha(x)b$ is the signed two-sided operator, and $\alpha$ is a trace-preserving grade involution.

## The Inner Conjugation of a Reflection

**Theorem (the reflection is fixed by its own signed inner conjugation).** For a reflection $r$ whose inner conjugation is $\mathrm{Sd}^{\alpha_{r}}_{r,r^{-1}}$ one has

$$
\boxed{\;\mathrm{Sd}^{\alpha_{r}}_{r,r^{-1}} = \mathrm{id}\;} ,
$$

so the reflection is fixed by its own signed two-sided operator; its trace-adjoint is itself,

$$
(\mathrm{Sd}^{\alpha_{r}}_{r,r^{-1}})^{\dagger} = \mathrm{Sd}^{\alpha_{r}}_{r^{-1},r} = \mathrm{id} ,
$$

and the reflection is both self-adjoint and unitary for its own signed structure.

**Proof.** $\mathrm{Sd}^{\alpha_{r}}_{r,r^{-1}}(x) = r\alpha_{r}(x)r^{-1} = r(rxr^{-1})r^{-1} = r^{2}xr^{-2} = x$, using $r^{2} = 1$ and $r^{-1} = r$. The adjoint is $\mathrm{Sd}^{\alpha_{r}}_{\alpha_{r}(r^{-1}),\alpha_{r}(r)} = \mathrm{Sd}^{\alpha_{r}}_{r^{-1},r}$ by *The Signed Adjoint Two-Sided Operator on a Topological Vector Space*, and $\alpha_{r}(r) = rr r^{-1} = r$, so $\mathrm{Sd}^{\alpha_{r}}_{r^{-1},r} = \mathrm{Sd}^{\alpha_{r}}_{r,r^{-1}} = \mathrm{id}$; unitarity is the previous article with $u = \alpha_{r}(r^{-1})\alpha_{r}(r) = r^{-1}r = 1$.

## The Adjoint for an Arbitrary Grade Involution

**Theorem (the adjoint of the signed inner conjugation).** For an arbitrary trace-preserving grade involution $\alpha$ the signed inner conjugation of the reflection has the trace-adjoint

$$
\boxed{\;(\mathrm{Sd}^{\alpha}_{r,r^{-1}})^{\dagger} = \mathrm{Sd}^{\alpha}_{\alpha(r)^{-1},\alpha(r)}\;} ,
$$

the signed two-sided operator with the image of $r$ under the grade involution; the two-sided operator is therefore self-adjoint exactly when $\mathrm{Sd}^{\alpha}_{r,r^{-1}} = \mathrm{Sd}^{\alpha}_{\alpha(r)^{-1},\alpha(r)}$, that is exactly when

$$
\boxed{\;\alpha(r) = r\;} ,
$$

and it is unitary for every $\alpha$.

**Proof.** The adjoint formula is the general computation with $a = r$, $b = r^{-1}$, using $\alpha(r^{-1}) = \alpha(r)^{-1}$. The two such operators have invertible parameters $r$ and $\alpha(r)$, so they are equal exactly when the parameters are equal, $r = \alpha(r)^{-1}$ and $r^{-1} = \alpha(r)$, which for $r^{-1} = r$ is the single condition $\alpha(r) = r$. Unitarity follows from the previous article, $u = \alpha(r^{-1})\alpha(r) = \alpha(r)^{-1}\alpha(r) = 1$ and $w = rr^{-1} = 1$, both central involutions.

**Corollary (self-adjointness and the grade involution).** The signed inner conjugation of a reflection is self-adjoint precisely when the reflection is fixed by the grade involution, $\alpha(r) = r$; in particular it is self-adjoint for $\alpha = \mathrm{id}$ and for $\alpha = \alpha_{r}$, and it fails to be self-adjoint for any grade involution that moves $r$. The two-sided operator is unitary in all these cases, so unitarity is the stable property and self-adjointness the exceptional one.

**Proof.** The theorem gives the criterion; the two cases $\alpha = \mathrm{id}$ and $\alpha = \alpha_{r}$ satisfy it, and a grade involution with $\alpha(r) \neq r$ violates it.

## Degenerate Cases

**Proposition (the trivial reflection).** If $r = 1$ then the inner conjugation is the identity, $\mathrm{Sd}^{\alpha}_{1,1} = \alpha$, and its adjoint is $\mathrm{Sd}^{\alpha}_{1,1} = \alpha$; the reflection is the identity operator, the grade involution coincides with the identity of the algebra, and the whole structure collapses to the algebra with its trace form.

**Proof.** $\mathrm{Sd}^{\alpha}_{1,1}(x) = \alpha(x)$, and the adjoint of $\alpha$ is $\alpha$ by the self-adjointness of the trace-preserving grade involution; every statement above specialises to this case.

**Proposition (the reflection moved by the grade involution).** If $\alpha(r) \neq r$ then the signed inner conjugation is unitary but not self-adjoint; its adjoint is the two-sided operator $\mathrm{Sd}^{\alpha}_{\alpha(r)^{-1},\alpha(r)}$, which differs from $\mathrm{Sd}^{\alpha}_{r,r^{-1}}$, and the defect is given by $\alpha(r)r^{-1}$, the element by which the grade involution moves the reflection. When $\alpha(r) = r^{-1} = r$ the defect is trivial and the reflection is fixed.

**Proof.** The adjoint is the theorem, and the defect $\alpha(r)r^{-1}$ is trivial exactly when $\alpha(r) = r$; the statement is the contrapositive of the self-adjointness criterion.

**Proposition (the failure in characteristic two).** In characteristic two the involution $r$ has $r + 1$ nilpotent, the fixed hyperplane is the kernel of $x \mapsto (r+1)x$, and the reflection is unipotent; the signed inner conjugation is still the identity, but the decomposition of the space into the fixed and the negated parts fails, and the reflection is not diagonalisable, so the two-sided reading is the only available one.

**Proof.** In characteristic two $r - 1 = r + 1$ and $(r+1)^{2} = r^{2} + 1 = 0$, so $r + 1$ is nilpotent; the fixed set is the kernel, which is not a complement of the image, and the grade involution $\alpha_{r}$ is still an involution but the sum decomposition $E = E^{+}\oplus E^{-}$ is unavailable.

## Examples

**Example (the reflection of a linear space).** For $E = \mathrm{End}_F(V)$ with $\operatorname{tr}$ and $r$ an involution of type $(n-1,1)$ the grade involution is $\alpha_{r}(X) = rXr$ and the inner conjugation is the identity; the reflection is self-adjoint and unitary for the trace form, in agreement with the linear-space computation.

**Example (the reflection of a Hermitian space).** For a reflection that is self-adjoint for a form, the grade involution $\alpha_{r}$ is the conjugation by $r$ and the inner conjugation is the identity, so the reflection is self-adjoint for the trace form; the pairing-based self-adjointness with respect to the form is a different operator, and the two coincide only when the form is the trace form, which is Part III.

**Example (a grade involution moving the reflection).** On a graded algebra with grade involution $\alpha$ and a reflection $r$ of odd part, $\alpha(r) = -r \neq r$, so the signed inner conjugation is unitary but not self-adjoint, and its adjoint is the two-sided operator by $-r$; the defect is $\alpha(r)r^{-1} = -r\cdot r = -1$, the central sign of the odd part.

## Summary

A reflection $r$ read as a signed two-sided operator defines the grade involution $\alpha_{r}(x) = rxr^{-1}$ and has inner conjugation $\mathrm{Sd}^{\alpha_{r}}_{r,r^{-1}} = \mathrm{id}$, so it is self-adjoint and unitary for its own signed structure. For an arbitrary trace-preserving grade involution $\alpha$ the adjoint of the signed inner conjugation is $\mathrm{Sd}^{\alpha}_{\alpha(r)^{-1},\alpha(r)}$, the two-sided operator with the image of $r$; the two-sided operator is unitary for every $\alpha$, because both parameters $u = \alpha(r)^{-1}\alpha(r) = 1$ and $w = rr^{-1} = 1$ are central, and it is self-adjoint exactly when $\alpha(r) = r$, the reflection being fixed by the grade involution. The degenerate cases are the trivial reflection $r = 1$, where the two-sided operator is the grade involution itself, and the reflection moved by $\alpha$, where the two-sided operator is unitary but not self-adjoint with defect $\alpha(r)r^{-1}$; in characteristic two the involution is unipotent, the fixed and negated splitting fails, and the two-sided reading is the only one available. The module-level variant of the group is *The Graded Adjoint Action on a Module over a Topological Vector Space*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $r$, $r^{2} = 1$ | reflection, a continuous involution |
| $\alpha_{r}(x) = rxr^{-1}$ | the grade involution of $r$ |
| $\mathrm{Sd}^{\alpha}_{a,b}(x) = a\alpha(x)b$ | signed two-sided operator |
| $\mathrm{Sd}^{\alpha_{r}}_{r,r^{-1}} = \mathrm{id}$ | a reflection is fixed by its own signed two-sided operator |
| $(\mathrm{Sd}^{\alpha}_{r,r^{-1}})^{\dagger} = \mathrm{Sd}^{\alpha}_{\alpha(r)^{-1},\alpha(r)}$ | its adjoint for an arbitrary $\alpha$ |
| $\alpha(r) = r$ | the self-adjointness criterion |
| $u = 1$, $w = 1$ | the unitarity, always |
| $\langle x,y\rangle = \tau(xy)$ | trace form |

## Further Reading

- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras I* (Academic Press, 1983), for the involutions, the reflections and the adjointable operators.
- Serge Lang, *Algebra* (Springer, third edition, 2002), for the reflections, the involutions and the graded structures.
- Gottfried Köthe, *Topological Vector Spaces II* (Springer, 1979), for the involutions of a topological algebra.
- Helmut H. Schaefer and Manfred P. Wolff, *Topological Vector Spaces* (Springer, second edition, 1999), for the topological algebras and the bilinear forms.
- Albrecht Pietsch, *Operator Ideals* (North-Holland, 1980), for the trace functionals and the duality of the trace form.
