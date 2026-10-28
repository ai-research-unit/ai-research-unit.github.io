# __The Frame, the Simple Nilpotents and the Gauge__

## Introduction

**The root fixes the flag, and a frame fixes one vector in each line of the flag; the freedom in that choice is a torus with one parameter per simple nilpotent.** The root therefore gives the idempotents and the lines, and the gauge gives the vectors and the units. The two together are the frame.

The article constructs the frame from a basis adapted to the spectral flag, states the matrix-unit rule, isolates the three simple nilpotents $E_{12},E_{23},E_{34}$, computes the gauge action and its cocycle, and counts the parameters: $12$ complex from the root and $3$ complex from the gauge, $15$ in all. The idempotents are gauge invariant. The gauge is not a second root: at $n=2$ the old "second root" is exactly a point of the gauge, and for $n=4$ there is no second root at all, only the three parameters.

The idempotents are from *Roots of Unity and the Lagrange Idempotents*; the corners are *The Peirce Decomposition*; the spin chain that uses the nilpotents as ladder steps is *The Spin Chain and the Adjoint Decomposition*; the count of the root set is *The Adjoint Action, the Orbits and the Flag Variety*. The general construction is *The Frame, the Simple Nilpotents and the Gauge* for $M_n(\mathbb{C})$.

## The Adapted Frame

**Definition.** A **frame adapted to the root** $H$ is a basis $(v_1,v_2,v_3,v_4)$ of $\mathbb{C}^4$ with

$$
v_k\in V_k=\operatorname{im}P_k,\qquad v_k\ne0,\qquad k=1,2,3,4.
$$

Let $(\ell_1,\ell_2,\ell_3,\ell_4)$ be the dual basis of the dual space, $\ell_k(v_m)=\delta_{km}$, and put

$$
E_{kl}=v_k\ell_l .
$$

**Proposition.** The sixteen elements $E_{kl}$ are a basis of $M_4(\mathbb{C})$. They satisfy

$$
E_{kl}E_{mn}=\delta_{lm}E_{kn},\qquad
E_{kk}=P_k,\qquad
H=\sum_{k=1}^{4}\zeta_kE_{kk},\qquad
\operatorname{tr}E_{kl}=\delta_{kl}.
$$

**Proof.** For $v\in\mathbb{C}^4$, write $v=\sum_m\ell_m(v)v_m$. Then

$$
E_{kl}E_{mn}v=v_k\ell_l\bigl(v_m\ell_n(v)\bigr)=\delta_{lm}v_k\ell_n(v)=\delta_{lm}E_{kn}v.
$$

On $v_m$, $E_{kk}$ acts as $v_k\ell_k(v_m)=\delta_{km}v_k$, so $E_{kk}=P_k$. The sum $\sum_k\zeta_kE_{kk}$ acts on $v_m$ as $\zeta_mv_m=Hv_m$. The trace is $\ell_l(v_k)=\delta_{kl}$. The sixteen units are the matrix units of the basis, hence a basis of the algebra.

**The frame is the choice of the vectors.** The root fixes the four lines. The frame fixes a nonzero vector in each line. Different frames of the same flag give different matrix units and the same idempotents:

$$
E_{kk}=P_k
$$

depends only on the line $V_k$, not on the vector $v_k$.

### The Standard Frame and a Non-Standard One

In the **standard frame** $v_k=e_k$ and $\ell_k=e_k^{\mathsf T}$, the units $E_{kl}$ are the coordinate matrix units, $P_k=E_{kk}$, and $H=H_0=\operatorname{diag}(1,i,-1,-i)$.

In a general frame the units are the outer products $v_k\ell_l$. For the upper triangular frame of *Roots of Unity and the Lagrange Idempotents*,

$$
v_1=\begin{pmatrix}1\\0\\0\\0\end{pmatrix},\quad
v_2=\begin{pmatrix}1\\1\\0\\0\end{pmatrix},\quad
v_3=\begin{pmatrix}0\\1\\1\\0\end{pmatrix},\quad
v_4=\begin{pmatrix}0\\0\\1\\1\end{pmatrix},
$$

with dual functionals

$$
\ell_1=(1,-1,1,-1),\quad
\ell_2=(0,1,-1,1),\quad
\ell_3=(0,0,1,-1),\quad
\ell_4=(0,0,0,1),
$$

the first units are

$$
E_{12}=v_1\ell_2=
\begin{pmatrix}0&1&-1&1\\0&0&0&0\\0&0&0&0\\0&0&0&0\end{pmatrix},
$$

