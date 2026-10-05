
# __The Graded Action on a Module over an Involutive Banach Algebra__

## Introduction

An algebra with a grade involution $\alpha$ acts on itself through the signed left multiplication, and the same construction applies to a module: when a Banach module $M$ over a graded Banach algebra carries a **parity operator** $\pi$, an involutive additive map that reverses the sign of the odd part, the action can be twisted by the grading and one gets the **graded action**

$$
r \star m = r \cdot \pi(m) .
$$

The twisted action is not a module action of the whole algebra, and the defect is exactly the sign rule: the product $r\star(s\star m)$ differs from $(rs)\star m$ by the factor $\alpha(s)-s$, so associativity holds exactly on the even part. The two structural facts that make the graded action work are the compatibility of the action with the grading, $\pi(r\cdot m) = \alpha(r)\cdot\pi(m)$, which is the module form of the semilinearity of the parity operator, and the self-adjointness of $\pi$ for the form of the category, which is what makes the adjoint of the graded action a graded action. This article fixes the graded action on a Banach module, proves the compatibility and the sign rule, identifies the operators the even and the odd elements produce, relates the construction to the regular module where it is the signed left multiplication, and reads the completion.

The article assumes the Banach algebra and its norm from *Topological Algebras and Banach Algebras*; the graded algebra, the grade involution and the sign rule from *Involutive Topological Bilinear Algebras* and *Graded Rings*; the topological and Banach modules, the continuous operators and the completed tensor products from *Topological Modules and Vector Spaces* and *Normed and Banach Spaces*; the signed left multiplication from *The Signed Left Multiplication on an Involutive Banach Algebra*; and the graded action of Part I from *The Graded Action on a Module over an Algebra*. The adjoint action is *The Graded Adjoint Action on a Module over an Involutive Banach Algebra*, later in this category; the anti-automorphism involution $\sigma$ is the `- * Theory` structure and is not used.

Throughout, $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$; $A$ is a unital Banach algebra over $\mathbb{K}$ with continuous grade involution $\alpha$, $\alpha^2 = \mathrm{id}$; $A = A^0\oplus A^1$ is the grading, with $A^0$ the even part and $A^1$ the odd part; $M$ is a Banach $A$-module with $\lVert r\cdot m\rVert \leq \lVert r\rVert\lVert m\rVert$; $\pi : M \to M$ is a **parity operator**, a continuous additive involution commuting with the scalars, $\pi^2 = \mathrm{id}$, with

$$
\pi(r\cdot m) = \alpha(r)\cdot\pi(m) \qquad (r \in A,\ m \in M) ;
$$

$M = M^0\oplus M^1$ is the grading of $M$ by $\pi$, with $M^0 = \ker(\pi-\mathrm{id})$ and $M^1 = \ker(\pi+\mathrm{id})$; and the **graded action** is $\ell_r^\pi(m) = r\star m = r\cdot\pi(m)$.

## The Graded Action

**Definition.** The **graded action** of $A$ on $M$ is the bilinear map

$$
A \times M \to M , \qquad (r,m) \mapsto r \star m = r\cdot\pi(m) ,
$$

and the **graded (twisted) multiplication** by $r$ is the operator $\ell_r^\pi(m) = r\cdot\pi(m)$.

**Proposition (compatibility of the action with the grading).** The parity operator satisfies

$$
\pi(r\cdot m) = \alpha(r)\cdot\pi(m) , \qquad \text{and for homogeneous } r , \quad \pi(r\cdot m) = (-1)^{\lvert r\rvert}\,r\cdot\pi(m) ,
$$

where $\lvert r\rvert$ is the parity of a homogeneous $r$. Equivalently $\pi \circ L_r = L_{\alpha(r)}\circ\pi$ and $L_r\circ\pi = \pi\circ L_{\alpha(r)}$ for the plain action $L_r(m) = r\cdot m$. Hence $\pi$ is $A^0$-linear but not $A$-linear unless $A^1 = 0$.

**Proof.** The identity is the defining property of the parity operator; for homogeneous $r$ with $\alpha(r) = (-1)^{\lvert r\rvert}r$ it reads $\pi(r\cdot m) = (-1)^{\lvert r\rvert}r\cdot\pi(m)$. For even $r$ the equation reads $\pi(r\cdot m) = r\cdot\pi(m)$, which is $A^0$-linearity; for odd $r$ it reads $\pi(r\cdot m) = -r\cdot\pi(m)$, which contradicts $A$-linearity when the odd part is nonzero. $\square$

**Proposition (the sign rule and the failure of associativity).** For all $r,s \in A$ and $m \in M$,

