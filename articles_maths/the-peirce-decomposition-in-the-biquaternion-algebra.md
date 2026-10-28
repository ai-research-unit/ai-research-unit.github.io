# __The Peirce Decomposition of the Biquaternion Algebra__

## Introduction

The biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has complex dimension four. A root of one, an element $\tilde\Xi$ with
$$
\tilde\Xi^{2}=e_{t},\qquad \tilde\Xi\ne\pm e_{t},
$$
produces the two idempotents
$$
\tilde\Pi_{\pm}=\frac{e_{t}\pm\tilde\Xi}{2},
$$
and the two idempotents cut $\mathbb{B}$ into four complex lines
$$
\mathbb{B}_{st}=\tilde\Pi_{s}\mathbb{B}\tilde\Pi_{t},\qquad s,t\in\{+,-\}.
$$
The root is the only input. No family of idempotents is preferred, and no element of a mixed line is chosen.

The article defines the family and the four lines, proves that each line is one-dimensional and that the lines sum directly, computes their multiplication rule, reads the weights of the root and the spin of the spinor space, and identifies the grading. The choice of an element in each line is the subject of *The Peirce Basis of the Biquaternion Algebra*; it needs more than the root. An example is given at the end.

## The Root and the Family

**Definition.** A family $\tilde\Pi_{+},\tilde\Pi_{-}$ is complete, orthogonal and idempotent when
$$
\tilde\Pi_{\pm}^{2}=\tilde\Pi_{\pm},\qquad
\tilde\Pi_{+}\tilde\Pi_{-}=\tilde\Pi_{-}\tilde\Pi_{+}=0,\qquad
\tilde\Pi_{+}+\tilde\Pi_{-}=e_{t}.
$$
It is nondegenerate when $\tilde\Pi_{\pm}\ne0$.

**The root.** For a nondegenerate family put
$$
\tilde\Xi=\tilde\Pi_{+}-\tilde\Pi_{-}.
$$
Then $\tilde\Xi^{2}=e_{t}$, $\tilde\Xi\ne\pm e_{t}$, and the family is recovered by $\tilde\Pi_{\pm}=(e_{t}\pm\tilde\Xi)/2$. Conversely, every root with $\tilde\Xi\ne\pm e_{t}$ gives a nondegenerate family by these formulas.

**The roots.** Write $\tilde\Xi=a e_{t}+\vec v$ with $a\in\mathbb{C}$ and $\vec v$ a complex vector. Then
$$
\tilde\Xi^{2}=(a^{2}-\vec v\cdot\vec v)e_{t}+2a\vec v,
$$
so $\tilde\Xi^{2}=e_{t}$ is equivalent to $a^{2}-\vec v\cdot\vec v=1$ and $a\vec v=0$. If $\vec v=0$ then $a=\pm1$, the trivial roots. Otherwise $a=0$ and $\vec v\cdot\vec v=-1$. Writing $\vec v=i\vec u$ gives
$$
\tilde\Xi=i\vec u,\qquad \vec u\cdot\vec u=1.
$$
The vector $\vec u$ has three complex components subject to one complex equation, hence four real parameters. The two roots $\pm\tilde\Xi$ give the same family with the two idempotents interchanged.

## The Four Lines

**Definition.** For $s,t\in\{+,-\}$ the Peirce line is $\mathbb{B}_{st}=\tilde\Pi_{s}\mathbb{B}\tilde\Pi_{t}$.

**Theorem.** Let $\tilde\Xi=i\vec u$ be a root with $\vec u\cdot\vec u=1$. Then each $\mathbb{B}_{st}$ is a complex line, and
$$
\mathbb{B}=\mathbb{B}_{++}\oplus\mathbb{B}_{+-}\oplus\mathbb{B}_{-+}\oplus\mathbb{B}_{--}.
$$

