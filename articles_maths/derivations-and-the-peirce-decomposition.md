# __Derivations and the Peirce Decomposition__

## Introduction

A derivation of an algebra is a linear map $\delta:A\to A$ satisfying the Leibniz rule

$$
\delta(ab)=\delta(a)b+a\delta(b).
$$

The inner derivations are the commutators $\operatorname{ad}_a(x)=ax-xa$, and the outer derivations are the rest. The Peirce decomposition of an idempotent $e$ gives a precise picture of both: the value $\delta(e)$ is always off-diagonal,

$$
\delta(e)\in N=A_{01}\oplus A_{10},
$$

and every element of $N$ occurs as $\delta(e)$ for an inner derivation. The derivations that kill $e$ are exactly the **Peirce-preserving** derivations, the ones that preserve each of the four corners. The article proves the resulting exact sequence

$$
0\longrightarrow \operatorname{Der}(A,e)\longrightarrow \operatorname{Der}(A)\xrightarrow{\ \operatorname{ev}_e\ }N\longrightarrow0,
$$

where $\operatorname{Der}(A,e)=\{\delta:\delta(e)=0\}$ and $\operatorname{ev}_e(\delta)=\delta(e)$. The sequence splits as vector spaces, and the splitting is the inner derivation by the off-diagonal element $-x_{01}+x_{10}$.

The decomposition of a general derivation is therefore

$$
\delta=\operatorname{ad}_a+\delta_0, \qquad a\in N,\quad \delta_0\in\operatorname{Der}(A,e),
$$

with $a$ unique. The Peirce-preserving part $\delta_0$ has a diagonal block matrix and restricts to derivations of the corner algebras; the inner part $\operatorname{ad}_a$ carries the corner-shifting blocks. In the central simple case every derivation is inner, so $\delta_0$ is itself inner by a diagonal element, and the exact sequence computes the evaluation map on the inner derivations. The article also reads the result in Hochschild cohomology: the derivations are the 1-cocycles, the inner derivations are the 1-coboundaries, and the evaluation at $e$ is the Peirce decomposition of the cocycle space.

The article is the derivation companion of *The Commutator Operator*, *Left and Right Multiplication on the Diagonal Peirce Part* and *The Sandwich Operators on the Peirce Components*. The Peirce decomposition is that of *Unital Algebras*, §*Idempotents and the Peirce Decomposition*; the inner derivations are *The Commutator Operator*; the central simple case is *Central Simple Algebras and the Brauer Group*; the Hochschild complex is *The Hochschild Differential as an Operator*; and the matrix examples are *Matrix Algebras*. No form, involution or topology is used.

Throughout, $k$ is a field and $A$ is a unital associative $k$-algebra with $1\neq0$, not assumed commutative and not assumed finite-dimensional unless a statement says so. The idempotent is $e$, its complement is $f=1-e$, the corners are $A_{ij}=e_iAe_j$ with $e_0=e$, $e_1=f$, and the Peirce decomposition is $A=A_{00}\oplus A_{01}\oplus A_{10}\oplus A_{11}$ with $A_{ij}A_{kl}\subseteq\delta_{jk}A_{il}$. The diagonal part is $D=A_{00}\oplus A_{11}$, the off-diagonal part is $N=A_{01}\oplus A_{10}$, and $\operatorname{ad}_a=L_a-R_a$ is the inner derivation by $a$.

## Derivations

### Definition and first properties

**Definition.** A **derivation** of $A$ is a $k$-linear map $\delta:A\to A$ with

$$
\delta(ab)=\delta(a)b+a\delta(b)\qquad\text{for all }a,b\in A.
$$

The set of derivations is written $\operatorname{Der}(A)$; it is a Lie algebra under the commutator $[\delta,\varepsilon]=\delta\varepsilon-\varepsilon\delta$, and a module over the centre $Z(A)$.

**Proposition.** Let $\delta$ be a derivation.

**(a)** $\delta(1)=0$.

**(b)** $\delta(a^n)=\sum_{i=0}^{n-1}a^i\delta(a)a^{n-1-i}$ for $n\geq1$.

**(c)** If $a$ is invertible, $\delta(a^{-1})=-a^{-1}\delta(a)a^{-1}$.

**(d)** The kernel of $\delta$ is a subalgebra of $A$ containing $1$.