$$
E_{23}=v_2\ell_3=
\begin{pmatrix}0&0&1&-1\\0&0&1&-1\\0&0&0&0\\0&0&0&0\end{pmatrix},
$$

$$
E_{34}=v_3\ell_4=
\begin{pmatrix}0&0&0&0\\0&0&0&1\\0&0&0&1\\0&0&0&0\end{pmatrix}.
$$

They are not the coordinate matrix units, and their entries are not zeros and ones only. The frame, not the standard basis, is the data.

## The Simple Nilpotents

**Definition.** The **simple nilpotents** of the frame are the three superdiagonal units

$$
N_1=E_{12},\qquad N_2=E_{23},\qquad N_3=E_{34}.
$$

**Proposition.** Each simple nilpotent squares to zero:

$$
N_1^2=N_2^2=N_3^2=0.
$$

The composites are the products of consecutive simple nilpotents:

$$
E_{13}=N_1N_2,\qquad E_{24}=N_2N_3,\qquad E_{14}=N_1N_2N_3.
$$

The subdiagonal units are

$$
E_{21}=N_1^{*},\qquad E_{32}=N_2^{*},\qquad E_{43}=N_3^{*}
$$

in an orthonormal frame, and in a general frame they are the dual units $E_{k+1,k}$. The diagonal units are recovered by the product rule:

$$
E_{11}=E_{12}E_{21},\quad
E_{22}=E_{23}E_{32},\quad
E_{33}=E_{34}E_{43},\quad
E_{44}=E_{43}E_{34}.
$$

**Proof.** $N_k^2=E_{k,k+1}E_{k,k+1}=0$ because the inner indices do not match. The composite formulas are the product rule $E_{k,k+1}E_{k+1,k+2}=E_{k,k+2}$ iterated. The subdiagonal identity is the definition of the conjugate transpose in an orthonormal frame; in a general frame the subdiagonal unit $E_{k+1,k}=v_{k+1}\ell_k$ is the dual unit, not the conjugate transpose of $N_k$ with respect to the standard inner product. The diagonal identities are the product rule with $E_{k,k+1}E_{k+1,k}=E_{kk}$ and $E_{k+1,k}E_{k,k+1}=E_{k+1,k+1}$.

**The simple nilpotents generate the frame.** The algebra generated by $N_1,N_2,N_3$ and the subdiagonal units $E_{21},E_{32},E_{43}$ is the whole of $M_4(\mathbb{C})$. The products of consecutive $N$'s give all $E_{kl}$ with $k<l$; the subdiagonal units give all $E_{kl}$ with $k>l$ by the same product rule; the diagonal is recovered as above. In an orthonormal frame the subdiagonal units are the conjugate transposes $N_k^{*}$, so the algebra generated by the simple nilpotents and their conjugate transposes is all of $M_4(\mathbb{C})$. The **strictly upper triangular algebra** generated by $N_1,N_2,N_3$ alone has the basis

$$
N_1,\ N_2,\ N_3,\ N_1N_2,\ N_2N_3,\ N_1N_2N_3,
$$

of dimension $6$; it is the algebra of the flag, and the lower triangular algebra is generated by the subdiagonal units.

**The chain is the Peirce chain.** The nilpotent $N_k$ maps the line $V_{k+1}$ to the line $V_k$ and kills the other lines. In the Peirce notation of *The Peirce Decomposition*,

$$
N_k\in\mathcal{A}_{k,k+1},\qquad k=1,2,3.
$$

The chain $N_1,N_2,N_3$ is the sequence of maps that steps down the flag. The composite $E_{kl}$ lies in $\mathcal{A}_{kl}$ and is the product of the simple nilpotents along the chain from $l$ to $k$.

**The nilpotents are not polynomials in $H$.** In the spectral frame a polynomial in $H$ is diagonal, because $H$ is diagonal; the $N_k$ are off-diagonal. They are therefore not part of the root data: they are frame data. This is the precise sense in which the root alone is not the frame.

## The Gauge Action

**Definition.** A **gauge transformation** of the frame is a rescaling

$$
v_k\longmapsto t_kv_k,\qquad t_k\in\mathbb{C}^{\times},\qquad k=1,2,3,4.
$$

The dual basis is rescaled inversely, $\ell_k\mapsto t_k^{-1}\ell_k$, so the matrix units transform by

