# __Bhabha Multi-Mass Wave Equations and the Bivector Space in Biquaternionic Form__

## Introduction

The mass formula of the companion *The Spin–Mass Formula and the Spectrum of Elementary Particles in Biquaternionic Form* comes from a family of wave equations, not from a single one. These are the **relativistic wave equations of Bhabha, Gel'fand and Yaglom**: finite-dimensional equations for a field in an arbitrary Lorentz representation $\tau^{l\bar l}$, whose mass operator is a matrix and whose determinant is a polynomial in $p^2$ with several roots — one field, several masses. When the representation is an interlocking chain $(l,\bar l)\oplus(\bar l,l)$, the equation describes a particle of generalised spin $s=|l-\bar l|$ and mass $m$. The chain that carries the proton is a case in point: the proton is assigned to the member $\tau^{59/2,29}$, of degree $3540$, taken together with its conjugate.

This article records the equations, the spin chains they live on, and the third ingredient the programme attaches to them: the reduction of the equations from Minkowski space to the **bivector space** $\mathbb{R}^6$. The reduction is not decorative. The Lorentz group is six-dimensional and so is the space of antisymmetric two-tensors — the bivectors, the field strengths. The programme maps the wave equations into that space and writes them there. The corpus knows the space under another name: the field-strength biquaternion $\vec E+i\vec B$ of *The Field-Strength Biquaternion and Its Invariants* has six real components and is exactly a point of the bivector space. The article notes the identification and states where it stops.

It is worth separating this article from the companion that shares the name Bhabha. *Bhabha Scattering in Biquaternionic Form* is about the elastic scattering of an electron and a positron; the present article is about Bhabha's *wave equations*, a different piece of work by the same author. The two are cross-referenced and not merged.

**Notation, once.** The imaginary unit is the central $i$ of $\mathbb{B}$, with $i^2=-1$. Displayed formulae are written with their imaginary units reduced whenever the algebra allows it; where the source's own conventions leave a reduction undecided, the display is transcribed as printed and the undecided step is flagged rather than silently repaired. The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with units $e_t=1$ and $\vec e_x,\vec e_y,\vec e_z$, the three squaring to $-e_t$. The two-sided cells act by $L_aR_b\psi=a\psi b$, and the **generator cell** of the coordinate $x_\mu$ is $G_\mu=iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}$, with $\nu(t)=x$ and $\nu(k)=y$ for $k=x,y,z$; the chirality cell is $-iR_{\vec e_z}^{\mathrm{axf}}$. The gammas are the frame names of the same cells and appear only in the section *The Legacy Pauli Gamma Formulation*; no gamma-matrix is used before it.

**The order of the article.** A first section fixes the spintensors and the spin chains. A second states the wave equations and the determinant argument. A third gives the bivector-space reduction and settles its metric and its index order. A fourth works the proton chain and writes the Dirac limit in its two forms, the one-sided chiral pair and the two-sided cell equation. A fifth states the biquaternion interpretation and separates what is established from what is transcribed; the gammas are collected in a section of their own before the summary.

**The articles it leans on.**

- Companion article *The Spin–Mass Formula and the Spectrum of Elementary Particles in Biquaternionic Form*, for the mass spectrum these equations produce.
- Companion article *The Spin–Charge Hilbert Space and the SU(3) Supermultiplets in Biquaternionic Form*, for the space in which the multi-mass fields are placed.
- Corpus article *The Field-Strength Biquaternion and Its Invariants*, for the biquaternion form of the bivector space.
- Corpus article *The Dirac–Hestenes Equation and Spacetime Algebra in Biquaternionic Form*, for the spinor form of the Dirac and Maxwell equations used in the Dirac limit.
- Corpus article *Bispinor Fields and the Fundamental Solution of the Generalized Maxwell–Dirac Equation*, for the Maxwell–Dirac package in the corpus's own form.
- Corpus article *Bhabha Scattering in Biquaternionic Form*, for the other work bearing Bhabha's name.

## Spintensors and the Spin Chains

### The Spintensor

A representation of $\mathrm{SL}(2,\mathbb{C})$ is carried by a **spintensor** with $k$ unbarred and $r$ barred indices,

$$
S = s_{\alpha_1\alpha_2\dots\alpha_k\bar\alpha_1\bar\alpha_2\dots\bar\alpha_r},
$$

a polynomial in the products of the unbarred and barred spinors $s_\alpha$ and $s_{\bar\alpha}$. The representation is $\tau^{l\bar l}$ with

$$
l = \tfrac{k}{2}, \qquad \bar l = \tfrac{r}{2}.
$$

The spintensor is the image of the tensor product of $k$ fundamental factors and $r$ conjugate factors,

$$
\underbrace{\mathbb{C}^2\otimes\cdots\otimes\mathbb{C}^2}_{k}\otimes
\underbrace{\bar{\mathbb{C}}^2\otimes\cdots\otimes\bar{\mathbb{C}}^2}_{r},
$$

and its spin space is

$$
\underbrace{S_2\otimes\cdots\otimes S_2}_{k}\otimes
\underbrace{\bar S_2\otimes\cdots\otimes\bar S_2}_{r}
$$

with $2^{k+r}$ components. The indices within each group can be permuted, so a spintensor may be taken **symmetric**; the space $\mathrm{sym}^{(k,r)}$ of symmetric spintensors has dimension

$$
\dim\mathrm{sym}^{(k,r)} = (k+1)(r+1),
$$

the **degree** of the representation $\tau^{l\bar l}$. This is the number that the mass formula uses: because $l=k/2$ and $\bar l=r/2$, the degree is $(2l+1)(2\bar l+1)=4\bigl(l+\tfrac12\bigr)\bigl(\bar l+\tfrac12\bigr)$.

**The degree does not name the representation.** Degree $4$ is carried by $\tau^{\frac12,\frac12}$, of generalised spin $0$, and by $\tau^{\frac32,0}$, of generalised spin $\frac32$; degree $15$ by $\tau^{2,1}$, of spin $1$, and by $\tau^{7,0}$, of spin $7$. Inside one spin line the degree strictly increases with the chain index, so there the index is recoverable from the degree. Across lines it is not: a mass formula that reads $m=\frac{\mu_0}{4}\deg\tau$ assigns one mass to particles of different spin, because the mass is a function of the degree and the degree does not fix the particle.