*Proof.* (a) $\delta(1)=\delta(1\cdot1)=\delta(1)+\delta(1)$. (b) Induction on $n$. (c) Differentiate $aa^{-1}=1$. (d) If $\delta(a)=\delta(b)=0$, then $\delta(ab)=0$; and $1\in\ker\delta$ by (a).

**Definition.** For $a\in A$, the **inner derivation** by $a$ is

$$
\operatorname{ad}_a:A\to A,\qquad \operatorname{ad}_a(x)=ax-xa=[a,x].
$$

The inner derivations form a Lie ideal $\operatorname{Inn}(A)$ of $\operatorname{Der}(A)$, and the quotient $\operatorname{Der}(A)/\operatorname{Inn}(A)$ is the first cohomology $H^1(A,A)$ in the sense of *The Hochschild Differential as an Operator*.

**Proposition.** The map $a\mapsto\operatorname{ad}_a$ is a Lie algebra homomorphism $A\to\operatorname{Der}(A)$ with kernel $Z(A)$; its image is $\operatorname{Inn}(A)$. In particular every inner derivation kills $1$.

*Proof.* The Leibniz rule is the Jacobi identity:

$$
\operatorname{ad}_a(xy)=a xy-xy a=(ax-xa)y+x(ay-ya)=\operatorname{ad}_a(x)y+x\operatorname{ad}_a(y).
$$

The commutator of inner derivations is $[\operatorname{ad}_a,\operatorname{ad}_b]=\operatorname{ad}_{[a,b]}$, and $\operatorname{ad}_a=0$ exactly when $a$ is central.

### The derivation of an idempotent

**Theorem.** Let $\delta\in\operatorname{Der}(A)$ and let $e$ be an idempotent. Then

$$
\delta(e)=\delta(e)e+e\delta(e),
$$

and consequently $\delta(e)\in N=A_{01}\oplus A_{10}$.

*Proof.* Differentiate $e^2=e$:

$$
\delta(e)=\delta(e^2)=\delta(e)e+e\delta(e).
$$

Write $x=\delta(e)=x_{00}+x_{01}+x_{10}+x_{11}$ in the Peirce decomposition. Then

$$
xe=x_{00}+x_{10}, \qquad ex=x_{00}+x_{01},
$$

so the equation $x=xe+ex$ reads

$$
x_{00}+x_{01}+x_{10}+x_{11}=2x_{00}+x_{01}+x_{10}.
$$

Comparing components gives $x_{00}=0$ and $x_{11}=0$, hence $x=x_{01}+x_{10}\in N$.

**Remark (the tangent space).** The equation $\delta(e)=\delta(e)e+e\delta(e)$ is the algebraic form of the fact that the derivative of a projection is off-diagonal. If $t\mapsto e(t)$ is a differentiable path of idempotents in a real or complex algebra, then differentiating $e(t)^2=e(t)$ gives $e'(t)=e'(t)e(t)+e(t)e'(t)$, so $e'(t)\in N_{e(t)}$. The tangent space to the idempotent variety at $e$ is therefore $N$, and the Peirce decomposition is its tangent decomposition.

### Inner derivations and the evaluation map

**Proposition.** For $a=a_{00}+a_{01}+a_{10}+a_{11}\in A$,

$$
\operatorname{ad}_a(e)=a_{10}-a_{01}.
$$

In particular the evaluation map

$$
\operatorname{ev}_e:\operatorname{Der}(A)\longrightarrow N,\qquad \delta\longmapsto\delta(e),
$$

is surjective, and the inner derivations already realize every element of $N$: for $x=x_{01}+x_{10}\in N$, the element $a=-x_{01}+x_{10}$ satisfies $\operatorname{ad}_a(e)=x$.

*Proof.* $ae=a_{00}+a_{10}$ and $ea=a_{00}+a_{01}$, because $e$ selects the first column on the right and the first row on the left. The difference is $a_{10}-a_{01}$. For the surjectivity, take $a=-x_{01}+x_{10}$; then $a_{10}=x_{10}$ and $a_{01}=-x_{01}$, so $\operatorname{ad}_a(e)=x_{10}+x_{01}=x$.

