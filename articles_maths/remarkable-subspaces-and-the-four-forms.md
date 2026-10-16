# __Remarkable Subspaces and the Four Forms__

## Introduction

The four **forms** of *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space*, the **general plain bilinear form** $\langle\cdot,\cdot\rangle$, the **general plain sesquilinear form** $\langle\cdot,\cdot\rangle_{*}$, the **general quaternionic bilinear form** $\langle\cdot,\cdot\rangle_{\natural}$ and the **general quaternionic sesquilinear form** $\langle\cdot,\cdot\rangle_{\natural*}$, are read here against the remarkable subspaces of *Introduction to the Remarkable Subspaces* — the centre $\mathbb{C}_{\mathbb{B}}$, the vector subspace $\mathrm{Vect}(\mathbb{B})$, the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$, the Hermitian subspace $\mathbb{M}_+$ and the anti-Hermitian subspace $\mathbb{M}_-$ — one subspace to a section, with the summary tables here.

The rule is one line and needs no proof beyond the definition. The **restriction** of a form $\varphi$ to a subspace $U$ is the form read on the elements of $U$,

$$
\varphi|_{U}(\tilde P,\tilde Q)=\varphi(\tilde P,\tilde Q)\big|_{\tilde P,\tilde Q\in U},
$$

and the only thing that happens is that the two arguments are confined to the subspace. Symmetry is inherited, conjugate-symmetry is inherited, non-degeneracy is inherited ($\S$*The Restriction of a Form*), and the value on a general pair is read off the coordinates of the two elements.

This article is the object-level counterpart of *Remarkable Subspaces and the Four Algebraic Norms*, which reads the **values at the two equal arguments** of the same four forms on the same remarkable subspaces. Such a value is a function of one element; the form is a function of two, and the two are not the same object even when that value is enough to recover the form. Two things are visible here that the value at the two equal arguments does not display:

- the **value on a general pair**, that is the restriction as a two-argument object;
- the **imaginary part**, which is a second real bilinear form on the subspace, **symmetric** for the two bilinear forms and **alternating** for the two sesquilinear forms. It is non-zero and non-degenerate on exactly two of the remarkable subspaces, the centre and the vector subspace, and it vanishes identically on the other four.

The first of the two tables below is the summary of the first point and the second of the second. Two sections at the end read the form as a metric: §*The Automorphism Groups of the Restrictions*, for the orthogonal group of each restriction and its real forms, and §*The Realified Form on the Subspaces*, for the maximal definite subspaces, the three orthogonal splittings and the real null cones of the real parts.

The value of each form on a general pair of elements of each subspace is this.

| subspace | $\langle\tilde P,\tilde Q\rangle$ | $\langle\tilde P,\tilde Q\rangle_{*}$ | $\langle\tilde P,\tilde Q\rangle_{\natural}$ | $\langle\tilde P,\tilde Q\rangle_{\natural*}$ |
|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $AC$ | $A\overline{C}$ | $AC$ | $A\overline{C}$ |
| $\mathrm{Vect}(\mathbb{B})$ | $-\sum_kP_kQ_k$ | $\sum_kP_k\overline{Q_k}$ | $\sum_kP_kQ_k$ | $-\sum_kP_k\overline{Q_k}$ |
| $\mathbb{H}_{\mathbb{B}}$ | $h_0k_0-\sum_jh_jk_j$ | $\sum_\mu h_\mu k_\mu$ | $\sum_\mu h_\mu k_\mu$ | $h_0k_0-\sum_jh_jk_j$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $-h_0k_0+\sum_jh_jk_j$ | $\sum_\mu h_\mu k_\mu$ | $-\sum_\mu h_\mu k_\mu$ | $h_0k_0-\sum_jh_jk_j$ |
| $\mathbb{M}_+$ | $a_0c_0+(\vec p,\vec q)$ | $a_0c_0+(\vec p,\vec q)$ | $a_0c_0-(\vec p,\vec q)$ | $a_0c_0-(\vec p,\vec q)$ |
| $\mathbb{M}_-$ | $-b_0d_0-(\vec q,\vec r)$ | $b_0d_0+(\vec q,\vec r)$ | $-b_0d_0+(\vec q,\vec r)$ | $b_0d_0-(\vec q,\vec r)$ |

Each row is written in the coordinates of its own subspace: $\tilde P=Ae_0$ and $\tilde Q=Ce_0$ on the centre, $\tilde P=\sum_kP_ke_k$ and $\tilde Q=\sum_kQ_ke_k$ on the vector subspace, $\tilde P=h$ and $\tilde Q=k$ on the quaternion subspace, $\tilde P=ih$ and $\tilde Q=ik$ on the anti-quaternion subspace, $\tilde P=c_0e_0+i\vec q$ and $\tilde Q=a_0e_0+i\vec p$ on the Hermitian subspace, and $\tilde P=id_0e_0+\vec r$ and $\tilde Q=ib_0e_0+\vec q$ on the anti-Hermitian subspace. In the four real-type rows the symbols $h_\mu,k_\mu$ are the real coefficients of the two elements on the real basis of the subspace, as in *Remarkable Subspaces and the Four Algebraic Norms*.

The field of the values separates the remarkable subspaces: on the centre and on the vector subspace all four forms are **complex-valued**, since the two elements carry general complex coefficients, and on the other four all four forms are **real-valued**, since there each coefficient is real or purely imaginary. The imaginary part therefore lives on the centre and on the vector subspace and nowhere else.

The imaginary part of each form on each subspace is this, written $\langle\cdot,\cdot\rangle=g_B+i\sigma_B$, $\langle\cdot,\cdot\rangle_{*}=g_H+i\omega_H$, $\langle\cdot,\cdot\rangle_{\natural}=g_N+i\sigma_N$ and $\langle\cdot,\cdot\rangle_{\natural*}=g_K+i\omega_K$.

| subspace | $\sigma_B$, $\sigma_N$ | rank | $\omega_H$, $\omega_K$ | rank |
|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | symmetric, non-zero | $2$ | alternating, non-zero | $2$ |
| $\mathrm{Vect}(\mathbb{B})$ | symmetric, non-zero | $6$ | alternating, non-zero | $6$ |
| $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$, $\mathbb{M}_-$ | zero | $0$ | zero | $0$ |

**The real part, and the table that is already written.** The **real part** $g$ of each form is a real symmetric bilinear form on the subspace, and the signature of the restriction, taken over $\mathbb{R}$ as in *Remarkable Subspaces and the Four Algebraic Norms*, is the signature of $g$. On the two sesquilinear forms the value at the two equal arguments is real and equals that of $g$, so their algebraic norm is exactly the value of $g$ at the two equal arguments; on the two bilinear forms the value at the two equal arguments is complex and that of $g$ is its real part. Either way the signature table of this article is the table of that article,

$$
(1,1),(1,1),(2,0),(2,0)\ \text{on}\ \mathbb{C}_{\mathbb{B}};\quad
(3,3),(3,3),(6,0),(0,6)\ \text{on}\ \mathrm{Vect}(\mathbb{B});
$$
$$
(1,3),(4,0),(4,0),(1,3)\ \text{on}\ \mathbb{H}_{\mathbb{B}};\quad
(3,1),(0,4),(4,0),(1,3)\ \text{on}\ i\mathbb{H}_{\mathbb{B}};
$$
$$
(4,0),(1,3),(4,0),(1,3)\ \text{on}\ \mathbb{M}_+;\quad
(0,4),(3,1),(4,0),(1,3)\ \text{on}\ \mathbb{M}_-,
$$

