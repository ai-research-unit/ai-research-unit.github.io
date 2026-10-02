
# __The Graded Action on a Module over a Topological Ring__

## Introduction

A graded ring acts on a graded module by operators that respect the grading, and the operator by which it acts is the **signed action**, the module-level form of the signed left multiplication: an element of the ring sends a homogeneous element of the module of degree $j$ to one of degree $i + j$, and the parity operator of the module intertwines with the grade involution of the ring. This article treats the graded action on a topological module over a topological ring: it fixes the graded action, proves the compatibility of the action with the two grade involutions as the relation $\pi(r\cdot m) = \alpha(r)\cdot\pi(m)$, shows that the twisted (signed) action is a genuine action exactly on the even part of the ring and that the odd part obstructs it unless the sign rule is imposed, and reads the grading topologically, where the parity operator is continuous exactly when the decomposition into the even and odd parts is a topological direct sum, and where the completion preserves the grading.

The article assumes the graded ring, the grading decomposition, the grade involution and the sign rule from *Graded Rings* and *The Grade Involution*; the module over a ring, the module endomorphisms and the regular module from *Modules*; the topological module, its topology and the continuity of the action from *Topological Modules and Vector Spaces*; the signed left multiplication on the ring itself from *The Signed Left Multiplication on a Topological Ring*; the signed sandwich and its composition from *The Signed Sandwich on a Topological Ring*; and the completion operator and its functoriality from *The Completion Operator*. The cohomology of graded modules, the Koszul complex and the superalgebra of the endomorphisms are named at the boundary and not used; the adjoint action is *The Graded Adjoint Action on a Module over a Topological Ring*, later in this category. No measure, no norm and no form occurs.

Throughout, $R = R^0\oplus R^1$ is a graded ring, unital, with grade involution $\alpha$, the automorphism equal to $+1$ on $R^0$ and $-1$ on $R^1$, assumed continuous; $M = M^0\oplus M^1$ is a graded left $R$-module with **parity operator** $\pi : M\to M$, the additive operator equal to $+1$ on $M^0$ and $-1$ on $M^1$; the **degree** $|x|$ of a homogeneous element is $0$ or $1$; and the action is written $r\cdot m$.

## Graded Rings and Graded Modules

**Definition.** A **graded ring** is a ring $R = R^0\oplus R^1$ with $R^iR^j\subseteq R^{i+j}$ (indices modulo $2$); a **graded left module** over $R$ is a module $M = M^0\oplus M^1$ with $R^iM^j\subseteq M^{i+j}$. An element is **homogeneous** if it lies in $R^0\cup R^1$ or $M^0\cup M^1$, and its **degree** is $0$ or $1$ accordingly.

**Proposition (the grade involution and the parity operator).** The grade involution $\alpha(r) = (-1)^i r$ for $r \in R^i$ is an involutive ring automorphism, with fixed subring $R^0$ and skew part $R^1$; the parity operator $\pi(m) = (-1)^j m$ for $m \in M^j$ is an involutive additive operator, with fixed part $M^0$ and skew part $M^1$, and the decompositions $R = R^0\oplus R^1$ and $M = M^0\oplus M^1$ are the eigenspace decompositions of $\alpha$ and $\pi$.

**Proof.** For $\alpha$: on homogeneous elements $\alpha(rs) = (-1)^{i+j}rs = \alpha(r)\alpha(s)$ and $\alpha(r+s) = \alpha(r)+\alpha(s)$, so $\alpha$ is a ring automorphism, and $\alpha^2$ is the identity because $(-1)^{2i}=1$; the eigenspaces of an involution are the fixed and skew parts, which are exactly $R^0$ and $R^1$. The same for $\pi$ with additivity, which is the only structure the module has in this respect.

## The Parity Operator

**Proposition (the parity operator intertwines the two grade involutions).** For $r \in R$ and $m \in M$, the compatibility of the action with the gradings is the relation

$$
\pi(r\cdot m) = \alpha(r)\cdot\pi(m) ,
$$

and for homogeneous $r$ of degree $i$ this reads $\pi(r\cdot m) = (-1)^i\,r\cdot\pi(m)$. Equivalently, the action $R\times M\to M$ is a morphism of graded modules, and the parity operator is **$\alpha$-semilinear**: it is additive, involutive, and $\pi(r\cdot m) = \alpha(r)\pi(m)$.

**Proof.** For homogeneous $r\in R^i$ and $m\in M^j$ the product lies in $M^{i+j}$, so $\pi(r\cdot m) = (-1)^{i+j}r\cdot m$; on the other side $\alpha(r)\cdot\pi(m) = (-1)^i r\cdot(-1)^j m = (-1)^{i+j}r\cdot m$. Both sides are additive, so the relation holds for all $r, m$.

**Corollary (the parity operator is not $R$-linear).** For $r$ odd, $\pi(r\cdot m) = -r\cdot\pi(m)$, so $\pi$ anticommutes with the odd action: the parity operator is $R^0$-linear but $\alpha$-semilinear, and it is $R$-linear only when the ring is evenly graded, $R = R^0$.