### The Two Schemes

The representations do not stand alone. $\tau^{l\bar l}$ and $\tau^{l_2\bar l_2}$ are **interlocking** when $l_2=l\pm\frac12$ and $\bar l_2=\bar l\pm\frac12$, the two signs being independent. The interlocking relations group the spin lines into two schemes. The **Bose scheme** carries the integer-spin lines, the spin-$0$, spin-$1$, $\dots$ lines; the **Fermi scheme** carries the half-integer-spin lines, the spin-$\frac12$, spin-$\frac32$, $\dots$ lines. Every spin value $s$ has its own infinite line inside its scheme, and the line is the chain of representations reached from $s$ by single interlocking steps. A **field of type $(l,\bar l)\oplus(\bar l,l)$** is a field transforming in a representation and its conjugate; the wave equations of the next section are written for such fields and describe a particle of generalised spin

$$
s = |l-\bar l| .
$$

The usual spin is recovered only on the restriction $\tau^{l\bar l}\to\tau^{l,0}$ (or $\to\tau^{0,\bar l}$), that is, at $\mathrm{SU}(2)\subset\mathrm{SL}(2,\mathbb{C})$, where the spin values run over $-l,-l+1,\dots,l$.

## The Wave Equations and the Determinant Argument

### The Equation and Its Determinant

The equations are written with the generator matrices $M^{l\bar l}_\mu$ of the representation $\tau^{l\bar l}$, one for each of the four coordinates, and read, for the field $\psi$ of the representation,

$$
iM^{l\bar l}_\mu\frac{\partial\psi}{\partial x_\mu}+m\psi=0,
\qquad\text{that is}\qquad
M(p)\psi=-m\psi,
$$

with $M(p)=M_0p_0-M_1p_1-M_2p_2-M_3p_3$ for a plane wave of momentum $p$. A nonzero solution requires

$$
D(p) = \det\bigl(M(p)+mE\bigr) = 0 .
$$

The determinant is a polynomial in $p_0,p_1,p_2,p_3$ and is constant on the transitivity surfaces of the Lorentz group, the hyperboloids $s^2(p)=p_0^2-p_1^2-p_2^2-p_3^2=\text{const}$, so it depends on $s^2$ alone and factors as

$$
\boxed{\;D\bigl(s^2\bigr) = \kappa\bigl(s^2-m_1^2\bigr)\bigl(s^2-m_2^2\bigr)\cdots\bigl(s^2-m_k^2\bigr)\;}.
$$

The equation has a solution exactly when $s^2=m_i^2$, so the roots $m_i$ are the masses the field can carry: a multi-mass field. Their number is bounded by the dimension. $D$ has degree at most $N$ in the momentum and depends on $s^2$ alone, so its degree in $s^2$ is at most $N/2$: a representation of dimension $N$ carries at most $N/2$ masses, which is the rest-frame $\pm$ pairing of the $N$ roots read the other way round.

### The Eigenvalues at Rest

Putting $\vec p=0$ makes $M(p)=p_0M_0$ and

$$
\det\bigl(p_0M_0+mE\bigr) = \prod_{i=1}^{N}\bigl(\lambda_ip_0+m\bigr),
$$

with $\lambda_i$ the eigenvalues of $M_0$ and $N$ the dimension of the representation. The source compares this with the factorisation

$$
\det\bigl(p_0M_0+mE\bigr) = \kappa\,\bigl(p_0-\mu_0\lambda_1\bigr)\bigl(p_0-\mu_0\lambda_2\bigr)\cdots\bigl(p_0-\mu_0\lambda_N\bigr),
$$

and reads off the relation

$$
m_1 = \mu_0\lambda_1,\quad -m_1=\mu_0\lambda_2,\quad m_2=\mu_0\lambda_3=-\mu_0\lambda_4,\ \dots
$$

which it writes first in this linear form for the general $\tau^{l\bar l}$; for the representations of type $\tau^{0,\bar l}$, where only the barred label runs, the same display holds with the barred eigenvalues alone, and in the general case the eigenvalues enter as products,

$$
m_1 = \mu_0\lambda_1\bar\lambda_1,\qquad -m_1=\mu_0\lambda_2\bar\lambda_2,\qquad m_2=\mu_0\lambda_3\bar\lambda_3=-\mu_0\lambda_4\bar\lambda_4,\ \dots
$$

**Why the spectrum is symmetric.** The source records the $\pm$ pairing as an observation: each non-null eigenvalue $\lambda$ of $M_0$ occurs with $-\lambda$ of the same multiplicity. It is not a separate assumption, and the reason is already in hand. At $\vec p=0$ the determinant is $\prod_i(\lambda_ip_0+m)$, and it is also $D(p_0^2)$, an even function of $p_0$, because $D$ depends on the momentum only through $s^2$. Expanding the product in $p_0$, the coefficient of $p_0^{2j+1}$ is $m^{N-2j-1}e_{2j+1}$, with $e_k$ the $k$-th elementary symmetric function of the $\lambda_i$; evenness therefore says $e_1=e_3=\dots=0$, and that holds exactly when the multiset $\{\lambda_i\}$ is closed under $\lambda\mapsto-\lambda$ with multiplicities preserved. The roots of $D$ are thus $\pm$ pairs — which is why the source's list contains $m_1$ and $-m_1$ — and a positive mass can be read from each pair only once the normalisation is fixed.

**A check of the comparison.** Taken literally, the two displays are not the same polynomial. The roots of $\det(p_0M_0+mE)$ are $p_0=-m/\lambda_i$, while the second display has roots $p_0=\mu_0\lambda_i$; the two agree only if $\mu_0\lambda_i=-m/\lambda_i$ for every eigenvalue, that is if all $|\lambda_i|$ are equal, which a general representation of the Lorentz group does not satisfy. A constant can match the two lists at one eigenvalue and at no more, so the step is not a rescaling with a scale absorbed; in terms of mass the mismatch is an inversion. The determinant gives $m_i=m/|\lambda_i|$, which falls as the eigenvalue grows, while the source's product form rises with it. The invariant content is the $\pm$ pairing; the functional form of the mass in the eigenvalues is the point the source leaves unexamined, and it is recorded below as an open question rather than silently repaired.