for $\langle\cdot,\cdot\rangle$, $\langle\cdot,\cdot\rangle_{*}$, $\langle\cdot,\cdot\rangle_{\natural}$, $\langle\cdot,\cdot\rangle_{\natural*}$ in that order. It is recalled here and not re-proved: the argument belongs to that article, and the agreement of the two is the check that the real part of a form carries the signature the corpus reads at the two equal arguments.

## Notational Conventions

$\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is the biquaternion algebra, with basis $e_0,e_1,e_2,e_3$, $e_0=1$, $e_k^{2}=-e_0$, and central scalar imaginary $i$, $i^{2}=-1$. A general element is $\tilde Q=\sum_{\mu=0}^{3}Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$, written in the centre–vector split $\tilde Q=c+v$ with $c=Q_0e_0\in\mathbb{C}_{\mathbb{B}}$ and $v=\sum_{k=1}^{3}Q_ke_k\in\mathrm{Vect}(\mathbb{B})$. The scalar part is $\mathrm{Sc}$, the coefficientwise conjugation is $\bar{\cdot}$, the natural conjugation is ${}^{\natural}$, with $Q^{\natural}_\nu=\varepsilon_\nu Q_\nu$, and $Q^{*}=\overline{Q^{\natural}}$. The sign vector is $\varepsilon=(1,-1,-1,-1)$.

The four forms are those of *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space*, written with the one bracket of *Conventions in the Biquaternion Universe* whose subscript records the pair $(a,b)$,

$$
\langle\tilde P,\tilde Q\rangle=\mathrm{Sc}(\tilde P\tilde Q)=\sum_\mu\varepsilon_\mu P_\mu Q_\mu,
\qquad
\langle\tilde P,\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde P\tilde Q^{*})=\sum_\mu P_\mu\overline{Q_\mu},
$$
$$
\langle\tilde P,\tilde Q\rangle_{\natural}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)=\sum_\mu P_\mu Q_\mu,
\qquad
\langle\tilde P,\tilde Q\rangle_{\natural*}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu},
$$

and their names, the **general plain bilinear**, the **general plain sesquilinear**, also called the **Hermitian**, the **general quaternionic bilinear**, and the **general quaternionic sesquilinear**, also called the **Krein**, are those of that article. The value at the two equal arguments is written with the same letter and one argument, $\langle\tilde Q\rangle=\langle\tilde Q,\tilde Q\rangle$ and likewise for the other three.

For a complex-valued form $\varphi$ on a real subspace $U$ the **real part** and the **imaginary part** are the real forms $g=\operatorname{Re}\varphi$ and $\sigma=\operatorname{Im}\varphi$, so that $\varphi=g+i\sigma$; the letter $\omega$ is used for the imaginary part when it is alternating, that is for $\langle\cdot,\cdot\rangle_{*}$ and $\langle\cdot,\cdot\rangle_{\natural*}$. The **signature** of $g$ over $\mathbb{R}$ is written $(n,m)$, $p$ positive and $q$ negative squares. The **null set** of a form on $U$ is $\{\tilde Q\in U:\varphi(\tilde Q,\tilde Q)=0\}$. A form is **non-degenerate** on $U$ when $\varphi(\tilde P,\tilde Q)=0$ for all $\tilde Q\in U$ forces $\tilde P=0$.

**The Gram matrix, and the two sizes it comes in.** The Gram matrix of a restriction is taken **in the complex basis** of the subspace — $(e_0)$ on the centre, $(e_1,e_2,e_3)$ on the vector subspace, the four-element bases of *Introduction to the Remarkable Subspaces* on the four real-type ones — so it is the submatrix of the $4\times4$ matrix of the form in the basis $e_0,e_1,e_2,e_3$, the convention of *Conventions in the Biquaternion Universe* and of *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space*. On the two complex subspaces it is therefore a $1\times1$ or a $3\times3$ **complex** matrix, and its rank there is the rank of the form, by the usual determinant rule; on the four real-type subspaces the basis is already over $\mathbb{R}$ and the matrix is the real $4\times4$. The **real part** $g$ and the **imaginary part** $\sigma$ are separate real data, of twice the size, and their matrices are real; the combined matrix $g+i\sigma$, which writes the two parts in one array, is **not** that Gram matrix and is not read with the determinant rule, since a form written on a real basis may have complex null vectors. Non-degeneracy is a statement about the complex-basis matrix, or equivalently about the two parts, through the identity that the radical of $\varphi$ is the intersection of the radicals of $g$ and $\sigma$.

## The Restriction of a Form

**Proposition (what the restriction inherits).** Let $U$ be one of the remarkable subspaces and $\varphi$ one of the four forms. The restriction $\varphi|_U$ is a form on the real vector space $U$ that inherits

- the **conjugate symmetry**, $\langle\tilde P,\tilde Q\rangle_{*}=\overline{\langle\tilde Q,\tilde P\rangle_{*}}$ for $\langle\cdot,\cdot\rangle_{*}$ and $\langle\cdot,\cdot\rangle_{\natural*}$ and the plain symmetry $\langle\tilde P,\tilde Q\rangle=\langle\tilde Q,\tilde P\rangle$ for $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{\natural}$, since the identity holds on the ambient space and $U$ is a subspace;
- the **scalar laws** for real scalars, $\varphi(\lambda\tilde P,\tilde Q)=\varphi(\tilde P,\lambda\tilde Q)=\lambda\varphi(\tilde P,\tilde Q)$ for $\lambda\in\mathbb{R}$, the conjugate-linear second slot of $\langle\cdot,\cdot\rangle_{*}$ and $\langle\cdot,\cdot\rangle_{\natural*}$ being available for complex scalars only when the subspace is complex, which is the case of the centre and of the vector subspace alone;
- the **real–imaginary split** $\varphi=g+i\sigma$, with $g$ a real **symmetric** bilinear form and $\sigma$ a real bilinear form that is **symmetric** for $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{\natural}$ and **alternating** for $\langle\cdot,\cdot\rangle_{*}$ and $\langle\cdot,\cdot\rangle_{\natural*}$;
- the **non-degeneracy**: all twenty-four restrictions, four forms on remarkable subspaces, are non-degenerate.

*Proof.* The symmetry and the conjugate symmetry are inherited because the two arguments are confined to $U$ and the ambient identity involves nothing outside it. The scalar laws are the ambient ones read on real multiples. For the split, $g=\tfrac12(\varphi+\bar\varphi)$ and $\sigma=\tfrac{1}{2i}(\varphi-\bar\varphi)$ with $\bar\varphi(\tilde P,\tilde Q)=\overline{\varphi(\tilde P,\tilde Q)}$. For $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{\natural}$, whose $\varphi$ is symmetric, the form $\bar\varphi$ is symmetric too and so is $\sigma$. For $\langle\cdot,\cdot\rangle_{*}$ and $\langle\cdot,\cdot\rangle_{\natural*}$, whose $\varphi$ is conjugate-symmetric, $\bar\varphi(\tilde P,\tilde Q)=\varphi(\tilde Q,\tilde P)$, so $\sigma=\tfrac{1}{2i}\bigl(\varphi(\tilde P,\tilde Q)-\varphi(\tilde Q,\tilde P)\bigr)$ and $\sigma(\tilde Q,\tilde P)=-\sigma(\tilde P,\tilde Q)$, that is alternating. Non-degeneracy is read on the Gram matrices of each subspace, and on the twenty-four it holds: the test is that the $2d\times d$ real matrix $[\operatorname{Re}G;\operatorname{Im}G]$ of the Gram matrix $G$ has rank $d$; the four Gram matrices of the centre and the vector subspace are computed in the two sections that follow, and the remaining sixteen are algebraic norm and of the four types $\operatorname{diag}(1,-1,-1,-1)$, $\mathrm I_4$, $-\mathrm I_4$ and $\operatorname{diag}(-1,1,1,1)$, all of full rank.

