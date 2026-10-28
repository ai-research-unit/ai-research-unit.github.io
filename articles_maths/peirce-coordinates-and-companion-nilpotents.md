# __Peirce Coordinates and Companion Nilpotents__

## Introduction

An idempotent $e$ of a unital algebra $A$ cuts the algebra into four corners. Two of them are algebras, the diagonal corners $eAe$ and $fAf$ with $f=1_A-e$; the other two are square-zero, and their elements are nilpotents. The corner $fAe$ is the **companion corner** of $e$: it is the part of the algebra that a left multiplication by $e$ kills and a right multiplication by $e$ preserves. Its elements are the **companion nilpotents**.

The object a spinor is read from is not a corner by itself but the subspace

$$
C(e)=Ae=eAe\oplus fAe,
$$

the part of $A$ fixed on the right by $e$. It is the set of $x$ with $xe=x$, it is stable under left multiplication, and it is acted on by the corner algebra $D=eAe$. The companion corner supplies the extra coordinates; the diagonal corner supplies the coefficients. This is the coordinate description that the Peirce decomposition gives, and it uses no module theory and no matrix model.

Three results organise the article. First, the four corners are the joint eigenspaces of the left and the right multiplication by $e$, and the two mixed corners are square-zero. Second, the carrier splits as $C(e)=D\oplus fAe$, and the number

$$
s=\text{least number of generators of }fAe\text{ over }D
$$

is the number of companion directions; the coordinate vector has $1+s$ entries over $D$. Third, the frame root $h=2e-1_A$ acts on the carrier by $+1$ on $D$ and $-1$ on the companion corner, so the Peirce decomposition supplies a canonical $\mathbb{Z}_2$ grading and nothing finer.

**Setting.** Throughout, $k$ is a field, $A$ is a finite-dimensional unital associative $k$-algebra with $1_A\neq0$, $e\in A$ is an idempotent, $f=1_A-e$, and $D=eAe$. The corners are

$$
A_{++}=eAe,\qquad A_{+-}=eAf,\qquad A_{-+}=fAe,\qquad A_{--}=fAf .
$$

The characteristic is not $2$ where the halving $e=(1_A+h)/2$ is used. The one-idempotent Peirce decomposition is *Unital Algebras*, §*Idempotents and the Peirce Decomposition*; the complete family is *Complementary Idempotents and the Peirce Decomposition*; the off-diagonal part is *Off-Diagonal Peirce Components and Noncentral Idempotents*; the primitive case is *Primitive Idempotents and Minimal Left Ideals*; and the operator reading of the corners is *Left and Right Multiplication on the Diagonal Peirce Part*.

## The Four Corners

**Definition.** The **Peirce corners** of $e$ are the four subspaces $A_{st}=e_sAe_t$, with $e_+=e$ and $e_-=f$. The **companion corner** of $e$ is $A_{-+}=fAe$, and a **companion nilpotent** is a nonzero element of it.

**Proposition (the corners are the joint eigenspaces).** The operators $L_e(x)=ex$ and $R_e(x)=xe$ commute, are idempotent, and on the corners take the values

| corner | $L_e$ | $R_e$ |
|---|---|---|
| $A_{++}$ | $1$ | $1$ |
| $A_{+-}$ | $1$ | $0$ |
| $A_{-+}$ | $0$ | $1$ |
| $A_{--}$ | $0$ | $0$ |

*Proof.* For $x=e_sxe_t$, $ex=e(e_sxe_t)=\delta_{s+}x$ and $xe=(e_sxe_t)e=\delta_{t+}x$, because $e_+e_-=e_-e_+=0$ and $e_\pm^2=e_\pm$. The four sign pairs are distinct, so the corners are exactly the joint eigenspaces and $A$ is their direct sum.

**Proposition (the multiplication table).** $A_{st}A_{uv}\subseteq\delta_{tu}A_{sv}$.

*Proof.* $(e_sAe_t)(e_uAe_v)=e_sA(e_te_u)Ae_v$, and $e_te_u=\delta_{tu}e_t$.

**Proposition (the mixed corners are square-zero).** $A_{+-}^2=0$ and $A_{-+}^2=0$. Consequently every element of a mixed corner is nilpotent of index at most two.

*Proof.* $A_{+-}^2=eAf\,eAf=eA(fe)Af=0$, and $A_{-+}^2=fAe\,fAe=fA(ef)Ae=0$.

**Remark.** The converse fails: an off-diagonal element need not be square-zero. In $M_2(k)$ the element $E_{12}+E_{21}$ is off-diagonal for $e=E_{11}$ and satisfies $(E_{12}+E_{21})^2=1_A$. Square-zero is a property of the mixed *corner*, not of every element with zero diagonal coordinates.