$$
E_{kl}=v_k\ell_l\longmapsto t_kt_l^{-1}E_{kl}.
$$

**Proposition.** The gauge fixes the idempotents and the root:

$$
P_k=E_{kk}\longmapsto E_{kk}=P_k,\qquad
H=\sum_k\zeta_kE_{kk}\longmapsto H.
$$

The diagonal $t_1=t_2=t_3=t_4$ acts trivially on every $E_{kl}$, so the effective gauge group is

$$
T/\mathbb{C}^{\times}\cong(\mathbb{C}^{\times})^3.
$$

**Proof.** The idempotent $E_{kk}=v_k\ell_k$ is invariant because $t_kt_k^{-1}=1$. The root is a linear combination of the idempotents with constant coefficients $\zeta_k$, hence invariant. The common rescaling $t_k=t$ gives $t t^{-1}=1$ for every unit, so the kernel is the diagonal.

**One parameter per simple nilpotent.** Put

$$
\lambda_k=t_kt_{k+1}^{-1},\qquad k=1,2,3.
$$

Then

$$
N_k=E_{k,k+1}\longmapsto\lambda_kN_k,
$$

and every other unit is fixed by the $\lambda$'s through the cocycle

$$
E_{kl}\longmapsto \lambda_k\lambda_{k+1}\cdots\lambda_{l-1}\,E_{kl}\quad(k<l).
$$

For $k>l$ the scale is the inverse of the product from $l$ to $k$:

$$
E_{kl}\longmapsto \bigl(\lambda_l\lambda_{l+1}\cdots\lambda_{k-1}\bigr)^{-1}E_{kl}\quad(k>l).
$$

**Proof.** For $k<l$, $t_k/t_l=(t_k/t_{k+1})(t_{k+1}/t_{k+2})\cdots(t_{l-1}/t_l)=\lambda_k\cdots\lambda_{l-1}$. For $k>l$, $t_k/t_l$ is the inverse of $t_l/t_k$. The composite $E_{kl}$ has no independent scale: its scale is the product of the consecutive ones.

**The fourth ratio is determined.** Put $\lambda_4=t_4/t_1$. Then

$$
\lambda_1\lambda_2\lambda_3\lambda_4
=\frac{t_1}{t_2}\frac{t_2}{t_3}\frac{t_3}{t_4}\frac{t_4}{t_1}=1.
$$

There are three independent $\lambda$'s, one per simple nilpotent, and the fourth is their inverse product. There is no fourth independent scalar, and there is no independent scale for a composite corner.

**The cocycle forbids an extra parameter.** Suppose that in addition to the $t_k$ one tries to rescale a single composite $E_{kl}$, $k<l$, by an independent $\mu$. The product rule forces

$$
E_{kl}=E_{k,k+1}E_{k+1,k+2}\cdots E_{l-1,l},
$$

so the scale of $E_{kl}$ is the product of the scales of the factors, and $\mu$ is determined by them. Equivalently, the gauge action on the units is the coboundary of the $0$-cochain $t$ in the torus, and a coboundary has no freedom beyond the cochain modulo constants.

**The gauge is not a second root.** The parameters $\lambda_k$ act on the nilpotents and on the off-diagonal units. They never act on the diagonal, on the idempotents, or on the root. A statement that depends on $\lambda$ is a statement about a frame, not about the algebra or the idempotents.

### An Explicit Gauge Transformation

In the standard frame, the gauge is the diagonal matrix

$$
D=\operatorname{diag}(t_1,t_2,t_3,t_4),
$$

acting by conjugation:

$$
D E_{kl}D^{-1}=\frac{t_k}{t_l}E_{kl}.
$$

Take

$$
(t_1,t_2,t_3,t_4)=\left(1,\frac12,\frac16,\frac1{30}\right).
$$

Then

$$
\lambda_1=\frac{t_1}{t_2}=2,\qquad
\lambda_2=\frac{t_2}{t_3}=3,\qquad
\lambda_3=\frac{t_3}{t_4}=5,\qquad
\lambda_4=\frac{t_4}{t_1}=\frac1{30},
$$

and

$$
\lambda_1\lambda_2\lambda_3\lambda_4=2\cdot3\cdot5\cdot\frac1{30}=1.
$$

The simple nilpotents and the composites scale as