**Remark (what the algebraic norm does and does not give).** For the two bilinear forms the algebraic norm determines the form, by the polarisation identity $\langle\tilde P,\tilde Q\rangle=\tfrac12\bigl(\langle\tilde P+\tilde Q\rangle-\langle\tilde P\rangle-\langle\tilde Q\rangle\bigr)$, and with it the rank. For the two sesquilinear forms the algebraic norm is real and gives only the **real part** $g$, and the imaginary part is separate data which the algebraic norm does not fix: a Hermitian form on a real subspace can have a vanishing real part and a non-vanishing imaginary part, and it is only when the multiplication by $i$ stays inside the subspace that the polarisation with $i$ ties the two. On the four real-type subspaces the imaginary part happens to vanish, which is the fact the six sections verify; on the two complex subspaces it does not, and there the complex structure ties it to the real part. So the algebraic norm is enough for everything on this page, and it is enough for a reason that is worth keeping: on each of the remarkable subspaces the imaginary part is either accessible through $i$ or zero.

## The Two Complex Subspaces and the Four Real-Type Subspaces

The remarkable subspaces fall into two classes, and the class is what decides whether the four forms have an imaginary part. The test is the multiplication by the central imaginary: the two complex subspaces satisfy $iU=U$, and the four others satisfy $iU\cap U=\{0\}$.

- The **two complex subspaces**, the centre $\mathbb{C}_{\mathbb{B}}$ and the vector subspace $\mathrm{Vect}(\mathbb{B})$, are complex-linear spans, of one and three complex dimensions, and their elements carry general complex coefficients. On them every one of the four forms is complex-valued and its imaginary part is non-zero and non-degenerate, and the multiplication by $i$ is available inside the subspace, so the alternating companion is read off the real part by the Kähler identity below.
- The **four real-type subspaces**, the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$, the Hermitian subspace $\mathbb{M}_+$ and the anti-Hermitian subspace $\mathbb{M}_-$, are real-linear spans whose elements have each coefficient real or purely imaginary. On them every one of the four forms is real-valued, its imaginary part vanishes, and the form is a real symmetric bilinear form recovered from its algebraic norm.

This is the structural content of the article, and it is worth stating in one line: **the four forms of the biquaternion algebra carry a phase structure on the two complex subspaces and none on the four real-type subspaces.** The rest of the article is the six sections that verify it subspace by subspace, and the proposition at the end of the remarkable subspaces that collects it.

## The Centre Subspace

An element of the centre is $\tilde Q=Ae_0$, $A\in\mathbb{C}$, and the centre is a complex line spanned by $e_0$ over $\mathbb{C}_{\mathbb{B}}$. Two elements are $\tilde P=Ae_0$ and $\tilde Q=Ce_0$, and the only coefficient of each is its scalar, so the four sums of the introduction reduce at once:

$$
\langle\tilde P,\tilde Q\rangle_{\natural}=AC,
\qquad
\langle\tilde P,\tilde Q\rangle_{*}=\langle\tilde P,\tilde Q\rangle_{\natural*}=A\overline{C}.
$$

**On the centre the four forms collapse to two, $\langle\cdot,\cdot\rangle=\langle\cdot,\cdot\rangle_{\natural}$ and $\langle\cdot,\cdot\rangle_{*}=\langle\cdot,\cdot\rangle_{\natural*}$.** The two collapses have one reason: the natural conjugation fixes the centre, $\tilde Q^{\natural}=\tilde Q$ for $\tilde Q\in\mathbb{C}_{\mathbb{B}}$, because $\varepsilon_0=1$ is the only sign that meets a non-zero coordinate. The first slot of the general product is therefore idle there, and with it the difference between the plain family and the quaternionic family. The first pair is the complex quadratic form $AC$ of the pair, the second the Hermitian form $A\overline{C}$.

Writing $A=a+ib$ and $C=c+id$ with real coordinates, the two forms are

$$
AC=(ac-bd)+i(ad+bc),
\qquad
A\overline{C}=(ac+bd)+i(bc-ad).
$$

The first has a real part of signature $(1,1)$ and an imaginary part $\sigma=ad+bc$, symmetric and of rank $2$; the second has a positive definite real part of signature $(2,0)$ and an imaginary part $\omega=bc-ad$, alternating, of rank $2$. In the complex basis $(e_0)$ the Gram matrix of each of the four is the single entry

$$
B=N=H=K=(1),
$$

non-singular, so all four restrictions are non-degenerate; and the two parts, read in the real basis $(e_0,ie_0)$, are

$$
g_B=g_N=\begin{pmatrix}1&0\\ 0&-1\end{pmatrix},
\qquad
\sigma_B=\sigma_N=\begin{pmatrix}0&1\\ 1&0\end{pmatrix},
\qquad
g_H=g_K=\mathrm I_2,
\qquad
\omega_H=\omega_K=\begin{pmatrix}0&-1\\ 1&0\end{pmatrix}.
$$

The single entry $(1)$ and the pair $(g,\sigma)$ carry the same information, the second being the first with its real and imaginary parts separated; the two real parts have signatures $(1,1)$ and $(2,0)$, which the complex matrix cannot show. The alternating form $\omega$ of the centre is non-degenerate, of rank $2$; it is the canonical pair of the line, and on the pair of real basis vectors it takes the value $\omega(e_0,ie_0)=-1$.

**The null set of each of the four on the centre is the origin alone.** The two bilinear forms vanish when $A^{2}=0$, and an element of the centre has no zero divisors, so $A=0$; the two sesquilinear forms vanish when $\lvert A\rvert^{2}=0$, which is again $A=0$. The ambient null sets, the complex cone of $\langle\cdot,\cdot\rangle$ and the zero-divisor cone of $\langle\cdot,\cdot\rangle_{\natural}$, meet the centre in the origin alone.

## The Vector Subspace

An element of the vector subspace is $\tilde Q=\sum_kQ_ke_k$ with $Q_k\in\mathbb{C}$, of real dimension six, with the real basis $(e_1,ie_1,e_2,ie_2,e_3,ie_3)$. Two elements are $\tilde P=\sum_kP_ke_k$ and $\tilde Q=\sum_kQ_ke_k$, and the four sums are read term by term, the vector part contributing $\mathrm{Sc}(P_kQ_ke_k^{2})=-P_kQ_k$ to the two bilinear forms and the star of the second slot leaving $\lvert P_k\rvert^{2}$ at the two equal arguments:

$$
\langle\tilde P,\tilde Q\rangle=-\sum_kP_kQ_k,
\qquad
\langle\tilde P,\tilde Q\rangle_{*}=\sum_kP_k\overline{Q_k},
\qquad
\langle\tilde P,\tilde Q\rangle_{\natural}=\sum_kP_kQ_k,
\qquad
\langle\tilde P,\tilde Q\rangle_{\natural*}=-\sum_kP_k\overline{Q_k}.
$$

**On the vector subspace the four forms are the two, up to sign: $\langle\cdot,\cdot\rangle=-N$ and $\langle\cdot,\cdot\rangle_{\natural*}=-H$.** The pair of bilinear forms is one complex symmetric form and its negative, and the pair of sesquilinear forms one Hermitian form and its negative.

Writing $P_k=p_k+iq_k$ and $Q_k=r_k+is_k$ with real coordinates, the real part of the Hermitian form is the positive definite sum $g_H=\sum_k(p_kr_k+q_ks_k)$, of signature $(6,0)$, and its imaginary part is $\omega=\sum_k(q_kr_k-p_ks_k)$, alternating and of rank $6$. In the complex basis $(e_1,e_2,e_3)$ the Gram matrices are the $3\times3$ matrices