**Remark.** The map $a\mapsto\operatorname{ad}_a(e)$ from $N$ to $N$ is the invertible linear map $a_{01}+a_{10}\mapsto a_{10}-a_{01}$, with inverse $x_{01}+x_{10}\mapsto -x_{01}+x_{10}$. Equivalently, the evaluation map induces an isomorphism $\operatorname{Der}(A)/\operatorname{Der}(A,e)\cong N$, and the inverse is $x\mapsto\operatorname{ad}_{-x_{01}+x_{10}}$.

## Peirce-Preserving Derivations

### Definition and the corner criterion

**Definition.** A derivation $\delta$ is **Peirce-preserving** when it preserves each corner:

$$
\delta(A_{ij})\subseteq A_{ij}\qquad\text{for all }i,j\in\{0,1\}.
$$

The set of Peirce-preserving derivations is written $\operatorname{Der}(A,e)$.

**Theorem.** For a derivation $\delta$, the following are equivalent.

**(a)** $\delta(e)=0$.

**(b)** $\delta(f)=0$.

**(c)** $\delta$ is Peirce-preserving.

*Proof.* (a)$\Leftrightarrow$(b): $\delta(f)=\delta(1-e)=-\delta(e)$. (a)$\Rightarrow$(c): for $a\in A_{ij}$,

$$
\delta(a)=\delta(e_i a e_j)=\delta(e_i)ae_j+e_i\delta(a)e_j+e_i a\delta(e_j)=e_i\delta(a)e_j\in A_{ij},
$$

because $\delta(e_i)=0$ for $i=0,1$. (c)$\Rightarrow$(a): $e\in A_{00}$, so $\delta(e)\in A_{00}$; but $\delta(e)\in N$ by the theorem of §*The derivation of an idempotent*, and $A_{00}\cap N=0$. Hence $\delta(e)=0$.

**Corollary.** $\operatorname{Der}(A,e)=\ker(\operatorname{ev}_e)$ is a Lie subalgebra of $\operatorname{Der}(A)$.

### The block matrix

**Theorem.** Let $\delta$ be Peirce-preserving. Then, relative to the ordered corners $(A_{00},A_{01},A_{10},A_{11})$, the block matrix of $\delta$ is diagonal:

$$
\delta=\operatorname{diag}(\delta_{00},\delta_{01},\delta_{10},\delta_{11}),
\qquad \delta_{ij}=\delta|_{A_{ij}}.
$$

Moreover:

**(a)** $\delta_{00}$ is a derivation of the corner algebra $A_{00}$, and $\delta_{11}$ is a derivation of $A_{11}$.

**(b)** $\delta_{01}$ is a derivation of the $A_{00}$-$A_{11}$ bimodule $A_{01}$: for $a\in A_{00}$, $x\in A_{01}$, $b\in A_{11}$,

$$
\delta_{01}(ax)=\delta_{00}(a)x+a\delta_{01}(x), \qquad
\delta_{01}(xb)=\delta_{01}(x)b+x\delta_{11}(b).
$$

**(c)** $\delta_{10}$ satisfies the same identities on the other side.

**(d)** The mixed blocks are coupled by the Leibniz rule on the products $A_{01}A_{10}\subseteq A_{00}$ and $A_{10}A_{01}\subseteq A_{11}$: for $x\in A_{01}$, $y\in A_{10}$,

$$
\delta_{00}(xy)=\delta_{01}(x)y+x\delta_{10}(y), \qquad
\delta_{11}(yx)=\delta_{10}(y)x+y\delta_{01}(x).
$$

*Proof.* (a) and (b) are the Leibniz rule restricted to the corners; (c) is the same on the other side; (d) is the Leibniz rule applied to $xy$ and $yx$.

**Remark.** The Peirce-preserving derivations are not simply a direct sum of four independent pieces. The corner derivations $\delta_{00}$ and $\delta_{11}$ and the bimodule derivations $\delta_{01},\delta_{10}$ are coupled by (d); the mixed part is a **derivation pair** or connection on the two mixed corners, and its curvature is measured by the failure of the two equations in (d) to be independent. The block matrix is diagonal, but the entries are not independent.

### The general derivation

**Theorem (the Peirce decomposition of a derivation).** Let $\delta\in\operatorname{Der}(A)$ and let $x=\delta(e)=x_{01}+x_{10}\in N$. Put $a=-x_{01}+x_{10}\in N$. Then

$$
\boxed{\;\delta=\operatorname{ad}_a+\delta_0,\qquad \delta_0\in\operatorname{Der}(A,e)\;},
$$