In the infinite-dimensional limit $l,\bar l\to\infty$ the formula becomes

$$
m^{(s)} = \mu_0\bigl(l+\tfrac12\bigr)\bigl(\bar l+\tfrac12\bigr),
\qquad s=|l-\bar l| ,
$$

which is the companion mass formula; in degree form it is $m^{(s)}=\frac{\mu_0}{4}\deg\tau^{l\bar l}$, since $(2l+1)(2\bar l+1)=4(l+\frac12)(\bar l+\frac12)$. The present article's contribution is the equations and the chains; the companion's is the spectrum and the assignments, and the two are kept separate.

## The Bivector Space $\mathbb{R}^6$

### The Metric Mapping

Minkowski space and the space of bivectors are related by the algebraic mapping

$$
g_{ab} \longrightarrow g_{\alpha\beta\gamma\delta} \equiv g_{\alpha\gamma}g_{\beta\delta}-g_{\alpha\delta}g_{\beta\gamma},
$$

which sends the metric of $\mathbb{R}^{1,3}$ to a metric on the six-dimensional space of antisymmetric two-tensors. The source's Minkowski metric is $\mathrm{diag}(-1,-1,-1,+1)$ in the coordinate order $(x_1,x_2,x_3,x_0)$, with the timelike coordinate $x_0$ listed last, and the printed bivector metric is

$$
g_{ab} = \mathrm{diag}(-1,-1,-1,+1,+1,+1).
$$

**The index order, corrected.** The source prints the collective order

$$
23\to0,\qquad 10\to1,\qquad 20\to2,\qquad 30\to3,\qquad 31\to4,\qquad 12\to5,
$$

but under that order the mapping does not reproduce the printed diagonal: componentwise it gives

$$
23\mapsto+1,\quad 10\mapsto-1,\quad 20\mapsto-1,\quad 30\mapsto-1,\quad 31\mapsto+1,\quad 12\mapsto+1,
$$

that is $(+1,-1,-1,-1,+1,+1)$. The printed diagonal is reproduced exactly by the order

$$
10\to0,\qquad 20\to1,\qquad 30\to2,\qquad 23\to3,\qquad 31\to4,\qquad 12\to5,
$$

which lists the three boosts first and the three rotations second: the pairs $10,20,30$ contain the timelike index $0$ and give $-1$, while the pairs $23,31,12$ are purely spatial and give $+1$. Two repairs would reconcile the printed table with the mapping: change the order, or change three signs of the metric. The order is the likelier slip, because the printed diagonal is the one the mapping must give — three negative boost directions and three positive rotation directions — and altering it would leave the bivector metric unrelated to the Minkowski metric it is defined from. The equations below are written in the $a_j$ basis and do not use the collective order at all, so the slip is confined to the display.

The inertia $(3,3)$ is the inertia of the Lorentz Lie algebra's Killing form, in the same order: three negative directions for the non-compact boosts and three positive for the compact rotations. The bivector space is $\mathbb{R}^6$ as a real vector space; the identification with $\mathbb{C}^3$ needs a complex structure, and the metric is not the positive-definite form that a Hermitian metric on $\mathbb{C}^3$ would give — it is the split form, with three directions of each sign. The two structures are therefore not interchangeable: $\mathbb{C}^3$ names a complex structure on $\mathbb{R}^6$, and the metric $g_{\alpha\beta\gamma\delta}$ is a separate choice on the same space.

**A note on the two orders of the coordinates.** The corpus's cell frame lists the time coordinate first and writes $\varepsilon=(1,-1,-1,-1)$, the opposite of the source's order; the two metrics are the same metric written in opposite orders. The article keeps each order where it is used and never mixes them in one display.

### The Equations in $\mathbb{R}^6$

Mapping the wave equations into $\mathbb{R}^6$ turns the four spacetime derivatives into six bivector derivatives. The equation is written with the tensor-product generator

$$
\Pi_j := M^{l}_j\otimes\mathbf{1}_{2\bar l+1}-\mathbf{1}_{2l+1}\otimes M^{\bar l}_j,
$$

in which $M^{l}_j$ and $M^{\bar l}_j$ are the generators of the two factors. With $a_j$ the three complex coordinates of $\mathbb{C}^3$, $a_j^*$ their conjugates, $\dot\psi$ the conjugate field and $\tilde a_j$ the dual coordinates, the source's equation and its conjugate read

$$
\boxed{\;
\begin{aligned}
\sum_{j=1}^{3}\Pi_j\frac{\partial\psi}{\partial a_j}
+i\sum_{j=1}^{3}\Pi_j^{*}\frac{\partial\psi}{\partial a_j^{*}}+m\psi &= 0,\\[6pt]
\sum_{j=1}^{3}\Pi_j^{*}\frac{\partial\dot\psi}{\partial\tilde a_j^{*}}
-i\sum_{j=1}^{3}\Pi_j\frac{\partial\dot\psi}{\partial\tilde a_j}+m\dot\psi &= 0.
\end{aligned}
\;}
$$

Here $\Pi_j^{*}$ is $\Pi_j$ with both factors conjugated.

**The two lines are written in opposite orders.** The first line's generator puts the unbarred factor first, $M^{l}_j\otimes\mathbf{1}_{2\bar l+1}-\mathbf{1}_{2l+1}\otimes M^{\bar l}_j$. The source's second line puts the barred factor first, $M^{\bar l}_j\otimes\mathbf{1}_{2l+1}-\mathbf{1}_{2\bar l+1}\otimes M^{l}_j$: the same operator on the same space, with the two tensor factors interchanged. Each line is dimensionally consistent on its own, and the interchange is legitimate, because the conjugate field $\dot\psi$ is written on $\bar V\otimes V$ rather than on $V\otimes\bar V$. The display above keeps one ordering for both lines; the interchange is a choice of basis, not a correction.