$$
B=K=-\mathrm I_3,
\qquad
N=H=\mathrm I_3,
$$

each the multiple of the identity, hence non-singular of rank $3$: the four restrictions are non-degenerate, and the two families differ by one overall sign alone. The two parts, read in the real basis ordered $(e_1,ie_1,e_2,ie_2,e_3,ie_3)$, are the real matrices

$$
g_H=\mathrm I_6,
\qquad
\omega_H=\begin{pmatrix}0&-1&0&0&0&0\\ 1&0&0&0&0&0\\ 0&0&0&-1&0&0\\ 0&0&1&0&0&0\\ 0&0&0&0&0&-1\\ 0&0&0&0&1&0\end{pmatrix},
$$

of ranks $6$ and $6$: the block sum of three copies of $\begin{pmatrix}0&-1\\ 1&0\end{pmatrix}$, one in each coordinate plane $(e_k,ie_k)$, which is the three canonical pairs of the three coordinate planes, one pair to a spatial direction. The $3\times3$ Gram matrix holds the same content as the pair $(g_H,\omega_H)$: the signs of $-\mathrm I_3$ and $\mathrm I_3$ are the pairing of a definite real part with an alternating one, and the extension of the space from three complex to six real dimensions is what doubles the array.

**The null sets on the vector subspace are two cones and two origins.** The two bilinear forms vanish on the complex cone $\sum_kQ_k^{2}=0$, of real dimension four, the zero divisors of the vector subspace; the two sesquilinear forms vanish when $\sum_k\lvert Q_k\rvert^{2}=0$, which is $Q=0$. So $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{\natural}$ have a genuine cone on the vector subspace while $\langle\cdot,\cdot\rangle_{*}$ and $\langle\cdot,\cdot\rangle_{\natural*}$ have none, exactly in reverse of the centre.

## The Quaternion Subspace

An element of the quaternion subspace is $\tilde Q=k=\sum_\mu k_\mu e_\mu$ with $k_\mu$ real, of real dimension four, with the real basis $(e_0,e_1,e_2,e_3)$. Two elements are $\tilde P=h$ and $\tilde Q=k$, and for real coefficients the coefficientwise conjugation is the identity, so the star of the second slot and the natural conjugation agree, and the four sums reduce to the two real forms

$$
\langle\tilde P,\tilde Q\rangle_{\natural*}=h_0k_0-\sum_{j=1}^{3}h_jk_j,
\qquad
\langle\tilde P,\tilde Q\rangle_{\natural}=\langle\tilde P,\tilde Q\rangle_{*}=\sum_{\mu=0}^{3}h_\mu k_\mu .
$$

**On the quaternion subspace the four forms collapse to two, $\langle\cdot,\cdot\rangle=\langle\cdot,\cdot\rangle_{\natural*}$ and $\langle\cdot,\cdot\rangle_{\natural}=\langle\cdot,\cdot\rangle_{*}$**, and they are the two classical real forms of the quaternion algebra: the Minkowski form $h_0k_0-(\vec h,\vec k)$ of signature $(1,3)$, and the Euclidean form $(\vec h,\vec k)_{\mathbb{R}^4}$ of signature $(4,0)$.

All four are real-valued, so the imaginary part vanishes identically and the splitting of each form into real and imaginary parts is the form itself. The Gram matrices are the two diagonal matrices $\operatorname{diag}(1,-1,-1,-1)$ for $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{\natural*}$ and $\mathrm I_4$ for $\langle\cdot,\cdot\rangle_{*}$ and $\langle\cdot,\cdot\rangle_{\natural}$, both of full rank, so all four restrictions are non-degenerate.

**The null sets on the quaternion subspace are one light cone and two origins.** The forms $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{\natural*}$ vanish on the real light cone $h_0^{2}=\lvert\vec h\rvert^{2}$, of real dimension three; the forms $\langle\cdot,\cdot\rangle_{*}$ and $\langle\cdot,\cdot\rangle_{\natural}$ vanish at the origin alone. This is the subspace on which the Minkowski form — and not the corpus's interval $\langle\cdot,\cdot\rangle_{\natural}$, which is Euclidean here — is the algebraic norm of $\langle\cdot\rangle_{\natural*}=\langle\cdot\rangle$, and the light cone here is its null cone.

## The Anti-Quaternion Subspace

An element of the anti-quaternion subspace is $\tilde Q=ik$ with $k$ of the quaternion subspace, of real dimension four, with the real basis $(ie_0,ie_1,ie_2,ie_3)$. Two elements are $\tilde P=ih$ and $\tilde Q=ik$ with $h,k$ real-coefficient, and the central imaginary $i$ enters every product twice, so the sign of the whole is that of $i^{2}=-1$ on the scalar part and of $i^{2}$ again against $e_k^{2}$ on the vector part. The four forms are

$$
\langle\tilde P,\tilde Q\rangle=-h_0k_0+\sum_{j=1}^{3}h_jk_j,
\qquad
\langle\tilde P,\tilde Q\rangle_{*}=\sum_{\mu=0}^{3}h_\mu k_\mu,
$$
$$
\langle\tilde P,\tilde Q\rangle_{\natural}=-\sum_{\mu=0}^{3}h_\mu k_\mu,
\qquad
\langle\tilde P,\tilde Q\rangle_{\natural*}=h_0k_0-\sum_{j=1}^{3}h_jk_j .
$$

**On the anti-quaternion subspace the four forms collapse to two with signs, $\langle\cdot,\cdot\rangle=-K$ and $\langle\cdot,\cdot\rangle_{\natural}=-H$**: each is the negative of the corresponding form on the quaternion subspace, $\langle\cdot,\cdot\rangle$ of $\langle\cdot,\cdot\rangle_{\natural*}$ and $\langle\cdot,\cdot\rangle_{\natural}$ of $\langle\cdot,\cdot\rangle_{*}$, and the two sign changes are those of the translation by $i$ that takes one subspace to the other. The signatures are $(3,1)$ for $\langle\cdot,\cdot\rangle$, $(4,0)$ for $\langle\cdot,\cdot\rangle_{*}$, $(0,4)$ for $\langle\cdot,\cdot\rangle_{\natural}$ and $(1,3)$ for $\langle\cdot,\cdot\rangle_{\natural*}$, and the Gram matrices are $\operatorname{diag}(-1,1,1,1)$, $\mathrm I_4$, $-\mathrm I_4$ and $\operatorname{diag}(1,-1,-1,-1)$, all of full rank.

All four are real-valued, so the imaginary part vanishes identically. The null sets are the real light cones of $\langle\cdot,\cdot\rangle$ and of $\langle\cdot,\cdot\rangle_{\natural*}$, of real dimension three, and the origins of $\langle\cdot,\cdot\rangle_{*}$ and of $\langle\cdot,\cdot\rangle_{\natural}$: the same pattern as the quaternion subspace, with the roles of the two signs exchanged.

## The Hermitian Subspace

An element of the Hermitian subspace is $\tilde Q=a_0e_0+i\vec p$ with $a_0$ real and $\vec p$ a real vector, of real dimension four, with the real basis $(e_0,ie_1,ie_2,ie_3)$. Two elements are $\tilde P=c_0e_0+i\vec q$ and $\tilde Q=a_0e_0+i\vec p$; the scalar parts contribute $a_0c_0$, and the vector parts contribute the real dot product $(\vec p,\vec q)$ with a sign that is $+$ for the pair $\langle\cdot,\cdot\rangle$, $\langle\cdot,\cdot\rangle_{*}$ and $-$ for the pair $\langle\cdot,\cdot\rangle_{\natural}$, $\langle\cdot,\cdot\rangle_{\natural*}$:

$$
\langle\tilde P,\tilde Q\rangle_{*}=a_0c_0+(\vec p,\vec q),
\qquad
\langle\tilde P,\tilde Q\rangle_{\natural}=\langle\tilde P,\tilde Q\rangle_{\natural*}=a_0c_0-(\vec p,\vec q).
$$

**On the Hermitian subspace the four forms collapse to two, $\langle\cdot,\cdot\rangle=\langle\cdot,\cdot\rangle_{*}$ and $\langle\cdot,\cdot\rangle_{\natural}=\langle\cdot,\cdot\rangle_{\natural*}$**, the Euclidean form of signature $(4,0)$ and the Minkowski form of signature $(1,3)$. The collapse pairs a bilinear form with a sesquilinear one here, which does not happen on the other five, and the reason is that on the Hermitian subspace the star of the second slot acts as the identity, since the coefficients are already real in the scalar slot and purely imaginary in the vector slots.

All four are real-valued, so the imaginary part vanishes identically, and the Gram matrices are $\mathrm I_4$ for $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{*}$ and $\operatorname{diag}(1,-1,-1,-1)$ for $\langle\cdot,\cdot\rangle_{\natural}$ and $\langle\cdot,\cdot\rangle_{\natural*}$, both of full rank. The null sets are the origin of the Euclidean pair $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{*}$ and the light cone of the Minkowski pair $\langle\cdot,\cdot\rangle_{\natural}$ and $\langle\cdot,\cdot\rangle_{\natural*}$, of real dimension three.

## The Anti-Hermitian Subspace

An element of the anti-Hermitian subspace is $\tilde Q=ib_0e_0+\vec q$ with $b_0$ real and $\vec q$ a real vector, of real dimension four, with the real basis $(ie_0,e_1,e_2,e_3)$. Two elements are $\tilde P=id_0e_0+\vec r$ and $\tilde Q=ib_0e_0+\vec q$, and the four forms are

$$
\langle\tilde P,\tilde Q\rangle=-b_0d_0-(\vec q,\vec r),
\qquad
\langle\tilde P,\tilde Q\rangle_{*}=b_0d_0+(\vec q,\vec r),
$$
$$
\langle\tilde P,\tilde Q\rangle_{\natural}=-b_0d_0+(\vec q,\vec r),
\qquad
\langle\tilde P,\tilde Q\rangle_{\natural*}=b_0d_0-(\vec q,\vec r).
$$

**On the anti-Hermitian subspace the four forms are four distinct functions, with the two sign relations $\langle\cdot,\cdot\rangle=-H$ and $\langle\cdot,\cdot\rangle_{\natural}=-K$.** The signatures are $(0,4)$ for $\langle\cdot,\cdot\rangle$, $(4,0)$ for $\langle\cdot,\cdot\rangle_{*}$, $(3,1)$ for $\langle\cdot,\cdot\rangle_{\natural}$ and $(1,3)$ for $\langle\cdot,\cdot\rangle_{\natural*}$, and the Gram matrices are $-\mathrm I_4$, $\mathrm I_4$, $\operatorname{diag}(-1,1,1,1)$ and $\operatorname{diag}(1,-1,-1,-1)$, all of full rank.

All four are real-valued, so the imaginary part vanishes identically. The null sets are the origins of $\langle\cdot,\cdot\rangle$ and of $\langle\cdot,\cdot\rangle_{*}$ and the light cones of $\langle\cdot,\cdot\rangle_{\natural}$ and of $\langle\cdot,\cdot\rangle_{\natural*}$, of real dimension three.

**This is the material sector.** The four forms here are the two sesquilinear ones with their signs, $\langle\cdot,\cdot\rangle_{*}=b_0^{2}+(\vec q,\vec q)$ the **Euclidean square** of signature $(4,0)$ and $\langle\cdot,\cdot\rangle_{\natural*}=b_0^{2}-(\vec q,\vec q)$ of signature $(1,3)$, against the two bilinear ones $\langle\cdot,\cdot\rangle=-H$ and $N=-K$, and the two pairs of the corpus's material reading — the **interval** $\langle\cdot,\cdot\rangle_{\natural}$ of signature $(3,1)$ against the Euclidean square, and the light cone of $\langle\cdot,\cdot\rangle_{\natural}$ against the definite $\langle\cdot,\cdot\rangle_{*}$ — are exactly the columns of $\langle\cdot,\cdot\rangle_{*}$ and of $\langle\cdot,\cdot\rangle_{\natural*}$ of the table above.

## The Real and Imaginary Parts

**Proposition (the split of a form on a subspace).** For each of the remarkable subspaces and each of the four forms, the form splits as $\varphi=g+i\sigma$ with $g$ real symmetric and $\sigma$ real, symmetric for $\langle\cdot,\cdot\rangle$ and for $\langle\cdot,\cdot\rangle_{\natural}$ and alternating for $\langle\cdot,\cdot\rangle_{*}$ and for $\langle\cdot,\cdot\rangle_{\natural*}$. The imaginary part $\sigma$ vanishes identically on the four real-type subspaces, and on the two complex subspaces it is non-zero and non-degenerate, of rank $2$ on the centre and of rank $6$ on the vector subspace.

*Proof.* The symmetry of $g$ and the two kinds of $\sigma$ are the proposition of $\S$*The Restriction of a Form*. The vanishing on the four real-type subspaces is read on the twelve formulas of $\S\S$*The Quaternion Subspace* to *The Anti-Hermitian Subspace*: each value there is real. The non-vanishing on the two complex subspaces and the ranks are read on the two matrices of $\S\S$*The Centre Subspace* and *The Vector Subspace*: the imaginary part of $\langle\cdot,\cdot\rangle$ on the centre is the matrix $\begin{pmatrix}0&1\\ 1&0\end{pmatrix}$ of rank $2$ and the imaginary part of $\langle\cdot,\cdot\rangle_{*}$ on the vector subspace is the block sum of three copies of $\begin{pmatrix}0&-1\\ 1&0\end{pmatrix}$, of rank $6$.

**The Kähler identity.** On the two complex subspaces the alternating part of $\langle\cdot,\cdot\rangle_{*}$ and of $\langle\cdot,\cdot\rangle_{\natural*}$ is the real part composed with the complex structure,

$$
\omega(\tilde P,\tilde Q)=g(\tilde P,i\tilde Q),
$$

for all $\tilde P,\tilde Q$ in the subspace. *Proof.* $\langle\tilde P,i\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde P(i\tilde Q)^{*})$ and $(i\tilde Q)^{*}=-i\tilde Q^{*}$, since the star is the coefficientwise conjugation composed with the natural conjugation and the two commute with the central imaginary; so $\langle\tilde P,i\tilde Q\rangle_{*}=-iH(\tilde P,\tilde Q)$, whose real part is the imaginary part of $\langle\cdot,\cdot\rangle_{*}$ and whose imaginary part is minus the real part. The same computation holds for $\langle\cdot,\cdot\rangle_{\natural*}$.

**The companion identity for the bilinear pair.** The same computation with the second slot read without the star gives $\langle\tilde P,i\tilde Q\rangle=iB(\tilde P,\tilde Q)$, since multiplying by a scalar pulls out of a bilinear slot without conjugation, and the real part of $i(g_B+i\sigma_B)$ is $-\sigma_B$. So

$$
\omega(\tilde P,\tilde Q)=+g(\tilde P,i\tilde Q)\ \text{for}\ H\ \text{and}\ K,
\qquad
\sigma(\tilde P,\tilde Q)=-g(\tilde P,i\tilde Q)\ \text{for}\ B\ \text{and}\ N,
$$