and the decomposition is unique with $a\in N$. Conversely, every pair $(a,\delta_0)\in N\times\operatorname{Der}(A,e)$ gives a derivation $\operatorname{ad}_a+\delta_0$.

*Proof.* By the proposition of §*Inner derivations and the evaluation map*, $\operatorname{ad}_a(e)=x=\delta(e)$, so $\delta_0=\delta-\operatorname{ad}_a$ kills $e$ and is Peirce-preserving. If $\operatorname{ad}_a+\delta_0=\operatorname{ad}_b+\delta_1$ with $a,b\in N$ and $\delta_0,\delta_1\in\operatorname{Der}(A,e)$, then $\operatorname{ad}_{a-b}=\delta_1-\delta_0$ kills $e$, so $(a-b)_{10}=(a-b)_{01}$. Since $a-b\in N$, both components vanish and $a=b$; then $\delta_0=\delta_1$.

**Corollary.** As vector spaces,

$$
\boxed{\;\operatorname{Der}(A)=\operatorname{Inn}(A)+\operatorname{Der}(A,e)\;},
$$

and the intersection is $\operatorname{ad}_D$, the inner derivations by the diagonal part $D=A_{00}\oplus A_{11}$. The evaluation map gives the exact sequence

$$
0\longrightarrow\operatorname{Der}(A,e)\longrightarrow\operatorname{Der}(A)\xrightarrow{\ \operatorname{ev}_e\ }N\longrightarrow0.
$$

The sequence splits as vector spaces by the section $x\mapsto\operatorname{ad}_{-x_{01}+x_{10}}$; the splitting is not a Lie algebra homomorphism.

*Proof.* The sum and intersection are the theorem with $a\in N$: every derivation is inner plus Peirce-preserving, and an inner derivation $\operatorname{ad}_a$ kills $e$ exactly when $a\in D$. The exact sequence is the definition of the kernel and the surjectivity of $\operatorname{ev}_e$. The section is linear and $\operatorname{ev}_e(\operatorname{ad}_{-x_{01}+x_{10}})=x$; it does not preserve brackets in general, because $N$ is not a Lie algebra.

**Theorem (the block shape).** In the decomposition $\delta=\operatorname{ad}_a+\delta_0$ with $a=a_{01}+a_{10}\in N$:

**(a)** $\delta_0$ has the diagonal block matrix of §*The block matrix*.

**(b)** $\operatorname{ad}_{a_{01}}$ has the corner-shifting blocks

$$
A_{00}\to A_{01},\quad A_{01}\to0,\quad A_{10}\to A_{00}\oplus A_{11},\quad A_{11}\to A_{01}.
$$

**(c)** $\operatorname{ad}_{a_{10}}$ has the mirror blocks

$$
A_{00}\to A_{10},\quad A_{01}\to A_{00}\oplus A_{11},\quad A_{10}\to0,\quad A_{11}\to A_{10}.
$$

In particular the off-diagonal blocks of $\delta$ are exactly those of the inner part $\operatorname{ad}_a$; the Peirce-preserving part contributes only the diagonal blocks.

*Proof.* For $a=a_{01}$, compute $\operatorname{ad}_a(x)=a x-x a$ on each corner. On $A_{00}$: $a x\in A_{01}$ and $xa=0$. On $A_{01}$: both products vanish. On $A_{10}$: $a x\in A_{00}$ and $xa\in A_{11}$. On $A_{11}$: $a x=0$ and $xa\in A_{01}$. The case $a=a_{10}$ is the mirror image. The sum $a=a_{01}+a_{10}$ gives the sum of the two block patterns, and $\delta_0$ is diagonal.

**Remark.** The block shape is the precise sense in which a derivation is a **first-order** operator on the Peirce decomposition: it can preserve the corner, or shift it by one off-diagonal step, but it cannot move a corner by two steps. The inner derivation by $a_{01}$ sends the diagonal corner $A_{00}$ to the mixed corner $A_{01}$ and the mixed corner $A_{10}$ to the two diagonal corners; the pattern is the Peirce form of the commutator with an off-diagonal element.

## The Central Simple Case

**Theorem.** Let $A$ be a finite-dimensional central simple algebra over $k$. Then every derivation of $A$ is inner:

$$
\boxed{\;\operatorname{Der}(A)=\operatorname{Inn}(A)\cong A/Z(A)\;}.
$$

Consequently

