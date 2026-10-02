
# __The Graded Adjoint Action on a Module over a Topological Vector Space__

## Introduction

The units of a topological algebra $E$ act on it by conjugation, $x \mapsto axa^{-1}$, and this **adjoint action** is the module-level form of the signed inner sandwich; with respect to the trace form of the category its adjoint is the conjugate action by $a^{-1}$, so the adjoint action is an involutive action in the sense that it intertwines the trace-adjoint with the inversion of the parameter. On a graded algebra the conjugation by a homogeneous element is compatible with the grading: by an even element it preserves the two parts, and by an odd element it preserves them up to the parity, and the elementwise condition for the compatibility is $a^{-1}\alpha(a) \in Z(E)$. On a graded module over $E$ the conjugated action satisfies $\beta\rho_{x} = (-1)^{i}\rho_{x}\beta$ for a homogeneous $x$ of parity $i$, and the sign rule that the graded commutator imposes is the one of the graded category, named here and deferred.

This article develops the adjoint action, its adjoint, and its compatibility with the grading on a module. The adjoint action and its relation to the inner automorphisms are *The Signed Sandwich on a Topological Vector Space*; the trace form and the adjoint of the inner sandwich are *The Adjoint of the Left Multiplication on a Topological Vector Space* and *The Signed Adjoint Sandwich on a Topological Vector Space*; the graded module and the compatible action are *The Graded Action on a Module over a Topological Vector Space*; the sign rule of the graded commutator is *Superalgebras and Graded Structures*. The forms are Part III.

Throughout, $E = E_{0}\oplus E_{1}$ is a graded Hausdorff locally convex algebra over $\mathbb{K}$ with a unit and jointly continuous multiplication, $\alpha$ is the grade involution, $+1$ on $E_{0}$ and $-1$ on $E_{1}$, $M = M_{0}\oplus M_{1}$ is a graded topological module over $E$ with action $\rho_{x}(m) = x\cdot m$ and grade involution $\beta$, $\tau$ is a continuous trace and $\langle x, y\rangle = \tau(xy)$ the trace form of the category, assumed non-degenerate, and ${}^{\dagger}$ is the trace-adjoint. All conjugations are by invertible elements.

## The Adjoint Action and Its Adjoint

**Definition.** The **adjoint action** of an invertible $a \in E$ on $E$ is the inner automorphism

$$
\mathrm{Ad}_{a}(x) = axa^{-1} ,
$$

a continuous algebra automorphism with $\mathrm{Ad}_{a}\mathrm{Ad}_{b} = \mathrm{Ad}_{ab}$ and $\mathrm{Ad}_{a}^{-1} = \mathrm{Ad}_{a^{-1}}$, so that $a \mapsto \mathrm{Ad}_{a}$ is a continuous representation of the unit group $E^{\times}$ with kernel the centre $Z(E)^{\times}$; the image is the group of inner automorphisms.

**Theorem (the adjoint of the adjoint action).** For every invertible $a \in E$ the adjoint action has the trace-adjoint

$$
(\mathrm{Ad}_{a})^{\dagger} = \mathrm{Ad}_{a^{-1}} = (\mathrm{Ad}_{a})^{-1} ,
$$

so the adjoint action is **unitary** for the trace form and the adjoint operation is compatible with the inversion of the parameter; equivalently, $\mathrm{Ad}_{a}$ is an isometry of the trace form.

**Proof.** $\mathrm{Ad}_{a} = \Theta^{\alpha}_{a,a^{-1}}$ with $\alpha = \mathrm{id}$, and the unsigned sandwich has adjoint $\Phi_{a^{-1},a} = \mathrm{Ad}_{a^{-1}}$ by *The Adjoint of the Left Multiplication on a Topological Vector Space*; since $\mathrm{Ad}_{a^{-1}} = (\mathrm{Ad}_{a})^{-1}$ and $(\mathrm{Ad}_{a})^{\dagger}\mathrm{Ad}_{a} = \mathrm{id}$, the action is unitary. Alternatively, $\langle axa^{-1}, y\rangle = \tau(axa^{-1}y) = \tau(xa^{-1}ya) = \langle x, a^{-1}ya\rangle$.

**Proposition (the adjoint action preserves self-adjointness and unitarity).** Conjugation by an invertible element sends the $\dagger$-self-adjoint operators to $\dagger$-self-adjoint operators and the unitary operators to unitary operators of the trace form; for the adjoint action of $a$ the image of the involution is $S \mapsto aSa^{-1}$, and $(aSa^{-1})^{\dagger} = aS^{\dagger}a^{-1}$.