on the two complex subspaces, and the one sign is the whole difference between the two pairs. It is worth keeping: the two identities are the reason the imaginary part of a bilinear form is symmetric and the imaginary part of a sesquilinear form alternating, and not the other way round.

The identity says that the alternating part is not a second independent object on top of the real part: it is the real part read through the complex structure, and it is available only where the complex structure is, which is the centre and the vector subspace. On the four real-type subspaces the complex structure leaves the subspace and the identity has no content, and there the imaginary part is zero.

**The two slotted conjugations and the two pairings.** The table of the imaginary part has one more line worth the reading. The imaginary part of a form is symmetric when the form is **bilinear** and alternating when the form is **sesquilinear**, and the second slot is the slot that decides it: the star conjugates $i$ and flips the sign of the companion identity, and the conjugate symmetry of $\langle\cdot,\cdot\rangle_{*}$ and $\langle\cdot,\cdot\rangle_{\natural*}$ then forces their imaginary part to be alternating. The first slot, the natural conjugation, does not touch the value: it is applied before the two elements are multiplied, and no conjugation of $i$ reaches the product. So the difference between the two families in the table of the imaginary part is the difference between the two second slots and nothing else.

## The Null Sets

| subspace | $\langle\cdot,\cdot\rangle$ | $\langle\cdot,\cdot\rangle_{*}$ | $\langle\cdot,\cdot\rangle_{\natural}$ | $\langle\cdot,\cdot\rangle_{\natural*}$ |
|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $\{0\}$ | $\{0\}$ | $\{0\}$ | $\{0\}$ |
| $\mathrm{Vect}(\mathbb{B})$ | the complex cone, real dimension $4$ | $\{0\}$ | the complex cone, real dimension $4$ | $\{0\}$ |
| $\mathbb{H}_{\mathbb{B}}$ | the light cone, real dimension $3$ | $\{0\}$ | $\{0\}$ | the light cone, real dimension $3$ |
| $i\mathbb{H}_{\mathbb{B}}$ | the light cone, real dimension $3$ | $\{0\}$ | $\{0\}$ | the light cone, real dimension $3$ |
| $\mathbb{M}_+$ | $\{0\}$ | $\{0\}$ | the light cone, real dimension $3$ | the light cone, real dimension $3$ |
| $\mathbb{M}_-$ | $\{0\}$ | $\{0\}$ | the light cone, real dimension $3$ | the light cone, real dimension $3$ |

The rule behind the table is one line: **off the centre a form has a complex null cone on a subspace exactly when the restriction of its real part is indefinite there**, and the signatures of the introduction and of the six sections say which are. On the centre the complex zeros are trivial for all four forms even though the real part of $\langle\cdot,\cdot\rangle$ and of $\langle\cdot,\cdot\rangle_{\natural}$ is indefinite, and it is the real zeros of the real part that form the cone there; the two kinds of zero are separated in §*The Realified Form on the Subspaces*. The count of forms with a complex null cone is none on the centre, two on the vector subspace, the bilinear pair $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{\natural}$ of signature $(3,3)$, and two on each of the four real-type subspaces, $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{\natural*}$ on the quaternion subspace and on its imaginary translate, $\langle\cdot,\cdot\rangle_{\natural}$ and $\langle\cdot,\cdot\rangle_{\natural*}$ on the two sectors. Two columns of the table are constant and are the two theorems of *The 4 Algebraic Norms over the Biquaternioid $\mathbb{C}$ Space* read on the remarkable subspaces: **$\langle\cdot,\cdot\rangle_{*}$ is definite on all of them**, so its null set is the origin in each, and **$\langle\cdot,\cdot\rangle_{*}$ is the only definite one**, so each of the other three has a cone on some subspace. A collapse with no sign keeps the cone, a collapse with a sign swaps it for the origin, and the collapse $\langle\cdot,\cdot\rangle_{*}=\langle\cdot,\cdot\rangle_{\natural*}$ on the centre against $K=-H$ on the vector subspace is exactly the exchange of a definite form for an indefinite one.

**The ambient cones are cut by the subspaces.** The ambient null sets of *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space* are the complex cone of $\langle\cdot,\cdot\rangle$, the zero-divisor cone $\mathcal N$ of $\langle\cdot,\cdot\rangle_{\natural}$ and the real cone $\mathcal K$ of $\langle\cdot,\cdot\rangle_{\natural*}$, of real dimensions six, six and seven. The table above is what those cones become on the remarkable subspaces, and the two are different pictures: the ambient cones have real dimension six or seven, and the cones of the table have real dimension four on the vector subspace and real dimension three on the four real-type subspaces, because the equations $\sum_kQ_k^{2}=0$ in three complex unknowns and $h_0^{2}=\lvert\vec h\rvert^{2}$ in four real unknowns have those dimensions. A subspace is not a small copy of the ambient space for a cone.

## The Automorphism Groups of the Restrictions

**Definition.** For a subspace $U$ of the remarkable subspaces the **automorphism group of the restriction** is the group of real-linear maps of $U$ preserving $B|_U$,

$$
\mathrm{Isom}\bigl(U,B\bigr)=\{S\in GL_{\mathbb{R}}(U):\langle Su,Sv\rangle=\langle u,v\rangle\ \text{for all }u,v\in U\}.
$$

It is the real orthogonal group of the signature of the real part $g_B$ on $U$, and its real dimension is $n(n-1)/2$ for $n=\dim_{\mathbb{R}}U$. The signatures of the introduction give the table.

| subspace | signature of $g_B$ | automorphism group | real dimension |
|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $(1,1)$ | $O(1,1)$ | $1$ |
| $\mathrm{Vect}(\mathbb{B})$ | $(3,3)$ | $O(3,3)$ | $15$ |
| $\mathbb{H}_{\mathbb{B}}$ | $(1,3)$ | $O(1,3)$ | $6$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $(3,1)$ | $O(3,1)\cong O(1,3)$ | $6$ |
| $\mathbb{M}_+$ | $(4,0)$ | $O(4)$ | $6$ |
| $\mathbb{M}_-$ | $(0,4)$ | $O(4)$ | $6$ |

The same rows with the signatures of $\langle\cdot,\cdot\rangle_{*}$, $\langle\cdot,\cdot\rangle_{\natural}$ and $\langle\cdot,\cdot\rangle_{\natural*}$ give their automorphism groups, since each of the four forms is non-degenerate on $U$ and its group depends on the signature alone.

**Remark (the real group against the complex one).** On the two complex subspaces the largest $\mathbb{C}$-linear group that preserves the subspace and the form is the smaller complex orthogonal group, $O_1(\mathbb{C})$ on the centre and $O_3(\mathbb{C})$ on the vector subspace, of real dimensions $0$ and $6$; the real groups $O(1,1)$ and $O(3,3)$ of the table are larger, because a real-linear form preservation need not respect the complex structure. On the four real-type subspaces the two agree: a real automorphism of the restriction extends by complex linearity to an automorphism of the algebra preserving the subspace, and conversely. The rows $O(1,3)$ and $O(4)$ are therefore the real forms of the complex orthogonal group $O_4(\mathbb{C})$ of *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space*, §*The Isometry Groups of the Four Forms*: each of the four real subspaces spans the algebra over $\mathbb{C}$, its restriction is a real form of a general plain bilinear form on $\mathbb{B}$, and the four restrictions are congruent to one another over $\mathbb{C}$. The groups $O(1,1)$ and $O(3,3)$ of the two complex subspaces are not real forms of that complex group.

## The Realified Form on the Subspaces