## The Companion Corner

**Definition.** The **companion count** of $e$ is

$$
s=\min\{\,r:\ \exists\,\nu_1,\dots,\nu_r\in A_{-+},\ A_{-+}=\nu_1D+\dots+\nu_rD\,\},
$$

the least number of elements of $A_{-+}$ that generate it by right multiplication by $D=eAe$. A family $(\nu_1,\dots,\nu_s)$ attaining the minimum is a **companion frame**, and its elements are the **companion nilpotents** of the frame.

**Proposition.** Every $\nu\in A_{-+}$ satisfies $\nu^2=0$. The corner is annihilated on the left by $A_{++}$, mapped into itself by $A_{--}$, and mapped into $A_{++}$ by $A_{+-}$:

$$
A_{++}A_{-+}=0,\qquad A_{--}A_{-+}\subseteq A_{-+},\qquad A_{+-}A_{-+}\subseteq A_{++}.
$$

*Proof.* The first claim is the square-zero proposition. The three inclusions are the multiplication table $A_{st}A_{uv}\subseteq\delta_{tu}A_{sv}$ with $u=-$, $v=+$ and $s=+,-,+$ respectively.

**Remark (the corner need not be free).** The number $s$ is a number of generators, not a dimension. When $D$ is a division ring, every right $D$-module is free and $s=\dim_D A_{-+}$. When $D$ is not a division ring, $A_{-+}$ can be cyclic and still have a relation: a single generator $\nu$ with a nonzero annihilator $\{d\in D:\nu d=0\}$ generates a module smaller than $D$. The coordinate description below distinguishes the two cases.

**Examples.** The count depends on the corner algebra, not on the dimension of $A$ alone.

| algebra | $e$ | $D=eAe$ | $\dim_k A_{-+}$ | $s$ |
|---|---|---|---|---|
| $\mathbb{B}=M_2(\mathbb{C})$ | $\tilde\Pi_+$ | $\mathbb{C}$ | $1$ | $1$ |
| $M_2(k)$ | $E_{11}$ | $k$ | $1$ | $1$ |
| $M_3(k)$ | $E_{11}$ | $k$ | $2$ | $2$ |
| $M_3(k)$ | $E_{11}+E_{22}$ | $M_2(k)$ | $2$ | $1$ |
| $M_4(k)$ | $E_{11}$ | $k$ | $3$ | $3$ |
| $M_4(k)$ | $E_{11}+E_{22}$ | $M_2(k)$ | $4$ | $1$ |
| $M_5(k)$ | $E_{11}+E_{22}$ | $M_2(k)$ | $6$ | $2$ |
| $\mathbb{H}$ | $1_A$ | $\mathbb{H}$ | $0$ | $0$ |
| $T_2(k)$ | $E_{22}$ | $k$ | $1$ | $1$ |
| $k[\varepsilon]$ | $1_A$ | $k[\varepsilon]$ | $0$ | $0$ |
| commutative $A$ | any $e$ | $eAe$ | $0$ | $0$ |

The last row is the commutative case: $fAe=feA=0$, so there is no companion corner and no companion nilpotent. The dual numbers show that $s=0$ does not imply that the carrier is small: $C(1_A)=A$ is the whole algebra, and the nilpotent $\varepsilon$ lies in the diagonal corner $D$, not in a companion corner.

## The Count in a Matrix Algebra

**Theorem.** Let $A=M_N(k)$ and let $e$ be an idempotent of rank $r$, $1\le r\le N$. Then $D=eAe\cong M_r(k)$ and

$$
s=\left\lceil\frac{N-r}{r}\right\rceil=\left\lceil\frac Nr\right\rceil-1 .
$$

In particular, for a primitive idempotent, $r=1$ and $s=N-1$.

*Proof.* The corner $A_{-+}=fAe$ is the space of $(N-r)\times r$ matrices, a right $M_r(k)$-module. Write $S=k^r$ for the row space, the simple right $M_r$-module. Then $A_{-+}\cong S^{N-r}$: each of the $N-r$ rows is an element of $S$, and right multiplication acts on each row. The direct sum $S^r$ is the space of $r\times r$ matrices, which is $M_r(k)$ itself, free of rank one. Grouping the $N-r$ copies of $S$ into blocks of $r$ therefore gives $\lceil (N-r)/r\rceil$ free blocks, one generator per block. No fewer can suffice, because one generator spans a cyclic submodule of dimension at most $r^2$, that is at most $r$ copies of $S$.

**Corollary.** For a primitive idempotent of $M_N(k)$, $s=N-1$ and $1+s=N$. The number of companion directions is one exactly when $N=2$.