$$
r\star(s\star m) = \bigl(r\,\alpha(s)\bigr)\cdot m , \qquad (rs)\star m = (rs)\cdot\pi(m) ,
$$

so the graded action is associative, $r\star(s\star m) = (rs)\star m$ for all $r,s,m$, exactly when every $s$ is even, that is $A = A^0$; in general the obstruction is the odd part of $s$. The operator $\ell_r^\pi$ satisfies the sign rule

$$
\ell_r^\pi\circ\pi = L_r , \qquad \pi\circ\ell_r^\pi = L_{\alpha(r)} , \qquad \text{so} \quad \pi\ell_r^\pi = (-1)^{\lvert r\rvert}\,\ell_r^\pi\pi ,
$$

and an odd element produces an operator anticommuting with $\pi$, an even element one commuting with $\pi$.

**Proof.** $r\star(s\star m) = r\star(s\cdot\pi(m)) = r\cdot\pi(s\cdot\pi(m)) = r\cdot\alpha(s)\cdot\pi^2(m) = r\alpha(s)\cdot m$; $(rs)\star m = rs\cdot\pi(m)$. The two agree for all $m$ exactly when $r\alpha(s) = rs$ as operators, that is $\alpha(s) = s$; this for every $r$ and every $s$ is $A = A^0$. For the sign rule, $\ell_r^\pi\pi(m) = r\cdot\pi^2(m) = r\cdot m$ and $\pi\ell_r^\pi(m) = \pi(r\cdot\pi(m)) = \alpha(r)\cdot\pi^2(m) = \alpha(r)\cdot m$, so $\pi\ell_r^\pi = L_{\alpha(r)} = (-1)^{\lvert r\rvert}L_r = (-1)^{\lvert r\rvert}\ell_r^\pi\pi$ for homogeneous $r$. $\square$

**Remark (the honest sign rule).** The graded action is the correct notion of an action twisted by the grading; the price is that it is not an action of the algebra but an action of the graded algebra in the sense of superalgebras: odd elements act as odd operators, and the sign rule $\pi\ell_r^\pi\pi = (-1)^{\lvert r\rvert}\ell_r^\pi$ is the statement that the operator is even or odd according to the parity of the element. The associative rewriting is recovered on the even part, which is the honest domain of the twisted action.

## The Operators the Elements Produce

**Proposition (the regular module).** For $M = A$ with the regular action $r\cdot m = rm$ and $\pi = \alpha$, the graded multiplication is the signed left multiplication,

$$
\ell_r^\pi(m) = r\,\alpha(m) = \ell_r(m) ,
$$

and the graded action of $A$ on itself is the signed left multiplication of *The Signed Left Multiplication on an Involutive Banach Algebra*.

**Proof.** Substituting $M = A$, $r\cdot m = rm$ and $\pi = \alpha$ gives $\ell_r^\pi(m) = r\alpha(m) = \ell_r(m)$; the compatibility $\pi(r\cdot m) = \alpha(r)\cdot\pi(m)$ is the multiplicativity of $\alpha$. $\square$

**Proposition (the even and the odd operators).** For $r \in A^0$ the operator $\ell_r^\pi$ preserves each of $M^0$ and $M^1$:

$$
\ell_r^\pi = r\cdot \text{ on } M^0 , \qquad \ell_r^\pi = -r\cdot \text{ on } M^1 ;
$$

for $r \in A^1$ the operator $\ell_r^\pi$ exchanges the two parts, $\ell_r^\pi(M^0) \subseteq M^1$ and $\ell_r^\pi(M^1) \subseteq M^0$. The operators are bounded with

$$
\lVert\ell_r^\pi\rVert \leq \lVert r\rVert\,\lVert\pi\rVert .
$$

**Proof.** On $M^0$, $\pi = \mathrm{id}$, so $\ell_r^\pi(m) = r\cdot m$; on $M^1$, $\pi = -\mathrm{id}$, so $\ell_r^\pi(m) = -r\cdot m$. For odd $r$, $\pi(\ell_r^\pi(m)) = \alpha(r)\cdot m = -r\cdot m$, so $\ell_r^\pi(m) \in M^1$ when $m \in M^0$ and in $M^0$ when $m \in M^1$. Boundedness is the composition of $L_r$ with $\pi$. $\square$

## Topology and Completion

**Proposition (continuity and the completed grading).** The parity operator $\pi$ is a topological automorphism of the additive group of $M$, hence a homeomorphism, with $\lVert\pi\rVert < +\infty$; the graded action is continuous as a map $A \times M \to M$; and if $M$ is graded, the completion of $M$ is the direct sum of the completions of its parts,