**Proof.** The sum is direct: if $\sum_{s,t}Q_{st}=0$ with $Q_{st}\in\mathbb{B}_{st}$, then multiplying on the left by $\tilde\Pi_{s}$ and on the right by $\tilde\Pi_{t}$ gives $Q_{st}=0$. It is all of $\mathbb{B}$ because
$$
\tilde Q=(\tilde\Pi_{+}+\tilde\Pi_{-})\tilde Q(\tilde\Pi_{+}+\tilde\Pi_{-})
=\sum_{s,t}\tilde\Pi_{s}\tilde Q\tilde\Pi_{t}
$$
for every $\tilde Q\in\mathbb{B}$. It remains to compute a corner.

Let $\tilde Q\in\mathbb{B}_{st}$, so that
$$
\tilde\Xi\tilde Q=s\tilde Q,\qquad \tilde Q\tilde\Xi=t\tilde Q.
$$
Write $\tilde Q=a e_{t}+\vec v$ with $a\in\mathbb{C}$ and $\vec v$ a complex vector, and decompose
$$
\vec v=\alpha\vec u+\vec w,\qquad \vec u\cdot\vec w=0.
$$
Since $\vec u^{2}=-e_{t}$ and $\vec u\cdot\vec u=1$, the map $T(\vec w)=\vec u\times\vec w$ satisfies $T^{2}=-\mathrm{id}$ on the plane $\vec u^{\perp}$. The two eigenvalue equations become, in the scalar, the $\vec u$ and the $\vec u^{\perp}$ parts,
$$
-i\alpha=sa,\qquad ia=s\alpha,\qquad iT(\vec w)=s\vec w,
$$
$$
-i\alpha=ta,\qquad ia=t\alpha,\qquad -iT(\vec w)=t\vec w.
$$

If $s=t$, the last pair gives $\vec w=0$, and the first pair gives $a=-is\alpha$. Hence $\tilde Q$ is a multiple of $\tilde\Pi_{s}$.

If $s=-t$, the scalar equations give $a=\alpha=0$, and $\vec w$ is an eigenvector of $T$ with eigenvalue $-is$. The eigenspaces of $T$ are one-dimensional, because $T^{2}=-\mathrm{id}$ on a two-dimensional space. Hence each corner is at most one-dimensional; the direct sum has dimension four, so each corner is exactly one-dimensional.

## The Multiplication Rule

**Theorem.** For $s,t,u,v\in\{+,-\}$,
$$
\mathbb{B}_{st}\mathbb{B}_{uv}\subseteq\delta_{tu}\mathbb{B}_{sv}.
$$