**A check of the imaginary units.** The $i$ of the second sum is not decorative, and the source's own conventions do not decide whether it can be removed. Alongside the equation it writes $g_4=ia_1,\dots,g_6=ia_3$ and $a_1^*=-ig_4,\dots,a_3^*=-ig_6$; the two relations together give $a_j^*=a_j$, which cannot be a conjugation, so at least one of them is a slip. With $a_j^*=-ig_{j+3}$ read as the definition, $\partial/\partial a_j^*=i\,\partial/\partial g_{j+3}$; the $i$ of the second sum then meets the chain-rule $i$, and $i^2=-1$ replaces the pair by a minus. If instead $g_{j+3}=ia_j^*$ is taken as the coordinate, the pair of relations is consistent and the same reduction holds. Either correction removes the $i$; the printed pair, read literally, does not. The display above keeps the $i$ as printed, and the open question below records which relation is meant to be the definition.

The equations are defined in the three-dimensional complex space $\mathbb{C}^3$, which is the bivector space in its complex form; the generalised spin is $s=|l-\bar l|$ and the mass is $m$, exactly as in Minkowski space. The structure of the equations — a difference of two tensor-product generators contracted with a derivative — is the structure that becomes the generator cells of the Dirac equation at the first chain member.

## The Proton Chain and the Dirac Limit

### The Chain

The chain that carries the nucleon is the spin-$\frac12$ line's Fermi-scheme chain

$$
\Bigl(\tfrac12,0\Bigr)\longleftrightarrow\Bigl(0,\tfrac12\Bigr)
\ \longrightarrow\
\Bigl(1,\tfrac12\Bigr)\longleftrightarrow\Bigl(\tfrac12,1\Bigr)
\ \longrightarrow\ \cdots\ \longrightarrow\
\Bigl(\tfrac{59}{2},29\Bigr)\longleftrightarrow\Bigl(29,\tfrac{59}{2}\Bigr)\ \longrightarrow\ \cdots
$$

The first member is the **fundamental doublet**: the representation $\tau^{\frac12,0}\oplus\tau^{0,\frac12}$, four complex components in all — the two spin projections $\pm\frac12$ in two copies, one copy from each factor — which is the **electron**. The Dirac field reads the two copies as the two chiralities, which in the massless limit are the two helicities. Each single arrow is one interlocking step, adding $\frac12$ to both labels; each double arrow pairs a representation with its conjugate.

### The Two Dirac Equations

On the fundamental doublet the Bhabha equation is the Dirac equation, and the corpus writes that equation in two forms that must not be read as one.

**The chiral pair.** On the Dirac module $\Delta=S\oplus S^{\mathrm{c}}$, with $\psi=\psi_L+\psi_R$, $\psi_L\in S$ and $\psi_R\in S^{\mathrm{c}}$, the equation is the one-sided pair

$$
\boxed{\;\tilde\nabla\psi_R=m_e\psi_L,\qquad \tilde\nabla^{\natural}\psi_L=m_e\psi_R\;}
$$

with

$$
\tilde\nabla=e_t\frac{\partial}{\partial Q_t}+\vec e_x\frac{\partial}{\partial Q_x}+\vec e_y\frac{\partial}{\partial Q_y}+\vec e_z\frac{\partial}{\partial Q_z}
$$

and $\tilde\nabla^{\natural}$ its conjugate, the natural conjugation $\natural$ applied to the units. One equation per chirality; the mass couples the two. At $m_e=0$ the pair decouples into $\tilde\nabla\psi_R=0$ and $\tilde\nabla^{\natural}\psi_L=0$. Applying $\tilde\nabla^{\natural}$ to the first member and using the second gives

$$
\Box\psi_R=m_e^2\psi_R,
\qquad
\Box=\tilde\nabla\tilde\nabla^{\natural}=\tilde\nabla^{\natural}\tilde\nabla
=\frac{\partial^2}{\partial Q_t^2}+\Delta ,
$$

so each chiral half obeys the Klein–Gordon equation.

**The two-sided cell equation.** On the same module the pair is one equation in which the derivatives act through two-sided cells. In the real coordinates $x_0=ct'$, with $Q_t=ix_0$ and $\partial/\partial Q_t=-i\,\partial/\partial x_0$, it is

$$
\boxed{\;(\mathbb{D}-m_e)\psi=0,\qquad
\mathbb{D}=-R_{\vec e_x}^{\mathrm{axf}}\frac{\partial}{\partial x_0}-\sum_{k=1}^{3}L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\frac{\partial}{\partial x_k}\;}
$$

The operator is the four generator cells contracted with the four derivatives; the $i$ of each cell cancels the $i$ in front, and the expanded form has no imaginary unit:

$$
G_0=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}=iR_{\vec e_x}^{\mathrm{axf}},\qquad
G_k=iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\qquad
\mathbb{D}=i\sum_{\mu=0}^{3}G_\mu\frac{\partial}{\partial x_\mu}.
$$

The cells carry the cell relation of $\varepsilon=(1,-1,-1,-1)$,

$$
\{G_\mu,G_\nu\}=2\varepsilon_\mu\delta_{\mu\nu}I_4,\qquad G_0^2=I_4,\qquad G_k^2=-I_4,
$$

so distinct cells anticommute, the cross terms of $\mathbb{D}^2$ vanish, and

$$
\mathbb{D}^2=-\frac{\partial^2}{\partial x_0^2}+\Delta=\Box .
$$

Hence $(\mathbb{D}-m_e)\psi=0$ implies $(\Box-m_e^2)\psi=0$, the same Klein–Gordon consequence as the pair. The mass enters with the scalar coefficient $-m_e$.

The chirality is the right multiplication $\chi=-iR_{\vec e_z}^{\mathrm{axf}}$, an involution with eigenvalues $\pm1$ of multiplicity two that splits $\Delta$ into the two chiral halves. It anticommutes with every generator cell, and therefore with $\mathbb{D}$,

$$
\chi\mathbb{D}\chi=-\mathbb{D},
$$

so the single equation is the pair $\mathbb{D}\psi_R=m_e\psi_L$ and $\mathbb{D}\psi_L=m_e\psi_R$: $\mathbb{D}\psi_R$ lies in the left half, where $m_e\psi_L$ lives, and $\mathbb{D}\psi_L$ lies in the right. The mass is a scalar and therefore even under $\chi$; it is exactly because $\mathbb{D}$ is odd and $m_e$ even that one equation links the halves at all. Chirality supplies the two equations, and the two-sided operator is what lets one equation hold them.