**Proof.** Set $i = 1$ in the relation; the failure of $R$-linearity is exact. When $R^1 = 0$ the grade involution is the identity and $\pi$ commutes with the action.

## The Graded Action and the Sign Rule

**Definition.** The **graded action** of $R$ on $M$ is the action $r\cdot m$ with $R^iM^j\subseteq M^{i+j}$; the **twisted action** is

$$
r\star m = r\cdot\pi(m) ,
$$

the module-level signed left multiplication. The **sign rule** is the requirement that for homogeneous $r$ the twisted action of $r$ carry the parity operator to multiplication by $(-1)^{|r|}$, that is $\pi(r\star m) = (-1)^{|r|}\,r\star m$.

**Proposition (the twisted action on the even part).** The twisted action is compatible with the grading, $\pi(r\star m) = \alpha(r)\star\pi(m)$, and it is associative exactly on the even part: for even $r$ and $s$, $(rs)\star m = r\star(s\star m)$; for odd $s$ this fails in general.

**Proof.** $\pi(r\star m) = \pi(r\pi(m)) = \alpha(r)\pi(\pi(m)) = \alpha(r)\pi(m) = \alpha(r)\star m$, using $\pi^2 = \mathrm{id}$ and the semilinearity. For associativity, $r\star(s\star m) = r\pi(s\pi(m)) = r\pi(s)m$ and $(rs)\star m = rs\,\pi(m)$; these agree for all $m$ exactly when $r\pi(s) = rs$, that is when $\pi(s) = s$ on the relevant part, that is when $s$ is even (for a faithful action).

**Theorem (the obstruction and the sign rule).** The twisted action is a module action of $R$ on $M$ if and only if the ring is evenly graded, $R = R^0$; on a genuinely graded ring the odd elements obstruct associativity, and the obstruction disappears exactly when the sign rule is imposed, that is when the odd elements of $R$ act as odd operators, anticommuting with the parity operator. The ordinary (untwisted) action is always a module action, and the twisted and untwisted actions differ by the parity operator.

**Proof.** The associativity computation of the previous proposition shows that the twisted action is associative for all $r,s$ exactly when every homogeneous $s$ is even, that is $R^1 = 0$. When $R^1 \neq 0$ the odd elements fail associativity by exactly the sign $(-1)^{|r||s|}$ carried by the parity operator, which is the sign rule; requiring the odd elements to act as odd operators restores associativity on the graded level. The untwisted action $r\cdot m$ is a module action by the definition of a module, and the twist inserts $\pi$.

**Corollary (the twisted action recovers the signed left multiplication on the regular module).** For $M = R$ with the regular action and $\pi = \alpha$, the twisted action is $r\star x = r\alpha(x)$, which is the signed left multiplication $\ell_r$ of *The Signed Left Multiplication on a Topological Ring*; hence the graded action on the regular module is exactly the signed one-sided action, and the sign rule is the obstruction computation above.

**Proof.** Substitute $M = R$, $\pi = \alpha$ and $r\cdot x = rx$ in the definition of the twisted action; the result is $\ell_r$. The sign rule is then the associativity computation of the theorem.

## The Topological Reading

**Proposition (continuity of the action and of the parity operator).** Let $M$ be a topological $R$-module, that is a topological abelian group with a continuous action $R\times M\to M$. Then the action is continuous, the parity operator $\pi$ is continuous exactly when the decomposition $M = M^0\oplus M^1$ is a **topological direct sum**, that is when the projection onto $M^0$ along $M^1$ is continuous, and when $\pi$ is continuous the twisted action is continuous.

**Proof.** The continuity of the action is the definition of a topological module. A linear involution of a topological abelian group is continuous exactly when its eigenspace decomposition is topological, because the projection onto an eigenspace is $\tfrac12(\mathrm{id}+\pi)$ and its continuity is that of $\pi$; conversely a continuous projection makes $\pi = 2p - \mathrm{id}$ continuous. When $\pi$ is continuous the twisted action is the composite of the continuous action and $\mathrm{id}\times\pi$, hence continuous.

**Proposition (the completion preserves the grading).** Let $R$ and $M$ be complete Hausdorff, with continuous parity operators. Then the completion of $M$ for the linear topology of the module inherits the grading, $\widehat{M} = \widehat{M^0}\oplus\widehat{M^1}$, the parity operator extends, $\widehat{\pi}\circ\iota = \iota\circ\pi$, and the completed action is the action of the completed ring; so the graded action commutes with the completion operator of *The Completion Operator*.

**Proof.** The completion of a topological module for a linear topology is the inverse limit of the quotients by the open submodules; the submodules $M^0\cap N$ and $M^1\cap N$ for $N$ ranging over a fundamental system exhibit the completion as the direct sum of the completions of the two parts, and the parity operator, being continuous and additive, extends uniquely to the completion with the same intertwining. The action extends by the continuity of the multiplication and the functoriality of the completion.