$$
\operatorname{Der}(A,e)=\operatorname{ad}_D,
$$

and the evaluation map is the surjection

$$
\operatorname{ad}_A\longrightarrow N,\qquad \operatorname{ad}_a\longmapsto a_{10}-a_{01},
$$

with kernel $\operatorname{ad}_D$.

*Proof.* The innerness of every derivation is the Skolem–Noether theorem in its derivation form, or the vanishing of $H^1(A,A)$ for a central simple algebra; it is stated in *Central Simple Algebras and the Brauer Group*. A derivation killing $e$ is then $\operatorname{ad}_a$ with $a_{10}=a_{01}$, hence $a\in D$; conversely every $\operatorname{ad}_d$ with $d\in D$ kills $e$. The kernel of the evaluation is therefore $\operatorname{ad}_D$, and the image is $N$ by the surjectivity of §*Inner derivations and the evaluation map*.

**Corollary.** For $A=M_n(k)$ and $e$ of rank $r$, the derivations are the inner derivations $\operatorname{ad}_a$, the Peirce-preserving ones are $\operatorname{ad}_d$ with $d$ block diagonal in the Peirce decomposition, and

$$
\dim\operatorname{Der}(A)=n^2-1,\qquad
\dim N=2r(n-r),\qquad
\dim\operatorname{Der}(A,e)=\dim D-1.
$$

*Proof.* The derivations of $M_n(k)$ are inner, with kernel the scalars, so the dimension is $n^2-1$. The off-diagonal part has dimension $r(n-r)+(n-r)r=2r(n-r)$. The diagonal part $D=M_r(k)\oplus M_{n-r}(k)$ has dimension $r^2+(n-r)^2$, and $\operatorname{ad}_D$ has dimension $\dim D-1$. The exact sequence gives the same total.

**Example (the matrix algebra $M_2(k)$).** Let $e=E_{11}$, $f=E_{22}$. The derivations are $\operatorname{ad}_a$ for $a\in M_2(k)$, a three-dimensional Lie algebra isomorphic to $\mathfrak{sl}_2(k)$. The Peirce-preserving derivations are $\operatorname{ad}_d$ for $d=\operatorname{diag}(d_0,d_1)$, a one-dimensional algebra modulo the scalars. On the mixed corners,

$$
\operatorname{ad}_d(E_{12})=(d_0-d_1)E_{12},\qquad
\operatorname{ad}_d(E_{21})=(d_1-d_0)E_{21},
$$

and $\operatorname{ad}_d$ kills the diagonal corners. The evaluation map $\operatorname{ad}_a\mapsto a_{10}-a_{01}$ is the map from the three-dimensional $\mathfrak{sl}_2$ onto the two-dimensional $N$, with the one-dimensional diagonal kernel. The example is the smallest case of the exact sequence.

**Example (the dual numbers).** Let $A=k[\varepsilon]/(\varepsilon^2)$ with $2\neq0$, and let $e=1$. The only nontrivial idempotent is $1$, so for this $e$ the off-diagonal part vanishes: $N=0$ and $\operatorname{Der}(A,e)=\operatorname{Der}(A)$. A derivation is determined by $\delta(\varepsilon)=b\varepsilon$, because the relation $\varepsilon^2=0$ forces $2\varepsilon\delta(\varepsilon)=0$; the derivations are the one-dimensional space

$$
\delta_b(x+y\varepsilon)=yb\,\varepsilon,\qquad b\in k,
$$

spanned by $\delta_1(\varepsilon)=\varepsilon$, and they all kill $e$. The exact sequence is $0\to\operatorname{Der}(A)\to\operatorname{Der}(A)\to0$. The example is the degenerate case in which the off-diagonal part vanishes and every derivation is Peirce-preserving; the nonzero derivations are outer.

**Example (the split algebra).** Let $A=k\times k$ with $e=(1,0)$, $f=(0,1)$. The algebra is commutative semisimple, so $\operatorname{Der}(A)=0$; the Peirce decomposition has $N=0$, and the exact sequence is trivial. The example is the other extreme: no derivations, no off-diagonal part.

## The Hochschild Reading

The derivation complex is the first degree of the Hochschild complex. For a $1$-cochain $f:A\to A$, the Hochschild differential is

$$
(df)(a,b)=a f(b)-f(ab)+f(a)b,
$$