**How the two are one.** The pair is the definition on the two chiral halves; the cell equation is its representative on the single module $\Delta$. The two are related by the dictionary of *The Dirac Equation in Biquaternionic Form*, they have the same square and the same massless content, and neither is a second physics. What distinguishes them is the side of the action: the pair is one-sided, left multiplication by $\tilde\nabla$ or $\tilde\nabla^{\natural}$, while the cell equation uses the two-sided cells, the time derivative acting from the right and the spatial derivatives from both sides.

The two squares are one operator in two coordinates, and one substitution shows it. In the complex coordinate $Q_t=ix_0$ the pair's square is $\partial^2/\partial Q_t^2+\Delta$, and $\partial/\partial Q_t=(1/i)\,\partial/\partial x_0$ gives $\partial^2/\partial Q_t^2=-\partial^2/\partial x_0^2$, which is the cell operator's square. The product $\tilde\nabla\tilde\nabla^{\natural}$ equals $\tilde\nabla^{\natural}\tilde\nabla$, so the order in which the pair is squared does not matter.

### The Proton

The nucleon sits on the same chain, far up it. The programme takes the chain member

$$
\tau^{\frac{59}{2},29}\oplus\tau^{29,\frac{59}{2}}
$$

as the proton. The first factor has degree $(2l+1)(2\bar l+1)=60\times59=3540$, and the conjugate factor has the same dimension, so the pair carries $7080$ components. The mass comes from the formula of the previous section. Normalising so that the electron's fundamental representation gives

$$
m_e=\mu_0\Bigl(\frac12+\frac12\Bigr)\Bigl(0+\frac12\Bigr)=\frac{\mu_0}{2},
$$

the ratio is

$$
\boxed{\;\frac{m_p}{m_e} = \frac{(2l+1)(2\bar l+1)}{2}
=2\Bigl(l+\frac12\Bigr)\Bigl(\bar l+\frac12\Bigr)\;}
$$

and $(59/2,29)$ gives $60\times59/2=1770$. The product $(l+\frac12)(\bar l+\frac12)=30\times29.5=885$ is $m_p/\mu_0$, not the ratio: since $m_e=\mu_0/2$, the ratio is twice that product. The source's own line $m_e=\mu_0(l+\frac12)=\mu_0$ drops the second factor $\bar l+\frac12=\frac12$, and that dropped factor is the whole of the factor of two. Its condition $(l+\frac12)(\bar l+\frac12)\approx1800$ becomes $\approx918$ once the mass formula is applied to the electron as well as to the proton; the member's $885$ falls short of $918$ by $3.6\%$, which is the $1770$ against $1836$.

The proton's equation in $\mathbb{R}^6$ is the equation of the $\tau^{59/2,29}$ factor — $3540$ components for the factor, doubled for the pair — with $M^{59/2,29}_j$ replacing $M^{1/2,0}_j$. Mapping the Dirac equation into $\mathbb{R}^6$ gives the generators $M^{\frac12,0}_j=\tfrac12c_{\frac12,\frac12}\sigma_j$: up to the normalisation constant, the three of them are the **Pauli matrices**, which the value $c_{\frac12,\frac12}=2$ makes exact. This is the concrete way in which the chain's first member carries the Dirac equation, and it is the dictionary the corpus records in *The Daviau Map and the Space Clifford Formulation of the Dirac Equation*, $\mathsf{M}_2(i\vec e_k)=\sigma_k$.

The programme's stated reason for moving up the chain is that the first member is algebraically too simple to carry the proton's internal structure. The move itself is a **choice**, not a derivation.

## The Biquaternion Reading

Three points connect this material to the framework, of three different strengths: an identification of algebras, an agreement of objects, and a relation of equations.

First, the **fundamental doublet's factor** is the biquaternion algebra. $\mathbb{C}^2$ is the defining module of $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}\cong\mathbb{C}\ell_2\cong M_2(\mathbb{C})$, and the tensor product with $k$ factors of $\mathbb{C}^2$ and $r$ of $\bar{\mathbb{C}}^2$ begins at $k=r=0$ with the centre $\mathbb{C}$. The chain of spaces the programme writes for the spin-$0$ line,

$$
\mathbb{C}\longrightarrow\mathbb{C}^2\otimes\bar{\mathbb{C}}^2
\longrightarrow\bigl(\mathbb{C}^2\otimes\bar{\mathbb{C}}^2\bigr)\otimes\bigl(\mathbb{C}^2\otimes\bar{\mathbb{C}}^2\bigr)\longrightarrow\cdots,
$$

has $\mathbb{C}$ as its first member, the centre, and $\mathbb{C}^2\otimes\bar{\mathbb{C}}^2\cong\mathrm{End}(\mathbb{C}^2)=M_2(\mathbb{C})\cong\mathbb{B}$ as its second. The corpus's *Higher Spin from Tensor Products: Why the Biquaternion Algebra Admits Only Spin Zero and One-Half* gives the framework's account of the same ladder of tensor powers; the present chain is the spinor-structure programme's version. One caution: the programme writes "$\mathbb{C}^2$ and complex conjugate $\bar{\mathbb{C}}^2$ are biquaternion algebras", which conflates the algebra with its module. $\mathbb{C}^2$ is the two-dimensional complex vector space on which $\mathbb{B}\cong M_2(\mathbb{C})$ acts; the algebra is the matrix algebra, and the tensor products of the chain are tensor products of **modules** until an algebra structure is imposed. The article keeps the distinction.

Second, the **bivector space** is the corpus's field-strength space. The six-dimensional space of antisymmetric two-tensors is, after the electric–magnetic split, a pair of a vector and an axial vector, and in the corpus's notation it is the field-strength biquaternion $\vec E+i\vec B$ with six real components. The mapping $g_{ab}\to g_{\alpha\beta\gamma\delta}$ gives the metric of the six-dimensional space on which the corpus's two invariants live: the first, $\vec E^2-\vec B^2$, is the quadratic form of that metric, and the second, $\vec E\cdot\vec B$, is the pairing of $\vec E$ with $\vec B$ through the duality of the same space. The programme's $\mathbb{C}^3$ is then the complex form in which $\vec B$ and $\vec E$ are the two halves of one complex vector. This is a genuine agreement of objects, and the article records it as one.