**Proof.** For $\tilde Q,\tilde Q'\in\mathbb{B}$,
$$
(\tilde\Pi_{s}\tilde Q\tilde\Pi_{t})(\tilde\Pi_{u}\tilde Q'\tilde\Pi_{v})
=\tilde\Pi_{s}\tilde Q(\tilde\Pi_{t}\tilde\Pi_{u})\tilde Q'\tilde\Pi_{v}
=\delta_{tu}\,\tilde\Pi_{s}\tilde Q\tilde Q'\tilde\Pi_{v},
$$
which lies in $\mathbb{B}_{sv}$ when $t=u$ and is zero otherwise.

The right index of the first factor must equal the left index of the second; the product runs from the left index of the first to the right index of the second. The mixed lines are square-zero, and the diagonal lines are the two idempotent lines.

## The Weights

**Left and right multiplication by the root give the two indices, and their difference is the adjoint weight.** For $\tilde Q\in\mathbb{B}_{st}$,
$$
\tilde\Xi\tilde Q=s\tilde Q,\qquad \tilde Q\tilde\Xi=t\tilde Q,\qquad
[\tilde\Xi,\tilde Q]=(s-t)\tilde Q.
$$

| Corner | $L_{\tilde\Xi}$ | $R_{\tilde\Xi}$ | $\operatorname{ad}_{\tilde\Xi}$ | $\operatorname{ad}_{J_{3}}$, $J_{3}=\tfrac12\tilde\Xi$ |
|---|---|---|---|---|
| $\mathbb{B}_{++}$ | $+1$ | $+1$ | $0$ | $0$ |
| $\mathbb{B}_{+-}$ | $+1$ | $-1$ | $+2$ | $+1$ |
| $\mathbb{B}_{-+}$ | $-1$ | $+1$ | $-2$ | $-1$ |
| $\mathbb{B}_{--}$ | $-1$ | $-1$ | $0$ | $0$ |

**The spin of the spinor space.** The space
$$
S_{+}=\mathbb{B}\tilde\Pi_{+}=\mathbb{B}_{++}\oplus\mathbb{B}_{-+}
=\mathbb{C}\tilde\Pi_{+}\oplus\mathbb{B}_{-+}
$$
is two-dimensional over $\mathbb{C}$. The operator $J_{3}=\tfrac12\tilde\Xi$ acts on it with weight $+\tfrac12$ on $\tilde\Pi_{+}$ and $-\tfrac12$ on $\mathbb{B}_{-+}$. The highest weight is $\tfrac12$, so $S_{+}$ is irreducible of spin
$$
j=\frac12,\qquad 2j+1=2.
$$
The highest-weight vector is $\tilde\Pi_{+}$, which is fixed by the root. The lowest-weight line $\mathbb{B}_{-+}$ has no vector fixed by the root. The same holds on $S_{-}=\mathbb{B}\tilde\Pi_{-}$, with $\tilde\Pi_{-}$ of weight $-\tfrac12$ and $\mathbb{B}_{+-}$ of weight $+\tfrac12$. The spin is the highest weight; it is the same for every root.

**The ladder without a choice of basis.** Left multiplication by any nonzero element of $\mathbb{B}_{+-}$ carries $\mathbb{B}_{-+}$ isomorphically onto $\mathbb{B}_{++}$ and annihilates $\mathbb{B}_{++}$; left multiplication by any nonzero element of $\mathbb{B}_{-+}$ carries $\mathbb{B}_{++}$ isomorphically onto $\mathbb{B}_{-+}$ and annihilates $\mathbb{B}_{+-}$. So the two mixed lines are the raising and lowering operators, up to scale. The scale is not fixed by the root; it is the gauge, treated in *The Peirce Basis of the Biquaternion Algebra*.

## The Grading

**The diagonal lines form a subalgebra and the mixed lines form its bimodule: the decomposition is a $\mathbb{Z}/2$-grading.** Put
$$
A_{0}=\mathbb{B}_{++}\oplus\mathbb{B}_{--},\qquad
A_{1}=\mathbb{B}_{+-}\oplus\mathbb{B}_{-+}.
$$
The product rule reads
$$
A_{0}A_{0}\subseteq A_{0},\qquad
A_{0}A_{1}\subseteq A_{1},\qquad
A_{1}A_{0}\subseteq A_{1},\qquad
A_{1}A_{1}\subseteq A_{0}.
$$
Here $A_{0}=\mathbb{C}\tilde\Pi_{+}\oplus\mathbb{C}\tilde\Pi_{-}$ is the commutative algebra $\mathbb{C}\times\mathbb{C}$ with unit $e_{t}$, and $A_{1}$ is the sum of the two mixed lines. The parity of a corner $\mathbb{B}_{st}$ is the product $st$, which is $+1$ on the diagonal and $-1$ on the mixed lines.

## What the Decomposition Does Not Give

The root gives the four lines and their multiplication. It gives no element of a mixed line, no basis, no gauge and no spinor. The diagonal lines have vectors fixed by the root, the idempotents. The mixed lines do not: each is a complex line with its zero element removed, and the choice of a point in it is an extra datum. That datum, and the freedom that remains after it, are *The Peirce Basis of the Biquaternion Algebra*.

## Example: The Root $i\vec e_{z}$

This example is given at the end because it is one point in the four-real-parameter space of roots, not a preferred one.

For $\tilde\Xi=i\vec e_{z}$,
$$
\tilde\Pi_{+}=\frac{e_{t}+i\vec e_{z}}{2},\qquad
\tilde\Pi_{-}=\frac{e_{t}-i\vec e_{z}}{2},
$$
and the four lines are spanned by
$$
\tilde\Pi_{+},\qquad
\vec\Upsilon_{1}=\frac{i\vec e_{x}-\vec e_{y}}{2},\qquad
\vec\Upsilon_{2}=\frac{i\vec e_{x}+\vec e_{y}}{2},\qquad
\tilde\Pi_{-},
$$
with $\vec\Upsilon_{1}\in\mathbb{B}_{+-}$ and $\vec\Upsilon_{2}\in\mathbb{B}_{-+}$. The products are
$$
\tilde\Pi_{+}\vec\Upsilon_{1}=\vec\Upsilon_{1}=\vec\Upsilon_{1}\tilde\Pi_{-},\qquad
\tilde\Pi_{-}\vec\Upsilon_{2}=\vec\Upsilon_{2}=\vec\Upsilon_{2}\tilde\Pi_{+},
$$
$$
\vec\Upsilon_{1}\vec\Upsilon_{2}=\tilde\Pi_{+},\qquad
\vec\Upsilon_{2}\vec\Upsilon_{1}=\tilde\Pi_{-},\qquad
\vec\Upsilon_{1}^{2}=\vec\Upsilon_{2}^{2}=0,
$$
and the other four products vanish. The weights under $J_{3}=\tfrac12 i\vec e_{z}$ are $+\tfrac12$ on $\tilde\Pi_{+}$ and $\vec\Upsilon_{1}$, and $-\tfrac12$ on $\vec\Upsilon_{2}$ and $\tilde\Pi_{-}$.

## Summary

A root $\tilde\Xi=i\vec u$ with $\vec u\cdot\vec u=1$ gives the idempotents $\tilde\Pi_{\pm}=(e_{t}\pm\tilde\Xi)/2$ and four complex lines $\mathbb{B}_{st}=\tilde\Pi_{s}\mathbb{B}\tilde\Pi_{t}$, each of dimension one, with the product rule $\mathbb{B}_{st}\mathbb{B}_{uv}\subseteq\delta_{tu}\mathbb{B}_{sv}$. The root has four real parameters; the family is the root modulo sign. The diagonal lines are fixed by the root and the mixed lines are nonzero and not fixed. On the spinor space $S_{+}=\mathbb{B}\tilde\Pi_{+}$ the operator $J_{3}=\tfrac12\tilde\Xi$ has highest weight $\tfrac12$, so the spinor has spin $j=\tfrac12$; on the traceless part $\operatorname{ad}_{J_{3}}$ has weights $+1,0,-1$. The four lines are a $\mathbb{Z}/2$-grading. The root fixes the lines but no element inside a mixed line.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | The biquaternion algebra |
| $e_{t},\vec e_{x},\vec e_{y},\vec e_{z}$ | The quaternion units |
| $\tilde\Xi=i\vec u$ | A root of $1$, $\vec u\cdot\vec u=1$ |
| $\tilde\Pi_{\pm}=\tfrac12(e_{t}\pm\tilde\Xi)$ | The two idempotents |
| $\mathbb{B}_{st}=\tilde\Pi_{s}\mathbb{B}\tilde\Pi_{t}$ | A Peirce line |
| $\vec\Upsilon_{+-},\vec\Upsilon_{-+}$ | Nonzero elements of the mixed lines |
| $J_{3}=\tfrac12\tilde\Xi$ | The spin operator on the spinor space |

## Further Reading

- [The Biquaternion Algebra and Its Vector Spaces](the-biquaternion-algebra-and-its-vector-spaces.html), for the units, the product table and the centre.
- [Square Roots of One and the Idempotents of the Biquaternion Algebra](square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.html), for the roots and the idempotents.
- [The Peirce Basis of the Biquaternion Algebra](the-peirce-basis-in-the-biquaternion-algebra.html), for the choice of an element in each line and the gauge.
- [Spinors as Peirce Coordinates in the Biquaternion Algebra](spinors-as-peirce-coordinates-in-the-biquaternion-algebra.html), for the elements of the two spinor spaces.
- [The Weight of a Frame Root and the Spin Quantum Number](the-weight-of-a-frame-root-and-the-spin-quantum-number.html), for the definition of the highest weight and the spin.
- [The Peirce Decomposition in $n$ Dimensions](the-peirce-decomposition-in-n-dimensions.html), for the general case.