$$
\widehat{M} = \widehat{M^0} \oplus \widehat{M^1} ,
$$

the parity operator extending to the completion as the sign change of the two summands.

**Proof.** $\pi$ is a continuous additive involution, so it is a homeomorphism with inverse itself; the graded action is the composite of the continuous action with $\pi$, hence continuous. For a graded $M$, the projections $p_0 = \tfrac12(\mathrm{id}+\pi)$ and $p_1 = \tfrac12(\mathrm{id}-\pi)$ are continuous when $2$ is invertible, so the grading is a topological direct sum and the completion of a direct sum is the direct sum of the completions. $\square$

**Example (a graded Banach module).** Let $A = A^0\oplus A^1$ be a graded Banach algebra and let $M = A^n$ with the componentwise action and the parity operator acting by $\alpha$ on each component. Then the graded action is componentwise the signed left multiplication, and the odd elements exchange the even and the odd parts of the module.

**Example (the sup-norm module).** Let $A = C(X,\mathbb{K})$ with the grading by a clopen subset $E$, so that $\alpha(f) = (2\chi - 1)f$, and let $M = C(X,\mathbb{K})$ with the parity operator $\pi(g) = (2\chi' - 1)g$ for another clopen subset $E'$. The compatibility $\pi(fg) = \alpha(f)\pi(g)$ holds exactly when the sign functions satisfy $\chi'\chi_E = \chi_E\chi'$ on the supports, that is when the two clopen subsets are compatible, and then the graded action is $f\star g = f(2\chi' - 1)g$.

## Summary

On a Banach module $M$ over a graded Banach algebra $A$ with grade involution $\alpha$ and parity operator $\pi$, the graded action is $r\star m = r\cdot\pi(m) = \ell_r^\pi(m)$, built on the compatibility $\pi(r\cdot m) = \alpha(r)\cdot\pi(m)$, which is the module form of the semilinearity of $\pi$: for homogeneous $r$ it reads $\pi(r\cdot m) = (-1)^{\lvert r\rvert}r\cdot\pi(m)$. The twisted multiplication is associative exactly on the even part, $r\star(s\star m) = r\alpha(s)\cdot m$ versus $(rs)\star m = rs\cdot\pi(m)$; the obstruction is the odd part of $s$, and the operator satisfies the sign rule $\pi\ell_r^\pi = (-1)^{\lvert r\rvert}\ell_r^\pi\pi$, an odd element producing an operator that anticommutes with $\pi$. On the regular module $M = A$, $\pi = \alpha$, the graded action is the signed left multiplication; on a graded module the even elements act with the sign $+1$ on the even part and $-1$ on the odd part, and the odd elements exchange the two parts. The operators are bounded with $\lVert\ell_r^\pi\rVert \leq \lVert r\rVert\lVert\pi\rVert$, the parity operator is a homeomorphism, and the completion preserves the grading. The adjoint is *The Graded Adjoint Action on a Module over an Involutive Banach Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A$, $\alpha$, $A = A^0\oplus A^1$ | Graded Banach algebra, grade involution, grading |
| $M$, $\lVert\cdot\rVert$ | Banach $A$-module |
| $\pi$, $\lVert\pi\rVert$, $M = M^0\oplus M^1$ | Parity operator, its bound, the grading of $M$ |
| $\pi(r\cdot m) = \alpha(r)\cdot\pi(m)$ | Compatibility of the action with the grading |
| $r\star m = \ell_r^\pi(m) = r\cdot\pi(m)$ | The graded action |
| $r\star(s\star m) = r\alpha(s)\cdot m$ | Twisted associativity; holds iff $A = A^0$ |
| $\pi\ell_r^\pi = (-1)^{\lvert r\rvert}\ell_r^\pi\pi$ | The sign rule |
| $\widehat{M} = \widehat{M^0}\oplus\widehat{M^1}$ | Completion preserves the grading |

## Further Reading

- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for the graded modules, the grade involution and the sign rule.
- Nicolas Bourbaki, *Algebra I, Chapters 1–3* (Springer, 1998), for the graded modules and the operators they carry.
- Charles E. Rickart, *General Theory of Banach Algebras* (Van Nostrand, 1960), for the Banach modules and the bounded operators on them.
- Theodore W. Palmer, *Banach Algebras and the General Theory of ${}^*$-Algebras, Volume I* (Cambridge University Press, 1994), for the graded Banach algebras and their modules.
- Joseph J. Rotman, *An Introduction to Homological Algebra* (Springer, second edition, 2009), for the sign rule of the graded structures and the Koszul sign convention.