Third, the **equations** themselves are the corpus's Dirac–Maxwell package in the programme's form. The Dirac limit's generators reduce to the Pauli matrices, and the massless limit of the pair is the Weyl pair, $\tilde\nabla\psi_R=0$ and $\tilde\nabla^{\natural}\psi_L=0$; the Maxwell field in spinor form is the programme's companion identification, and the corpus's *Bispinor Fields* derives the Maxwell–Dirac solution in its own form. The two are related and not identical, and the relation is cited rather than re-derived here. The higher chain members are the multi-mass generalisations, and they lie outside $\mathbb{B}$ exactly as the companion articles say.

## What the Framework Establishes, Transcribes, and Does Not

**Established, and recomputed.**

- The spintensor degree $\dim\mathrm{sym}^{(k,r)}=(k+1)(r+1)=(2l+1)(2\bar l+1)$ at $l=k/2$, $\bar l=r/2$, and its non-injectivity across spin lines; for the proton's first factor $60\times59=3540$.
- The $\pm$ pairing of the eigenvalues of $M_0$, derived from the evenness in $p_0$ of the rest-frame determinant.
- The bivector metric's $(3,3)$ inertia, and the printed diagonal as the componentwise image in the order $10,20,30,23,31,12$; recomputed for all six collective indices.
- The Dirac limit's cells: $\{G_\mu,G_\nu\}=2\varepsilon_\mu\delta_{\mu\nu}I_4$ with $\varepsilon=(1,-1,-1,-1)$, $iG_\mu=-L_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}$, $\mathbb{D}^2=\Box$, the product of the four generator cells equal to $-R_{\vec e_z}^{\mathrm{axf}}$, and the reduction to the Pauli matrices at $c_{\frac12,\frac12}=2$; recomputed on the explicit $4\times4$ cell representation.
- The proton-to-electron mass ratio: the product $(l+\frac12)(\bar l+\frac12)$ is $30\times29.5=885$ at $(59/2,29)$ and $1\times\frac12$ at the electron's $(1/2,0)$, so the ratio is $885/\frac12=1770$.

**Transcribed, not derived.**

- The wave equations in Minkowski space and their images in $\mathbb{R}^6\cong\mathbb{C}^3$.
- The determinant factorisation $D(p)=D(s^2)$, which is the source's Lorentz-invariance argument and is not re-proved here.
- The interlocking schemes and the assignment of the proton to the chain member $(59/2,29)$.
- The source's eigenvalue relation $m_i=\mu_0\lambda_i$ and its product form. The literal rest-frame determinant gives $m_i=m/|\lambda_i|$ instead, an inverse dependence, so the source's reading is not the determinant's reading with a scale absorbed.
- The printed collective index order, which the article corrects to the boost-first order.
- The conjugate-coordinate relations $g_{j+3}=ia_j$ and $a_j^*=-ig_{j+3}$, which cannot both hold.

**Gap, left visible.**

- The functional form of the mass in the eigenvalues — direct, as the source's product, or inverse, as the determinant — is not settled by the source.
- The two printed relations for the conjugate coordinate in $\mathbb{R}^6$ are mutually inconsistent, so whether the second sum's $i$ reduces by $i^2=-1$ is not decided by the source.
- The degree fixes the mass and not the particle, so an independent spin label is needed for every assignment.
- The passage from the abstract chain to a physical particle remains a choice fixed by the mass ratio.
- The infinite-dimensional limit is used to state the mass formula while the chains used are finite-dimensional; the same weakness as the companion mass article.
- The Dirac–Maxwell relation is cited as known and not re-derived here.

## Open Questions

1. **The eigenvalue normalisation.** The rest-frame determinant has roots $p_0=-m/\lambda_i$, so the masses it carries are $m_i=m/|\lambda_i|$, which fall as the eigenvalues grow. The source writes the roots as $p_0=\mu_0\lambda_i$ and reads off $m_i=\mu_0\lambda_i\bar\lambda_i$, which rise. The two cannot both be the statement of one determinant: they agree only if all $|\lambda_i|$ are equal, and they differ by an inversion otherwise. A reconciliation would need eigenvalues falling as the degree grows, and the generators of $\tau^{l\bar l}$ carry weights of order $l+\bar l$, which grow. As it stands, the companion's rising spectrum does not come from this determinant in the form displayed. Which dependence is intended?

2. **The conjugate coordinate in $\mathbb{R}^6$.** The source writes both $g_{j+3}=ia_j$ and $a_j^*=-ig_{j+3}$, which together give $a_j^*=a_j$. Which is the definition? Under the reading $g_{j+3}=ia_j^*$ the $i$ of the second sum reduces by $i^2=-1$; under the printed reading it does not.

3. **$\mathbb{C}^3$ versus $\mathbb{R}^6$ in the corpus's hands.** The corpus's field-strength biquaternion $\vec E+i\vec B$ is an element of the vector part of $\mathbb{B}$, which is $\mathbb{C}^3$ over the central $i$; the programme's bivector space is the real $\mathbb{R}^6$. Are the two complex structures the same — the corpus's central imaginary unit and the $i$ of the programme's $\mathbb{C}^3$ — or does the identification stop at the real space?

4. **Does the chain of algebras carry the mass spectrum?** The companion mass article orders a spin line by degree; the present chain orders the same line by algebra. Is the chain's algebra sequence the object that fixes which chain members are physical?

5. **The multi-mass sector.** The equations have several roots, only one of which is used. Are the subleading masses physical — further particles on the same chain — and does the corpus have an interpretation for them?

6. **The Maxwell–Dirac package.** The corpus's *Bispinor Fields* article derives the Maxwell–Dirac solution in the corpus's form. Does the programme's massless limit coincide with it exactly, including the conventions of the axial current?

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The bracket is the frame, on the generators as on the metric, $\gamma_\mu[\mathbb{M}_-]$ or $\gamma_\mu[\mathbb{B}]$, so that a glyph names a display and not an object of the algebra.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra. The left and right multiplications act by $L_a\psi=a\psi$ and $R_b\psi=\psi b$, and the four generator cells and the chirality cell of the body become