**The maximal definite subspaces.** The real part $g_B$ on the whole algebra has signature $(4,4)$, so its maximal positive definite and maximal negative definite dimensions are both $4$. The Hermitian subspace $\mathbb{M}_+$, of real dimension $4$ and positive definite, is a **maximal positive definite subspace**, and the anti-Hermitian subspace $\mathbb{M}_-$ a **maximal negative definite subspace**; neither can be enlarged while remaining definite, and the two are orthogonal complements. The centre is a definite plane only in the hyperbolic sense, its signature $(1,1)$ being neither positive nor negative definite, and the quaternion and vector subspaces carry both signs.

**The three orthogonal splittings.** The form is diagonal in the natural bases, so three pairs of complementary subspaces split the algebra orthogonally, the signatures adding to $(4,4)$ in each:

$$
\mathbb{B}=\mathbb{C}_{\mathbb{B}}\perp\mathrm{Vect}(\mathbb{B}),\qquad
\mathbb{B}=\mathbb{H}_{\mathbb{B}}\perp i\mathbb{H}_{\mathbb{B}},\qquad
\mathbb{B}=\mathbb{M}_+\perp\mathbb{M}_-,
$$

of signatures $(1,1)\perp(3,3)$, $(1,3)\perp(3,1)$ and $(4,0)\perp(0,4)$. Only the third splits the realified form into a positive definite and a negative definite piece; in the first two both sides carry isotropic vectors. The two restricted forms of the third split are exchanged by the central scalar, $\langle i\tilde P,i\tilde Q\rangle=-\langle\tilde P,\tilde Q\rangle$.

**The real null cones of $g_B=\operatorname{Re}B$.** On each of the four indefinite rows the real zeros of $g_B$ form a cone through the origin of real dimension one less than the subspace, and one null element on each row exhibits it.

| subspace | signature | null element | real null cone, real dimension |
|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $(1,1)$ | $e_0+ie_0$ | $1$, the two lines $\mathbb{R}(e_0\pm ie_0)$ |
| $\mathrm{Vect}(\mathbb{B})$ | $(3,3)$ | $e_1+ie_1$ | $5$ |
| $\mathbb{H}_{\mathbb{B}}$ | $(1,3)$ | $e_0+e_1$ | $3$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $(3,1)$ | $ie_0+ie_1$ | $3$ |