| Unit | Scale |
|---|---|
| $E_{12}$ | $\lambda_1=2$ |
| $E_{23}$ | $\lambda_2=3$ |
| $E_{34}$ | $\lambda_3=5$ |
| $E_{13}$ | $\lambda_1\lambda_2=6$ |
| $E_{24}$ | $\lambda_2\lambda_3=15$ |
| $E_{14}$ | $\lambda_1\lambda_2\lambda_3=30$ |
| $E_{21},E_{32},E_{43}$ | $\lambda_1^{-1}, \lambda_2^{-1}, \lambda_3^{-1}$ |
| $E_{31},E_{42},E_{41}$ | $6^{-1}, 15^{-1}, 30^{-1}$ |

The idempotents $E_{11},E_{22},E_{33},E_{44}$ have scale $1$, and the root $H_0$ is unchanged. The fourth ratio $1/30$ is not an independent parameter; it is fixed by the other three and by the condition that the product around the cycle is $1$.

**A numerical check.** With this gauge, $D H_0D^{-1}=H_0$ because $D$ is diagonal and $H_0$ is diagonal, and $D E_{kk}D^{-1}=E_{kk}$ for every $k$. The composite $E_{14}$ scales by $t_1/t_4=30$, which is the product $2\cdot3\cdot5$. Rescaling $E_{14}$ by any other number would violate $E_{14}=E_{12}E_{23}E_{34}$.

## The Count of the Frame

**A frame modulo overall scale has $15$ complex dimensions.** The set of bases of $\mathbb{C}^4$ is $GL_4(\mathbb{C})$, of complex dimension $16$. Two bases that differ by an overall scalar give the same matrix units, since $E_{kl}=v_k\ell_l$ is unchanged when all $v_k$ are multiplied by $t$ and all $\ell_l$ by $t^{-1}$. The frame modulo scale is therefore a point of $PGL_4(\mathbb{C})$, of complex dimension $15$.

**The root and the gauge split the count.** The map from frames to roots,

$$
(v_1,v_2,v_3,v_4)\longmapsto H=\sum_{k=1}^{4}\zeta_kE_{kk},
$$

has fibre the torus $T/\mathbb{C}^{\times}\cong(\mathbb{C}^{\times})^3$: the frames that give the same root are exactly the rescalings of the vectors inside the fixed lines. Hence

$$
\underbrace{15}_{\text{frame}/\mathbb{C}^{\times}}
=
\underbrace{12}_{\text{root}}
+
\underbrace{3}_{\text{gauge}} .
$$

The root set is the base of the fibration, the gauge is the fibre, and the frame is the total space. The root count is *The Adjoint Action, the Orbits and the Flag Variety*; the gauge is the stabiliser of the root in $PGL_4$.

**The case $n=2$.** For the biquaternion algebra $M_2(\mathbb{C})$,

$$
\underbrace{3}_{\text{frame}/\mathbb{C}^{\times}}
=
\underbrace{2}_{\text{root}}
+
\underbrace{1}_{\text{gauge}},
$$

all complex. In real dimensions the frame modulo scale has $6$, the root has $4$ and the gauge has $2$: the four real parameters of the biquaternion root and the two real parameters of the complex number $\lambda$. This is the six-dimensional basis of the biquaternion frame.

## The "Second Root" Is a Gauge Choice

**At $n=2$ the element that the older biquaternion frame called a second root is exactly a point of the gauge.** In the frame $(v_1,v_2)$ with $H=\operatorname{diag}(1,-1)$, let $R$ satisfy

$$
R^2=I,\qquad RH=-HR.
$$

The anticommutation forces $R$ to be off-diagonal, $R=aE_{12}+bE_{21}$, and $R^2=abI=I$ forces $b=a^{-1}$. Hence

$$
R=aE_{12}+a^{-1}E_{21},\qquad a\in\mathbb{C}^{\times}.
$$

Under the gauge $E_{12}\mapsto\lambda E_{12}$, $E_{21}\mapsto\lambda^{-1}E_{21}$, the element $R$ is carried to

$$
a\lambda E_{12}+a^{-1}\lambda^{-1}E_{21},
$$

which is the same family with $a$ replaced by $a\lambda$. The gauge orbit of $R$ is the whole family, and the parameter $a$ is gauge, not root.

**What the second root did and did not do.** It supplied a vector in each mixed Peirce line: $R$ has nonzero entries exactly in $\mathcal{A}_{12}$ and $\mathcal{A}_{21}$, and it normalised them relative to each other. It did not supply the idempotents: those are $P_\pm=(I\pm H)/2$, produced by $H$ alone. The presentation of the frame as a root together with a second root therefore overstated the role of $R$. The correct primitive data is the root; the correct additional data is the gauge point, and at $n=2$ the gauge point is a complex number.