**Remark.** The theorem is a statement about generators, not about the dimension of the corner. For $r\ge2$ the corner $A_{-+}$ has $r(N-r)$ parameters but is generated by $\lceil (N-r)/r\rceil$ elements over $M_r(k)$. The two numbers agree only at $r=1$.

## The Carrier and Its Coordinates

**Definition.** The **Peirce carrier** of $e$ is

$$
C(e)=Ae=\{\,x\in A:\ xe=x\,\}.
$$

**Proposition.** $C(e)=A_{++}\oplus A_{-+}=D\oplus fAe$, and left multiplication by any $a\in A$ maps $C(e)$ into itself.

*Proof.* If $x=ae$ then $xe=ae^2=ae=x$; conversely $xe=x$ gives $x=xe\in Ae$. The Peirce decomposition of $x\in Ae$ has only the corners with right index $+$, that is $A_{++}$ and $A_{-+}$. If $x\in Ae$ then $(ax)e=a(xe)=ax$, so $ax\in Ae$.

**Theorem (coordinates).** Let $(\nu_1,\dots,\nu_s)$ generate $A_{-+}$ over $D$. Then every $\xi\in C(e)$ is of the form

$$
\xi=d_0+\nu_1d_1+\dots+\nu_sd_s,\qquad d_0,d_1,\dots,d_s\in D,
$$

and the expression is unique when $(\nu_1,\dots,\nu_s)$ is a $D$-basis of $A_{-+}$. In that case the **coordinate vector** of $\xi$ is

$$
(d_0;d_1,\dots,d_s)\in D^{1+s},
$$

and the $1+s$ entries are the coordinates, one on the idempotent and one on each companion nilpotent.

*Proof.* The sum $D+fAe$ is direct because $A_{++}\cap A_{-+}=0$. If the generators are a basis, the expansion of an element of $fAe$ is unique, and $D\cap fAe=0$ gives uniqueness of $d_0$.

**Remark (when the coordinates are unique).** The expansion is a basis exactly when $A_{-+}$ is free over $D$. This holds when $D$ is a division ring, in particular when $A$ is semisimple and $e$ is primitive. It fails in general. In $M_3(k)$ with $e=E_{11}+E_{22}$, $D=M_2(k)$, $s=1$, and $A_{-+}$ is the $1\times2$ row space, of $k$-dimension $2$ against $\dim_k D=4$: the single generator has a nonzero annihilator, and the expansion is a presentation, not a basis. The coordinate vector then has repeated descriptions.

## The Peirce Matrix

**Proposition (the left action in coordinates).** Let $x\in A$ and write

$$
x e=p_0+\sum_{j=1}^{s}\nu_jp_j,\qquad
x\nu_i=q_{0i}+\sum_{j=1}^{s}\nu_jq_{ji},
\qquad p_j,q_{ji}\in D .
$$

Then for $\xi=d_0+\sum_i\nu_id_i$,

$$
x\xi=\Bigl(p_0d_0+\sum_iq_{0i}d_i\Bigr)
+\sum_j\nu_j\Bigl(p_jd_0+\sum_iq_{ji}d_i\Bigr).
$$

The **Peirce matrix** of $x$ on $C(e)$ is therefore the $(1+s)\times(1+s)$ matrix over $D$