$$
\gamma_0[\mathbb{M}_-]=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\quad
\gamma_1[\mathbb{M}_-]=iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad
\gamma_2[\mathbb{M}_-]=iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad
\gamma_3[\mathbb{M}_-]=iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad
\gamma_5[\mathbb{M}_-]=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}.
$$

The same in the axis-free display:

$$
\gamma_0[\mathbb{M}_-]=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}},\quad
\gamma_1[\mathbb{M}_-]=iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad
\gamma_2[\mathbb{M}_-]=iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad
\gamma_3[\mathbb{M}_-]=iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad
\gamma_5[\mathbb{M}_-]=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}.
$$

Thus $\gamma_\mu[\mathbb{M}_-]=G_\mu$, and the Dirac operator of the body reads

$$
\mathbb{D}=i\sum_{\mu=0}^{3}\gamma_\mu[\mathbb{M}_-]\frac{\partial}{\partial x_\mu}.
$$

The dictionary between the two names is the single collapse

$$
i\,\gamma_\mu[\mathbb{M}_-]=-L_{e_\mu}^{\mathrm{pau}}R_{\vec e_{\nu(\mu)}}^{\mathrm{pau}},
$$

In the axis-free display:

$$
i\,\gamma_\mu[\mathbb{M}_-]=-L_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}},
$$

so multiplying a generator cell by $i$ trades it for a plain cell, and the four imaginary units of a four-fold product reduce by $i^4=+1$. In particular the volume cell is

$$
\gamma_0[\mathbb{M}_-]\gamma_1[\mathbb{M}_-]\gamma_2[\mathbb{M}_-]\gamma_3[\mathbb{M}_-]=-R_{\vec e_z}^{\mathrm{pau}}=\omega=-i\gamma_5[\mathbb{M}_-] .
$$

The same identities in the axis-free display:

$$
\gamma_0[\mathbb{M}_-]\gamma_1[\mathbb{M}_-]\gamma_2[\mathbb{M}_-]\gamma_3[\mathbb{M}_-]=-R_{\vec e_z}^{\mathrm{axf}}=\omega=-i\gamma_5[\mathbb{M}_-] .
$$

$\gamma_5[\mathbb{M}_-]=-iR_{\vec e_z}^{\mathrm{pau}}=\chi$ is the chirality cell on the module; the central grading $\chi_{\mathrm{ad}}=i\tilde\Xi_{\mathrm{ad}}$, with $\tilde\Xi_{\mathrm{ad}}$ the central root of $-e_t$ and $\chi_{\mathrm{ad}}$ the difference of the two central idempotents of the complexified algebra, so $\chi_{\mathrm{ad}}^2=e_t$, is a different object; being central, it acts on the module as a sign, and $\gamma_5[\mathbb{M}_-]$ is its representative there.

The anticommutation relations in the gamma reading are

$$
\{\gamma_\mu[\mathbb{M}_-],\gamma_\nu[\mathbb{M}_-]\}=2\varepsilon_\mu\delta_{\mu\nu}I_4,\qquad
\gamma_5[\mathbb{M}_-]^2=I_4,\qquad
\{\gamma_\mu[\mathbb{M}_-],\gamma_5[\mathbb{M}_-]\}=0,
$$

with $\varepsilon=(1,-1,-1,-1)$.

**The sign of $\gamma_5[\mathbb{M}_-]$.** With all four indices lowered the volume relation is $\gamma_5[\mathbb{M}_-]=i\gamma_0[\mathbb{M}_-]\gamma_1[\mathbb{M}_-]\gamma_2[\mathbb{M}_-]\gamma_3[\mathbb{M}_-]$, equivalently $\gamma_0[\mathbb{M}_-]\gamma_1[\mathbb{M}_-]\gamma_2[\mathbb{M}_-]\gamma_3[\mathbb{M}_-]=-i\gamma_5[\mathbb{M}_-]$. The textbook form is $\gamma_5=i\gamma^0\gamma^1\gamma^2\gamma^3$, with raised indices; raising the three spatial gammas costs three signs, so applying that convention to the same cells gives $-\gamma_5[\mathbb{M}_-]$. The overall sign of $\gamma_5[\mathbb{M}_-]$ is a labelling convention, and no equation of the body uses it. What does use it is the naming of the halves: a reader comparing with a textbook should flip the labels of $\psi_L$ and $\psi_R$.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{e_\mu}^{\mathrm{axf}}=C_{\Pi}L_{e_\mu}^{\mathrm{pau}}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

The Bhabha–Gel'fand–Yaglom wave equations place a field in an arbitrary Lorentz representation $\tau^{l\bar l}$, carried by coefficients of symmetric spintensors of degree $(k+1)(r+1)=(2l+1)(2\bar l+1)$, and give it a matrix mass whose determinant is a polynomial in $s^2=p^2$ with roots $m_i^2$. The $\pm$ pairing of the eigenvalues is a consequence of the determinant's evenness at rest; the source's reading of the masses from those eigenvalues is not the determinant's, and is recorded as an open question. The representations are organised into interlocking chains — the Bose and Fermi schemes — and the fields of type $(l,\bar l)\oplus(\bar l,l)$ carry generalised spin $s=|l-\bar l|$.

The equations can be mapped into the six-dimensional bivector space $\mathbb{R}^6\cong\mathbb{C}^3$. The printed bivector metric is the componentwise image of the Minkowski metric under the boost-first collective order $10,20,30,23,31,12$; the order printed in the source interleaves the two classes and does not reproduce it. With the corrected order, the three boosts carry $-1$ and the three rotations $+1$, which is the $(3,3)$ split of the Lorentz parameter space. The $\mathbb{R}^6$ equation keeps the source's explicit $i$ in its second sum: the source's two relations for the conjugate coordinate are mutually inconsistent, so the reduction of that pair of imaginary units by $i^2=-1$ is stated as a consequence of one reading and left open, rather than performed silently.