**For $n=4$ there is no single second root.** Elements anticommuting with $H$ do exist: they occupy the two mixed blocks $\mathcal{A}_{13},\mathcal{A}_{31},\mathcal{A}_{24},\mathcal{A}_{42}$, and a general such element is a sum of two independent off-diagonal pairs. Under the gauge it sees only the two combinations $\lambda_1\lambda_2$ and $\lambda_2\lambda_3$, so its orbit has dimension two and it does not carry the third parameter. No single element therefore plays the role that $R$ plays at $n=2$; the gauge is a torus, and there is no second primitive.

## Summary

An adapted frame $(v_1,v_2,v_3,v_4)$ gives the matrix units $E_{kl}=v_k\ell_l$, with $E_{kl}E_{mn}=\delta_{lm}E_{kn}$, $E_{kk}=P_k$ and $H=\sum_k\zeta_kE_{kk}$. The simple nilpotents $N_1=E_{12}$, $N_2=E_{23}$, $N_3=E_{34}$ square to zero, generate the algebra together with the subdiagonal units (their conjugate transposes in an orthonormal frame), and every composite is their consecutive product. The gauge $v_k\mapsto t_kv_k$ acts by $E_{kl}\mapsto(t_k/t_l)E_{kl}$, an effective torus $(\mathbb{C}^{\times})^3$ with one parameter $\lambda_k=t_k/t_{k+1}$ per simple nilpotent, subject to the cocycle that fixes the composites and to the relation $\lambda_1\lambda_2\lambda_3\lambda_4=1$. The frame modulo scale has $15$ complex dimensions, split as $12$ for the root and $3$ for the gauge; at $n=2$ this is $3=2+1$ complex, the $6=4+2$ real count of the biquaternion frame. The older "second root" of the biquaternion frame is a point of this gauge, not a second primitive.

$$
\boxed{\ 15=12+3,\qquad N_k\longmapsto\lambda_kN_k,\qquad E_{kl}\longmapsto\lambda_k\cdots\lambda_{l-1}E_{kl},\qquad \lambda_1\lambda_2\lambda_3\lambda_4=1.\ }
$$

| Object | Dimension over $\mathbb{C}$ |
|---|---|
| Frame $GL_4$ | $16$ |
| Frame modulo overall scale $PGL_4$ | $15$ |
| Root $PGL_4/T$ | $12$ |
| Gauge $(\mathbb{C}^{\times})^3$ | $3$ |
| Simple nilpotents | $3$ |
| Independent gauge parameters | $3$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $v_k$ | a nonzero vector in the spectral line $V_k$ |
| $\ell_k$ | the dual functional, $\ell_k(v_m)=\delta_{km}$ |
| $E_{kl}=v_k\ell_l$ | the matrix unit of the frame |
| $N_k=E_{k,k+1}$ | the simple nilpotent, $N_k^2=0$ |
| $t_k$ | the gauge scale of $v_k$ |
| $\lambda_k=t_kt_{k+1}^{-1}$ | the gauge parameter on $N_k$ |
| $T$ | the torus of rescalings, effective $(\mathbb{C}^{\times})^3$ |
| $D=\operatorname{diag}(t_1,t_2,t_3,t_4)$ | the gauge matrix in the standard frame |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for matrix units, Peirce corners and the coordinate algebra of a frame.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for bases, dual bases and the matrix of a linear map.
- [Roots of Unity and the Lagrange Idempotents](roots-of-unity-and-the-lagrange-idempotents-of-m4c.html), for the root that fixes the flag.
- [The Peirce Decomposition](the-peirce-decomposition-of-m4c.html), for the corners that the units span.
- [The Spin Chain and the Adjoint Decomposition](the-spin-chain-and-the-adjoint-decomposition-of-m4c.html), for the chain of nilpotents as a ladder.
- [The Rank-Two Split](the-rank-two-split-of-m4c.html), for the coarse split and the mass block.
- [The Frame, the Simple Nilpotents and the Gauge](the-frame-the-simple-nilpotents-and-the-gauge-mnc.html), for the general construction at order $n$.
- [Ideals, Peirce Decompositions and Spinors in the Biquaternion Algebra](ideals-peirce-decompositions-and-spinors-in-the-biquaternion-algebra.html), for the biquaternion frame and the parameter $\lambda$.