$$
P(x)=
\begin{pmatrix}
p_0 & q_{01} & \cdots & q_{0s}\\
p_1 & q_{11} & \cdots & q_{1s}\\
\vdots & \vdots & & \vdots\\
p_s & q_{s1} & \cdots & q_{ss}
\end{pmatrix},
\qquad
P(x)\,(d_0,d_1,\dots,d_s)^{\mathsf T}
=(d_0',d_1',\dots,d_s')^{\mathsf T}.
$$

*Proof.* Expand $x\xi=x(ed_0)+\sum_i x(\nu_id_i)=(xe)d_0+\sum_i(x\nu_i)d_i$ by associativity, substitute the two expansions, and collect the coefficients of $e$ and of the $\nu_j$.

**Example (the biquaternion).** Let $A=\mathbb{B}$, $e=\tilde\Pi_+$, $f=\tilde\Pi_-$, $\nu_1=\vec\Upsilon_y$. Then $D=\mathbb{C}\tilde\Pi_+\cong\mathbb{C}$ and

$$
C(\tilde\Pi_+)=\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\vec\Upsilon_y .
$$

For $x=a\tilde\Pi_+ + b\vec\Upsilon_x + c\vec\Upsilon_y + d\tilde\Pi_-$ one has $x\tilde\Pi_+=a\tilde\Pi_+ + c\vec\Upsilon_y$ and $x\vec\Upsilon_y=b\tilde\Pi_+ + d\vec\Upsilon_y$, so the Peirce matrix is

$$
P(x)=\begin{pmatrix}a&b\\ c&d\end{pmatrix}.
$$

The matrix model is recovered as the Peirce matrix in the frame, not assumed.

**Example (the matrix algebra).** For $A=M_N(k)$ and $e=E_{11}$, $D=k$, $s=N-1$, $\nu_i=E_{i+1,1}$, and $C(e)$ is the first column. The Peirce matrix of $x$ is $x$ itself, read on the first column with the first entry as $d_0$.

## The Grading Element

**Definition.** The **frame root** of $e$ is

$$
h=2e-1_A=e-f .
$$

**Proposition.** $h^2=1_A$. The left multiplication $L_h$ has eigenvalue $+1$ on $A_{++}$ and $A_{+-}$ and $-1$ on $A_{-+}$ and $A_{--}$; the right multiplication $R_h$ has eigenvalue $+1$ on $A_{++}$ and $A_{-+}$ and $-1$ on $A_{+-}$ and $A_{--}$. The inner derivation $\operatorname{ad}_h=L_h-R_h$ has eigenvalues $0$ on the diagonal corners and $+2$ on $A_{+-}$, $-2$ on $A_{-+}$.

*Proof.* On $A_{st}$, $L_h$ is $+1$ for $s=+$ and $-1$ for $s=-$, and $R_h$ is $+1$ for $t=+$ and $-1$ for $t=-$. The difference is $s-t$.

**Corollary.** On the carrier $C(e)$ the left multiplication by $h$ has eigenvalue $+1$ on $D$ and $-1$ on the companion corner. The Peirce decomposition therefore supplies a canonical $\mathbb{Z}_2$ grading of the carrier, with the companion coordinates in the odd part. It supplies no finer splitting: the odd part is a single eigenspace, of dimension $\dim_k fAe$ over $k$.

**Remark.** The grading element is canonical, but the grading is only $\mathbb{Z}_2$. A weight string of the form $\lambda,\lambda-2,\dots,-\lambda$ needs an $\mathfrak{sl}_2$ triple, not one idempotent. The triple and the spin number are the subject of *The Weight of a Frame Root and the Spin Quantum Number*; the definition of the spinor read from $C(e)$ is *Spinors as Peirce Coordinates*.

## Summary

An idempotent gives four corners, the joint eigenspaces of $L_e$ and $R_e$, with the multiplication table $A_{st}A_{uv}\subseteq\delta_{tu}A_{sv}$. The mixed corners are square-zero, so every element of $fAe$ is a companion nilpotent. The carrier $C(e)=Ae=D\oplus fAe$ is the fixed space of $R_e$ and is stable under left multiplication. The companion count $s$ is the least number of generators of $fAe$ over $D=eAe$, and the coordinate vector has $1+s$ entries over $D$; it is a basis exactly when $fAe$ is free, which holds when $D$ is a division ring. In $M_N(k)$ with an idempotent of rank $r$, $s=\lceil N/r\rceil-1$, and for a primitive idempotent $s=N-1$, so the biquaternion case $N=2$ is the only one with a single companion. The frame root $h=2e-1_A$ gives the $\mathbb{Z}_2$ grading of the carrier, with $+1$ on $D$ and $-1$ on the companion corner.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $k$ | A field |
| $A$ | A finite-dimensional unital associative $k$-algebra |
| $1_A$ | The identity of $A$ |
| $e$ | An idempotent, $e^2=e$ |
| $f$ | The complement $1_A-e$ |
| $A_{st}=e_sAe_t$ | The Peirce corners, $e_+=e$, $e_-=f$ |
| $D=eAe$ | The diagonal corner algebra with identity $e$ |
| $fAe=A_{-+}$ | The companion corner, square-zero |
| $s$ | The least number of generators of $fAe$ over $D$ |
| $C(e)=Ae$ | The Peirce carrier, the fixed space of $R_e$ |
| $h=2e-1_A$ | The frame root |
| $L_h,R_h,\operatorname{ad}_h$ | Left, right and inner-derivation action of $h$ |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the Peirce decomposition and the corners.
- Yurij A. Drozd and Vladimir V. Kirichenko, *Finite Dimensional Algebras* (Springer, 1994), for the refinement to primitive idempotents and the local corners.
- Frank W. Anderson and Kent R. Fuller, *Rings and Categories of Modules* (Springer, 2nd ed. 1992), for idempotents and the direct summands of the regular module.
- Tsit-Yuen Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for the corner algebras and the lifting of idempotents.
- The corpus article *Complementary Idempotents and the Peirce Decomposition*, for the complete family, and *Off-Diagonal Peirce Components and Noncentral Idempotents*, for the commutator reading of the mixed corners.