Each element is null because the real part of its value vanishes, $1-1$ on the centre and on the vector and quaternion subspaces, $-1+1$ on the anti-quaternion subspace. On an indefinite form of signature $(n,m)$ the zeros of the diagonal form a cone of real codimension one, whence the dimensions; on the centre, of real dimension two, the cone is the pair of lines $\mathbb{R}(e_0\pm ie_0)$. The two definite rows, $\mathbb{M}_+$ and $\mathbb{M}_-$, contribute no null element, so the isotropic rows are four and not six. These are the real zeros of $g_B$, and they are distinct from the complex null sets of the table above, which are the complex zeros of $\langle\cdot,\cdot\rangle$: on the four real-type subspaces the two agree, because there $\langle\cdot,\cdot\rangle$ is real-valued, while on the centre and the vector subspace they do not — the complex null set of $\langle\cdot,\cdot\rangle$ is the origin on the centre and the complex cone of real dimension $4$ on the vector subspace, against the two real lines and the cone of real dimension $5$ found here. On the vector subspace the cone $\sum_kq_k^2=\sum_k(q'_k)^2$ contains the totally isotropic real plane $\mathrm{span}_{\mathbb{R}}\{e_1+ie_1,\ e_2+ie_2\}$, and the three elements $e_k+ie_k$ span a totally isotropic subspace of real dimension $3$, the maximum for signature $(3,3)$.

## The Material Interpretation

The reading is a reading and not a theorem; it is the one the corpus gives to the four forms and it is sharpened here by the remarkable subspaces.

- On the **material sector** $\mathbb{M}_-$ the four forms are real and the article adds nothing to the four algebraic norms: the interval, the Euclidean square and their negatives. The material sector carries no imaginary part, so it carries no phase pairing, and the light cone there is the interval's.
- On the **two complex subspaces** the four forms carry, besides the intervals and the squares of their algebraic norms, a second real form: symmetric for the two bilinear forms, and alternating for the two sesquilinear ones. The alternating companion is non-degenerate, so the centre carries one canonical pair and the vector subspace three, one to a spatial direction.
- The alternating companion is the **phase**, or area, pairing: the object a canonical pair needs, and the one the corpus has so far read only through the imaginary part of the Hermitian form. On the centre it is the pairing of the complex line with itself, of rank $2$; on the vector subspace it is the pairing of the three complex directions, of rank $6$; on the four real-type subspaces, and in particular on the material sector, it is absent.

So the corpus's four forms are, on the two complex subspaces, **four intervals and two symplectic forms**, and on the four real-type subspaces four intervals alone. The second half of that sentence is what *Remarkable Subspaces and the Four Algebraic Norms* records; the first half is what this article adds.

## Summary

The four forms of *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space* are read on the remarkable subspaces of *Introduction to the Remarkable Subspaces*, one subspace to a section. The restriction of a form to a subspace is the form read on the elements of the subspace; it inherits symmetry or conjugate-symmetry, the real scalar laws and non-degeneracy, and all twenty-four restrictions are non-degenerate.

The forms split as $\varphi=g+i\sigma$, with $g$ real symmetric and $\sigma$ real, symmetric for $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{\natural}$ and alternating for $\langle\cdot,\cdot\rangle_{*}$ and $\langle\cdot,\cdot\rangle_{\natural*}$. The imaginary part vanishes on the four real-type subspaces, $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$ and $\mathbb{M}_-$, where all four forms are real-valued, and it is non-zero and non-degenerate on the two complex subspaces, the centre and the vector subspace, of rank $2$ and rank $6$. The real part has the signature of the algebraic norm of *Remarkable Subspaces and the Four Algebraic Norms*, and its algebraic norm is that norm.

The four forms collapse on the remarkable subspaces as $\langle\cdot,\cdot\rangle=\langle\cdot,\cdot\rangle_{\natural}$ and $\langle\cdot,\cdot\rangle_{*}=\langle\cdot,\cdot\rangle_{\natural*}$ on the centre, $\langle\cdot,\cdot\rangle=-N$ and $K=-H$ on the vector subspace, $\langle\cdot,\cdot\rangle=\langle\cdot,\cdot\rangle_{\natural*}$ and $\langle\cdot,\cdot\rangle_{\natural}=\langle\cdot,\cdot\rangle_{*}$ on the quaternion subspace, $\langle\cdot,\cdot\rangle=-K$ and $N=-H$ on the anti-quaternion subspace, $\langle\cdot,\cdot\rangle=\langle\cdot,\cdot\rangle_{*}$ and $\langle\cdot,\cdot\rangle_{\natural}=\langle\cdot,\cdot\rangle_{\natural*}$ on the Hermitian subspace and $\langle\cdot,\cdot\rangle=-H$ and $N=-K$ on the anti-Hermitian subspace. On the two complex subspaces the imaginary part is read off the real part by the complex structure, $\omega(\tilde P,\tilde Q)=+g(\tilde P,i\tilde Q)$ for $\langle\cdot,\cdot\rangle_{*}$ and $\langle\cdot,\cdot\rangle_{\natural*}$ and $\sigma(\tilde P,\tilde Q)=-g(\tilde P,i\tilde Q)$ for $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{\natural}$, the one sign being the whole difference between the two pairs.

The null sets are four origins on the centre; on the vector subspace two cones and two origins, the cones being the complex cone of the bilinear pair; and on each of the four real-type subspaces two light cones and two origins. The rule is that off the centre a form has a complex null cone on a subspace exactly when the restriction of its real part is indefinite there; $\langle\cdot,\cdot\rangle_{*}$ is definite on all six and every other form has a cone on some subspace.

Read as a metric, the restriction carries the orthogonal group of its signature: $O(1,1)$, $O(3,3)$, $O(1,3)$, $O(3,1)$, $O(4)$ and $O(4)$ on the centre, the vector subspace, the quaternion subspace, the anti-quaternion subspace and the two Hermitian subspaces, of real dimensions $1$, $15$, $6$, $6$, $6$ and $6$. The four real-type rows are the real forms of the complex orthogonal group $O_4(\mathbb{C})$, of $O(1,3)$ and $O(4)$; the two complex rows are the realified groups, larger than the complex groups $O_1(\mathbb{C})$ and $O_3(\mathbb{C})$ because a real-linear form preservation need not respect the complex structure. The realified form $g_B$ of signature $(4,4)$ has the Hermitian subspace as a maximal positive definite subspace and the anti-Hermitian subspace as a maximal negative definite one, orthogonal complements of one another, and it splits orthogonally three ways, $\mathbb{C}_{\mathbb{B}}\perp\mathrm{Vect}(\mathbb{B})$ of signatures $(1,1)\perp(3,3)$, $\mathbb{H}_{\mathbb{B}}\perp i\mathbb{H}_{\mathbb{B}}$ of $(1,3)\perp(3,1)$ and $\mathbb{M}_+\perp\mathbb{M}_-$ of $(4,0)\perp(0,4)$. The real zeros of $g_B$ are the four isotropic rows with the null elements $e_0+ie_0$, $e_1+ie_1$, $e_0+e_1$ and $ie_0+ie_1$, of real dimensions $1$, $5$, $3$ and $3$; on the two complex subspaces they are not the complex null sets of the table above, which are the complex zeros of the form.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\varphi|_U(\tilde P,\tilde Q)$ | the restriction of a form to the subspace $U$, the form read on the elements of $U$ |
| $g=\operatorname{Re}\varphi$ | the real part, a real symmetric bilinear form on $U$ |
| $\sigma_B$, $\sigma_N$ | the imaginary parts of the two bilinear forms, real and symmetric |
| $\omega_H$, $\omega_K$ | the imaginary parts of the two sesquilinear forms, real and alternating |
| $\omega(\tilde P,\tilde Q)=+g(\tilde P,i\tilde Q)$ | the Kähler identity for $\langle\cdot,\cdot\rangle_{*}$ and $\langle\cdot,\cdot\rangle_{\natural*}$, on the centre and on the vector subspace |
| $\sigma(\tilde P,\tilde Q)=-g(\tilde P,i\tilde Q)$ | the companion identity for $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{\natural}$, with the opposite sign, on the same two |
| $(1,1),(2,0),(3,3),(6,0),(0,6),(1,3),(3,1),(4,0),(0,4)$ | the signatures of the real parts on the remarkable subspaces |
| rank $2$, rank $6$ | the ranks of the imaginary parts on the centre and on the vector subspace |
| the Gram matrix in the complex basis | the submatrix of the $4\times4$ matrix of the form: $(1)$ on the centre, $-\mathrm I_3$ and $\mathrm I_3$ on the vector subspace, the real $4\times4$ algebraic norms on the four real-type subspaces; its rank is the rank of the form |
| $g$ and $\sigma$ in the real basis | the two parts as real matrices of twice the size: $\mathrm I_6$ and the block sum of three $\begin{pmatrix}0&-1\\ 1&0\end{pmatrix}$ on the vector subspace; the combined array $g+i\sigma$ is **not** the Gram matrix and is not read with the determinant rule |
| $\langle\cdot,\cdot\rangle=\langle\cdot,\cdot\rangle_{\natural}$, $\langle\cdot,\cdot\rangle_{*}=\langle\cdot,\cdot\rangle_{\natural*}$; $\langle\cdot,\cdot\rangle=-N$, $K=-H$; $\langle\cdot,\cdot\rangle=\langle\cdot,\cdot\rangle_{\natural*}$, $\langle\cdot,\cdot\rangle_{\natural}=\langle\cdot,\cdot\rangle_{*}$; $\langle\cdot,\cdot\rangle=-K$, $N=-H$; $\langle\cdot,\cdot\rangle=\langle\cdot,\cdot\rangle_{*}$, $\langle\cdot,\cdot\rangle_{\natural}=\langle\cdot,\cdot\rangle_{\natural*}$; $\langle\cdot,\cdot\rangle=-H$, $N=-K$ | the collapse patterns, one to a subspace |
| the light cone | the null cone of the Minkowski form on the four real-type subspaces; on the material sector it is the null cone of the interval $\langle\cdot,\cdot\rangle_{\natural}$ of signature $(3,1)$ and of its negative $\langle\cdot,\cdot\rangle_{\natural*}$ of signature $(1,3)$ |
| $O(1,1)$, $O(3,3)$, $O(1,3)$, $O(3,1)$, $O(4)$ | the automorphism groups of the restrictions of $\langle\cdot,\cdot\rangle$, of real dimensions $1$, $15$, $6$, $6$, $6$ and $6$; the four real-type rows are the real forms of $O_4(\mathbb{C})$ |
| $\mathbb{C}_{\mathbb{B}}\perp\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}\perp i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+\perp\mathbb{M}_-$ | the three orthogonal splittings of the algebra by $g_B$, of signatures $(1,1)\perp(3,3)$, $(1,3)\perp(3,1)$ and $(4,0)\perp(0,4)$ |
| $e_0+ie_0$, $e_1+ie_1$, $e_0+e_1$, $ie_0+ie_1$ | the null elements of the four indefinite rows for the real part $g_B=\operatorname{Re}B$, whose real null cones have real dimensions $1$, $5$, $3$ and $3$ |

## Further Reading

- *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/the-4-forms-over-the-biquaternioid-c-space.md`), for the four forms, their count, their definition with the one bracket whose subscript records the pair, the two slots and the four names.
- *Remarkable Subspaces and the Four Algebraic Norms* (`articles_maths/remarkable-subspaces-and-the-four-algebraic-norms.md`), the article of the algebraic norms, for the four algebraic norms on the same remarkable subspaces, the signature table recalled here, the definiteness of $\langle\cdot\rangle_{*}$ on all six and the material reading of the interval and the Euclidean square.
- *Remarkable Subspaces and the Four General Products* (`articles_maths/remarkable-subspaces-and-the-four-general-products.md`), for the four general products — the operations whose scalar parts the four forms are — read on the same remarkable subspaces, with their symmetrisations and their brackets.
- *Introduction to the Remarkable Subspaces* (`articles_maths/introduction-to-the-remarkable-subspaces.md`), for the remarkable subspaces, their defining conditions, their real bases and the dimensions used throughout.
- *Conventions in the Biquaternion Universe* (`articles_physics/conventions-in-the-biquaternion-universe.md`), for the convention of the four pairings, the one bracket, the four names and the four pairs, and the readings of the four on the algebra and on the material sector.
- *The Four General Products and Their Physical Readings* (`articles_physics/the-four-general-products-and-their-physical-readings.md`), for the four readings of the four forms — composition, probability, causality and gauge — and their signature table on the remarkable subspaces.
- *The Norm Defined by a Form* (`articles_maths/the-norm-defined-by-a-form.md`) and *Hermitian Forms over Algebras and Norms* (`articles_maths/hermitian-forms-over-algebras-and-norms.md`), for the passage from a form to its algebraic norm and from the algebraic norm to the topological norm, and for the real part, the imaginary part and the alternating companion of a Hermitian form.