The first chain member is the electron's Dirac doublet, and the Dirac equation has two forms. The **chiral pair** $\tilde\nabla\psi_R=m_e\psi_L$, $\tilde\nabla^{\natural}\psi_L=m_e\psi_R$ is the one-sided definition on the two chiral halves. The **cell equation** $(\mathbb{D}-m_e)\psi=0$ is its two-sided representative on the single module, with $\mathbb{D}=-R_{\vec e_x}^{\mathrm{axf}}\partial/\partial x_0-\sum_kL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\partial/\partial x_k$ and $\mathbb{D}^2=\Box$. The two have the same square, the same massless content, and neither is a second physics: the chirality cell anticommutes with $\mathbb{D}$, and that oddness is what turns the single equation into the pair. The nucleon is taken at the chain member $(59/2,29)$ of degree $3540$; the ratio $m_p/m_e=1770$ is $3.6\%$ below the measured value.

The framework's relation to this is the fundamental doublet's factor: $\mathbb{C}^2$ is the defining module of the biquaternion algebra, the bivector space is the corpus's field-strength space, and the equations' massless limit is the corpus's Weyl pair, with the Maxwell field in spinor form as the programme's companion identification. The higher chain members lie outside $\mathbb{B}$, and the physical assignments are choices fixed by the mass ratio.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $s_{\alpha_1\dots\alpha_k\bar\alpha_1\dots\bar\alpha_r}$ | Spintensor of the representation $\tau^{l\bar l}$ |
| $l=k/2$, $\bar l=r/2$ | Lorentz labels from the numbers of unbarred/barred indices |
| $\dim\mathrm{sym}^{(k,r)}=(k+1)(r+1)$ | Degree of the representation |
| $s=\lvert l-\bar l\rvert$ | Generalised spin of the field type $(l,\bar l)\oplus(\bar l,l)$ |
| $\Delta=S\oplus S^{\mathrm{c}}$ | Dirac module, with $\psi_L\in S$ and $\psi_R\in S^{\mathrm{c}}$ |
| $M^{l\bar l}_\mu$, $M(p)$ | Generator matrices of the representation and the momentum matrix |
| $D(p)=\det(M(p)+mE)$ | Determinant whose roots are the masses |
| $\mu_0$, $\lambda_i$ | Mass scale and eigenvalues of $M_0$ |
| $g_{ab}$, order $10,20,30,23,31,12$ | Bivector-space metric and its boost-first collective order |
| $a_j$, $a_j^*$ | Three complex bivector coordinates and their conjugates |
| $\Pi_j=M^{l}_j\otimes\mathbf{1}-\mathbf{1}\otimes M^{\bar l}_j$ | Tensor-product generator of the $\mathbb{R}^6$ equation |
| $\mathbb{C}^3\cong\mathbb{R}^6$ | Complex form of the bivector space, Lorentz parameter space |
| $(59/2,29)$, degree $3540$ | The proton's chain member |
| $\tilde\nabla$, $\tilde\nabla^{\natural}$, $\Box=\partial^2/\partial Q_t^2+\Delta$ | Gradient, its natural conjugate, and the scalar d'Alembertian |
| $\tilde\nabla\psi_R=m\psi_L$, $\tilde\nabla^{\natural}\psi_L=m\psi_R$ | The one-sided Dirac pair, one equation per chirality |
| $L_aR_b\psi=a\psi b$, $G_\mu=iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}$, $\nu(t)=x$, $\nu(k)=y$ | Two-sided cells and the generator cells |
| $\mathbb{D}=-R_{\vec e_x}^{\mathrm{axf}}\partial/\partial x_0-\sum_kL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\partial/\partial x_k$, $\mathbb{D}^2=\Box$ | Two-sided cell Dirac operator; $(\mathbb{D}-m)\psi=0$ |
| $\chi=-iR_{\vec e_z}^{\mathrm{axf}}$ | Chirality cell on the module, $\chi^2=I_4$, eigenvalues $\pm1$ |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- H. J. Bhabha, "Relativistic wave equations for the elementary particles," *Reviews of Modern Physics* **17** (1945) 200–216, for the finite-dimensional relativistic wave equations and their multi-mass spectra.
- I. M. Gel'fand and A. M. Yaglom, "General relativistic-invariant equations with a mass spectrum," *Zhurnal Eksperimentalnoi i Teoreticheskoi Fiziki* **18** (1948) 703–733, for the general theory of the equations with a mass spectrum.
- E. Majorana, "Teoria relativistica di particelle con momento intrinseco arbitrario," *Nuovo Cimento* **9** (1932) 335–344, for the infinite-component equation.
- I. M. Gel'fand, R. A. Minlos and Z. Ya. Shapiro, *Representations of the Rotation and Lorentz Groups and Their Applications* (Pergamon, 1963), for the representations, the spintensors and the interlocking schemes.
- R. Penrose and W. Rindler, *Spinors and Space-Time*, vol. 1 (Cambridge, 1984), for the van der Waerden two-spinor formalism by which a Minkowski vector is a pair of conjugate spinors.
- A. Z. Petrov, *Einstein Spaces* (Pergamon, 1969), for the mapping of the curvature tensor into $\mathbb{R}^6$ and the classification of Einstein spaces.
- V. V. Varlamov, "Spinor Structure and Internal Symmetries," *International Journal of Theoretical Physics* **54** (2015) 3533–3576 (arXiv:1409.1400), for the wave equations, the chains and the bivector-space reduction recorded here.
- Companion articles: [The Spin–Mass Formula and the Spectrum of Elementary Particles in Biquaternionic Form](the-spin-mass-formula-and-the-spectrum-of-elementary-particles-in-biquaternionic-form.html); [The Spin–Charge Hilbert Space and the SU(3) Supermultiplets in Biquaternionic Form](the-spin-charge-hilbert-space-and-the-su3-supermultiplets-in-biquaternionic-form.html); [Bhabha Scattering in Biquaternionic Form](bhabha-scattering-in-biquaternionic-form.html); [The Field-Strength Biquaternion and Its Invariants](the-field-strength-biquaternion-and-its-invariants.html); [The Dirac–Hestenes Equation and Spacetime Algebra in Biquaternionic Form](the-dirac-hestenes-equation-and-spacetime-algebra-in-biquaternionic-form.html); [Bispinor Fields and the Fundamental Solution of the Generalized Maxwell–Dirac Equation](bispinor-fields-and-the-fundamental-solution-of-the-generalized-maxwell-dirac-equation.html).