**Proof.** By the theorem $\mathrm{Ad}_{a}$ is an isometry of the trace form; an isometry intertwines the adjoint, $(\mathrm{Ad}_{a}S)^{\dagger} = \mathrm{Ad}_{a}(S^{\dagger})$, because $(\mathrm{Ad}_{a})^{\dagger} = \mathrm{Ad}_{a}^{-1}$; hence $S = S^{\dagger}$ gives $aSa^{-1} = aS^{\dagger}a^{-1}$, and unitarity is preserved by a product of unitaries.

## Compatibility with the Grading

**Theorem (parity of the conjugation).** Let $a$ be invertible and homogeneous of parity $p$, $a \in E_{p}$, and let $x$ be homogeneous of parity $i$. Then $axa^{-1}$ is homogeneous of parity $p + i + p = i$, since $a^{-1}$ has the parity $p$ and $2p = 0$ in the grading group $\mathbb{Z}/2$; hence

$$
\mathrm{Ad}_{a}(E_{i}) \subseteq E_{i} \qquad (i = 0, 1),
$$

so the conjugation by a homogeneous unit preserves the grading, for even and for odd units alike, and it is an automorphism of the graded algebra.

**Proof.** $a \in E_{p}$, $x \in E_{i}$ and $a^{-1} \in E_{p}$ give $axa^{-1} \in E_{p+i+p} = E_{2p+i} = E_{i}$. The two same-parity factors $a$ and $a^{-1}$ cancel their parities, which is why the odd units conjugate within the parts and are not the ones that move them.

**Corollary (the grading-preserving conjugations).** The conjugation by an arbitrary invertible unit $a$ preserves the two parts of the grading exactly when

$$
a^{-1}\alpha(a) \in Z(E) ;
$$

for a homogeneous unit this always holds, because then $a^{-1}\alpha(a) = \pm 1$, so every homogeneous unit conjugates by a graded automorphism, while a general unit need not, and the group of grading-preserving inner automorphisms is the image of the units satisfying the condition modulo the kernel $Z(E)^{\times}$.

**Proof.** $\mathrm{Ad}_{a}$ commutes with the grade involution $\alpha$ iff $a\alpha(x)a^{-1} = \alpha(axa^{-1}) = \alpha(a)\alpha(x)\alpha(a)^{-1}$ for all $x$, that is iff $a^{-1}\alpha(a)$ centralises the image of $\alpha$, which is all of $E$; a homogeneous unit has $\alpha(a) = (-1)^{p}a$, whence the automatic condition.

**Proposition (the adjoint action on the grade involution).** For invertible $a$,

$$
\mathrm{Ad}_{a}\,\alpha = \alpha_{a}\,\alpha , \qquad \alpha_{a}\alpha(x) = a\alpha(x)a^{-1} = \Theta^{\alpha}_{a,a^{-1}}(x) ,
$$

so the conjugate of the grade involution is the signed inner sandwich of $a$; when $a$ is an involution this is the grade involution $\alpha_{a}$ attached to $a$, and the adjoint action of an involution reproduces the reflection's graded structure.

**Proof.** $\mathrm{Ad}_{a}\alpha(x) = a\alpha(x)a^{-1} = \Theta^{\alpha}_{a,a^{-1}}(x)$ is the definition of the signed inner sandwich; for $a^{2} = 1$ it is the grade involution of *Reflections as Signed Two-Sided Operators on a Topological Vector Space*.

## The Module Case and the Sign Rule

**Theorem (the conjugated action on a graded module).** Let $\rho : E \to \mathrm{End}(M)$ be the action and let $a$ be an invertible unit. Then the conjugated action $\rho^{a}_{x} = \rho_{axa^{-1}}$ is again an action, and for homogeneous $x$ of parity $i$ the operator $\rho^{a}_{x}$ has the same parity as $\rho_{x}$,

$$
\beta\rho^{a}_{x} = (-1)^{i}\rho^{a}_{x}\beta ,
$$

because $axa^{-1}$ has the same parity $i$ as $x$; the conjugation therefore preserves the compatibility of the action with the grading, and the conjugation by a homogeneous unit is an automorphism of the graded module structure. The action by a homogeneous element $a$ itself, $m \mapsto a \cdot m$, is a different map: it sends $M_{j}$ into $M_{j+p}$ for $a$ of parity $p$, so the left multiplication by an odd element shifts the parity while the conjugation does not.

**Proof.** For homogeneous $m \in M_{j}$ and $x \in E_{i}$, the parity of $axa^{-1}$ is $i$ by the parity theorem, so $\rho^{a}_{x}$ acts with parity $i$ on $M$: $\beta\rho^{a}_{x} = (-1)^{i}\rho^{a}_{x}\beta$. The conjugation is an action because $a \mapsto \mathrm{Ad}_{a}$ is a homomorphism, and the statement for the left multiplication is the module compatibility $E_{i}M_{j} \subseteq M_{i+j}$ of *The Graded Action on a Module over a Topological Vector Space*.