and $df=0$ is exactly the Leibniz rule: the $1$-cocycles are the derivations. The $1$-coboundaries are the inner derivations $f=\operatorname{ad}_a$ (up to the sign convention of the cochain complex), so

$$
Z^1(A,A)=\operatorname{Der}(A),\qquad B^1(A,A)=\operatorname{Inn}(A),\qquad H^1(A,A)=\operatorname{Der}(A)/\operatorname{Inn}(A).
$$

The evaluation at $e$ is a linear map

$$
\operatorname{ev}_e:Z^1(A,A)\longrightarrow N,
$$

and the exact sequence of §*The general derivation* is the Peirce decomposition of the cocycle space:

$$
0\longrightarrow Z^1_e(A,A)\longrightarrow Z^1(A,A)\longrightarrow N\longrightarrow0,
$$

where $Z^1_e(A,A)=\operatorname{Der}(A,e)$ is the space of cocycles killing $e$. The sequence is the first-degree shadow of the Peirce decomposition of the Hochschild complex; the higher degrees are the subject of *The Hochschild Differential as an Operator*.

**Remark.** The cohomological reading explains why the evaluation at an idempotent is so useful: it is a canonical map from the first cocycles to the off-diagonal part, and its kernel is the subcomplex of derivations that preserve the Peirce decomposition. The map is not a Lie algebra homomorphism, because $N$ is only a vector space; the Lie algebra structure lives on the kernel and on the total space.

## Summary

A derivation $\delta$ of $A$ satisfies $\delta(e)=\delta(e)e+e\delta(e)$ for every idempotent $e$, and hence $\delta(e)\in N=A_{01}\oplus A_{10}$. The evaluation map $\operatorname{ev}_e:\operatorname{Der}(A)\to N$, $\delta\mapsto\delta(e)$, is surjective; the inner derivation by $a=-x_{01}+x_{10}$ realizes the value $x=x_{01}+x_{10}$. The kernel is the Lie algebra $\operatorname{Der}(A,e)$ of Peirce-preserving derivations, equivalently the derivations killing $e$; these are exactly the derivations whose block matrix relative to the four corners is diagonal. Every derivation decomposes uniquely as

$$
\delta=\operatorname{ad}_a+\delta_0,\qquad a\in N,\quad \delta_0\in\operatorname{Der}(A,e),
$$

and the decomposition gives the exact sequence $0\to\operatorname{Der}(A,e)\to\operatorname{Der}(A)\to N\to0$, split as vector spaces. The Peirce-preserving part has diagonal blocks that are derivations of the corner algebras and bimodule derivations of the mixed corners, coupled by the Leibniz rule on $A_{01}A_{10}$ and $A_{10}A_{01}$; the inner part has the corner-shifting blocks of $\operatorname{ad}_{a_{01}}$ and $\operatorname{ad}_{a_{10}}$. In the central simple case every derivation is inner, $\operatorname{Der}(A,e)=\operatorname{ad}_D$, and the evaluation is the surjection $\operatorname{ad}_A\to N$ with kernel $\operatorname{ad}_D$. The matrix algebra $M_2(k)$, the dual numbers and the split algebra are the worked examples, and the Hochschild reading identifies the derivations with the $1$-cocycles and the Peirce-preserving derivations with the cocycles killing $e$. No form, involution or topology is used.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{Der}(A)$ | the Lie algebra of derivations of $A$ |
| $\operatorname{Inn}(A)$ | the inner derivations $\operatorname{ad}_a$ |
| $\operatorname{ad}_a(x)=ax-xa$ | the inner derivation by $a$ |
| $\operatorname{Der}(A,e)$ | the derivations killing $e$ |
| $\operatorname{ev}_e(\delta)=\delta(e)$ | the evaluation at $e$ |
| $D=A_{00}\oplus A_{11}$ | the diagonal Peirce part |
| $N=A_{01}\oplus A_{10}$ | the off-diagonal part |
| $Z^1(A,A),B^1(A,A),H^1(A,A)$ | Hochschild cocycles, coboundaries, cohomology |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the Peirce decomposition and the derivations of the classical algebras.
- Nathan Jacobson, *Basic Algebra II* (Freeman, 1989), for derivations, inner derivations and the central simple case.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2001), for the derivation algebra of a matrix ring and the Skolem–Noether theorem.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the derivations and the Peirce decompositions of the classical algebras.