**Remark (the boundary).** The graded action is the operator form of the grading, and its adjoint with respect to the form of the category is *The Graded Adjoint Action on a Module over a Topological Ring*, later in this category. The cohomology of a graded module, the Koszul complex and the superalgebra $\operatorname{End}(M)$ with its $\mathbb{Z}/2$-grading are named at this boundary and are not used; no measure, norm or form occurs.

## Examples

**Example (the symmetric algebra and its sign change).** For $R = k[x_1,\ldots,x_n]$ with the grading by degree modulo $2$ and $M = R$ with the regular action, the parity operator is $f(x)\mapsto f(-x)$ and the twisted action is $\ell_f(g) = f(-x)g$; the ring is commutative, so the twisted action is associative on the even part and the odd part obeys the sign rule.

**Example (the exterior algebra).** For the exterior algebra $\Lambda(V)$ with the usual grading, the grade involution is the sign change on the odd part, and the regular module is graded; the twisted action is the signed left multiplication, which for an odd element $v$ satisfies $\pi(v\star m) = -v\star m$ because $v$ is odd, the sign rule in its simplest form.

**Example (a graded module of rank one).** Let $M = R e$ with $e$ odd and $r\cdot e = \alpha(r)e$; then $M^0 = R^1e$ and $M^1 = R^0e$, the parity operator is $\pi(re) = (-1)^{|r|+1}re$, equal to $-e$ on the generator, and the twisted action obeys the sign rule because the generator is odd: $\pi(r\star e) = -r\star e$ for every homogeneous $r$.

**Example (the Clifford module).** The spin representation of a Clifford algebra is a graded module on which the odd elements act as odd operators, and the compatibility $\pi(r\cdot m) = \alpha(r)\cdot\pi(m)$ is the assertion that the Clifford action is a morphism of graded modules; this is the model for which the graded action is named.

## Summary

A graded ring $R = R^0\oplus R^1$ with grade involution $\alpha$ acts on a graded module $M = M^0\oplus M^1$ with parity operator $\pi$ by a graded action, $R^iM^j\subseteq M^{i+j}$, and the compatibility of the action with the two involutions is the semilinearity relation $\pi(r\cdot m) = \alpha(r)\cdot\pi(m)$, equivalently $\pi(r\cdot m) = (-1)^{|r|}r\cdot\pi(m)$ for homogeneous $r$. The parity operator is $R^0$-linear but $\alpha$-semilinear and is $R$-linear only when the ring is evenly graded. The twisted action $r\star m = r\cdot\pi(m)$ is the module-level signed left multiplication; it is compatible with the grading, and it is associative exactly on the even part of the ring, so on a genuinely graded ring the odd elements obstruct associativity, and the obstruction is removed exactly by the sign rule, which states that the odd elements act as odd operators anticommuting with the parity operator. On the regular module the twisted action is the signed left multiplication $\ell_r$ of the ring.

Topologically, the action of a topological module is continuous by definition, the parity operator is continuous exactly when the decomposition into the even and odd parts is a topological direct sum, and the completion preserves the grading and the action, so the graded action commutes with the completion operator; the adjoint of the graded action and the cohomological constructions of graded modules are the neighbouring subjects.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R = R^0\oplus R^1$ | The graded ring, $R^iR^j\subseteq R^{i+j}$ |
| $M = M^0\oplus M^1$ | The graded left module, $R^iM^j\subseteq M^{i+j}$ |
| $\alpha(r) = (-1)^i r$ | The grade involution of $R$ |
| $\pi(m) = (-1)^j m$ | The parity operator of $M$ |
| $r\cdot m$ | The graded action |
| $\pi(r\cdot m) = \alpha(r)\cdot\pi(m)$ | The semilinearity of the parity operator |
| $r\star m = r\cdot\pi(m)$ | The twisted (signed) action |
| $\pi(r\star m) = (-1)^{|r|}r\star m$ | The sign rule |
| $R^1 = 0$ | The condition for the twisted action to be associative |
| $\widehat{M} = \widehat{M^0}\oplus\widehat{M^1}$ | The completion preserves the grading |

## Further Reading

- Nicolas Bourbaki, *Algebra I, Chapters 1–3* (Springer, 1998), for graded rings, graded modules and the regular module.
- C. T. C. Wall, "Graded algebras, anti-involutions, simple groups and symmetric spaces", *Bulletin of the American Mathematical Society* **74** (1968), 143–148, for graded algebras, their involutions and the sign rule.
- Pierre Deligne and John Morgan, *Notes on Supersymmetry (following Joseph Bernstein)*, in *Quantum Fields and Strings: A Course for Mathematicians* (American Mathematical Society, 1999), for the sign rule in graded (super) algebra.
- Claude Chevalley, *The Algebraic Theory of Spinors and Clifford Algebras* (Springer, 1997; collected works), for graded modules over a Clifford algebra and the parity operator.
- Joseph J. Rotman, *An Introduction to Homological Algebra* (Springer, 2nd ed. 2009), for complexes, the Koszul sign rule and the grading of the endomorphism algebra.