**Remark (the sign rule).** The graded compatibility $\beta\rho_{x} = (-1)^{i}\rho_{x}\beta$ for $x$ of parity $i$ is the sign rule in its module form; the sign rule of the graded commutator, the graded tensor product and the graded derivations is the one of *Superalgebras and Graded Structures* and of the graded-algebra category of this Part, and it is named here and not developed; what this article fixes is the adjoint action, its trace-adjoint, and its compatibility with the grading.

## Examples

**Example (the central action).** If $a \in Z(E)^{\times}$ then $\mathrm{Ad}_{a} = \mathrm{id}$ and the parameter is in the kernel of the adjoint action; the action is trivial, its adjoint is the identity, and the compatibility with the grading is automatic because a central unit is even or the grading is trivial.

**Example (the adjoint action of an involution).** For an involution $r$ the adjoint action $\mathrm{Ad}_{r}$ is the grade involution $\alpha_{r}$, of parity one if $r$ is odd, and the adjoint of $\mathrm{Ad}_{r}$ is $\mathrm{Ad}_{r}$ because $r^{-1} = r$; the adjoint action of an involution is therefore self-adjoint and unitary, the reflection structure of *The Signed Adjoint of the Reflection on a Topological Vector Space*.

**Example (the graded endomorphism algebra).** For $M = E$ with the regular action and the adjoint action of $E^{\times}$ on the endomorphisms by conjugation, every homogeneous unit acts by a graded automorphism, because the two same-parity factors cancel, while a general unit acts by a graded automorphism exactly when $a^{-1}\alpha(a)$ is central; the induced adjoint action on the graded endomorphism algebra is compatible with its grading, and the sign rule of the commutator of the graded endomorphisms is deferred, as above.

## Summary

The adjoint action $\mathrm{Ad}_{a}(x) = axa^{-1}$ of the invertible elements of a topological algebra is a continuous representation of the unit group with kernel the central units, and with respect to the trace form of the category its adjoint is $\mathrm{Ad}_{a^{-1}}$, so the adjoint action is unitary and preserves self-adjointness and unitarity. On a graded algebra the conjugation by a homogeneous unit of parity $p$ preserves the grading, sending $E_{i}$ to $E_{i}$ for $p = 0$ and for $p = 1$ alike, because the two same-parity factors cancel, and a general unit preserves the grading exactly when $a^{-1}\alpha(a)$ is central; the conjugate of the grade involution is the signed inner sandwich of the parameter, so the adjoint action of an involution reproduces the reflection's graded structure. On a graded module the conjugated action satisfies $\beta\rho^{a}_{x} = (-1)^{i}\rho^{a}_{x}\beta$ for a homogeneous $x$ of parity $i$, the conjugation preserving the parity; the sign rule of the graded commutator and of the graded tensor product belongs to *Superalgebras and Graded Structures* and to the graded-algebra category of this Part, and is named, not developed. The forms are Part III.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $E = E_{0}\oplus E_{1}$, $\alpha$ | graded topological algebra and its grade involution |
| $\mathrm{Ad}_{a}(x) = axa^{-1}$ | adjoint action of a unit |
| $(\mathrm{Ad}_{a})^{\dagger} = \mathrm{Ad}_{a^{-1}}$ | the trace-adjoint, unitary |
| $\mathrm{Ad}_{a}(E_{i}) \subseteq E_{i + p}$ | parity $p$ of the conjugating unit |
| $a^{-1}\alpha(a) \in Z(E)$ | grading-preservation condition |
| $\mathrm{Ad}_{a}\alpha = \Theta^{\alpha}_{a,a^{-1}}$ | conjugate of the grade involution |
| $M = M_{0}\oplus M_{1}$, $\beta$ | graded module and its grade involution |
| $\beta\rho^{a}_{x} = (-1)^{i}\rho^{a}_{x}\beta$ | the module compatibility, $x \in E_{i}$ |
| $Z(E)$ | centre; inner automorphisms modulo it |

## Further Reading

- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras I* (Academic Press, 1983), for the inner automorphisms and the unitary elements of an operator algebra.
- Jacques Dixmier, *von Neumann Algebras* (North-Holland, 1981), for the traces, the conjugations and the unitary group.
- Serge Lang, *Algebra* (Springer, third edition, 2002), for the graded algebras, the graded modules and the adjoint action.
- Pierre Deligne and John W. Morgan, *Notes on Supersymmetry* (in *Quantum Fields and Strings*, AMS, 1999), for the sign rule of the graded structures.
- Gottfried Köthe, *Topological Vector Spaces II* (Springer, 1979), for the topological algebras and their automorphisms.
