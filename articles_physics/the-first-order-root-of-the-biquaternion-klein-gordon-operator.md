# __The First-Order Root of the Biquaternion Klein–Gordon Operator__

## Introduction

The biquaternion Klein–Gordon operator has a first-order root, but it has no single one. Squaring a first-order operator to the central scalar $\Box-\mu^2$ needs four mutually anticommuting generators with $(iR_{\vec e_x}^{\mathrm{axf}})^2=+1$ and $(iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}})^2=-1$, the Lorentz signature; the biquaternion algebra supplies the three spatial ones, and the fourth needs a second factor. That factor doubles the minimal module to four complex dimensions. Write $iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}$ for the four generators and $-iR_{\vec e_z}^{\mathrm{axf}}$ for their chirality, the cell that anticommutes with all four. With a pseudoscalar mass the single square exists; with the physical scalar mass only a factorisation exists, and the physical equation is one factor of it. The root therefore lives in the two-sided algebra $\mathbb{B}\otimes\mathbb{B}^{\mathrm{opp}}\cong M_4(\mathbb{C})$, while $\Box$ itself remains central.

Here $iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}$ is the generator cell of the coordinate $x_\mu$, with $\nu(t)=x$ and $\nu(k)=y$.

The equation is

$$
\left(\Box-\mu^2\right)\tilde\Phi=0,
\qquad
\mu=\frac{mc}{\hbar}.
$$

The companion *The Klein–Gordon Equation in Biquaternionic Form* records that the operator is central and scalar, that the equation decouples into four scalar equations, and that no scalar first-order operator in $\mathbb{B}$ has it as its square. The companion *Klein–Gordon from the Dirac Square in Biquaternionic Form* records the other side: a first-order equation exists, but it is spinor-valued and its mass couples two chiral halves. Together they leave Open Question 3 of the Klein–Gordon article: is the spinor root the only first-orderisation, and why four components?

There are two inequivalent senses of "first-order root", and the article treats both. A **single square** is one operator $D$ with $D^2=(\Box-\mu^2)I$. A **factorisation** is a product $D_-D_+=(\Box-\mu^2)I$ of two first-order factors; the physical equation is one factor, and the product is the Klein–Gordon operator. The single square is the stronger notion, and the physical mass does not admit it. The factorisation is the weaker notion, and the physical mass requires it.

The two notions give two first-order equations, and the article keeps them apart. Write $\mathsf D$ for the derivative part in the Lorentz frame, defined in §*The ansatz*; the single square is

$$
\mathsf D_{\mathrm{ps},\pm}=\mathsf D\pm\mu R_{\vec e_z}^{\mathrm{axf}},
\qquad
\mathsf D_{\mathrm{ps},\pm}^2=\left(\Box-\mu^2\right)I ,
$$

with a pseudoscalar mass, and the factorisation is

$$
\mathsf D_{\mathrm{sc},\pm}=\mathsf D\pm\mu I,
\qquad
\mathsf D_{\mathrm{sc},-}\mathsf D_{\mathrm{sc},+}
=\left(\Box-\mu^2\right)I ,
$$

with a scalar mass. The first is the Dirac equation read in the two-sided operator algebra; the second is the corpus's chiral pair, written in the cell frame and with both factors kept. They are different equations, not two spellings of one, and the physical mass selects the second.

Three results:

- **The root acts on four complex components.** The derivative part $\mathsf D$ of a first-order operator $\mathsf D+B$ squares to the scalar $\Box I$ exactly when the four cells $iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}$ mutually anticommute, with $(iR_{\vec e_x}^{\mathrm{axf}})^2=+1$ and $(iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}})^2=-1$. They generate $\mathrm{Cl}_{1,3}(\mathbb{C})\cong M_4(\mathbb{C})$, whose smallest module is $\mathbb{C}^4$, of real dimension eight.
- **The algebra supplies three of the four.** The three $\vec e_k$ supply the spatial Clifford system inside $\mathbb{B}$. No fourth element of $\mathbb{B}$ anticommutes with all three, so the fourth acts on a second factor. In the regular picture that factor is the right copy $\mathbb{B}_R$, and the root lives in $\mathbb{B}\otimes\mathbb{B}^{\mathrm{opp}}$.
- **The mass term is constrained.** The condition $\{B,iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}\}=0$ leaves $B$ one-dimensional, along the chirality cell: $B=c\,(-iR_{\vec e_z}^{\mathrm{axf}})$ with $c=\pm i\mu$, that is, $B=\pm\mu R_{\vec e_z}^{\mathrm{axf}}$. A single operator exists only with a **pseudoscalar** mass. A **scalar** mass commutes with the generators, so it admits only the factorisation, and the physical first-order equation is one factor.

The Clifford classification is standard. The identification of its generators with cells of the two-sided algebra is the corpus's dictionary, and the mass dichotomy read as the reason for the chiral pair is the synthesis offered here. Nothing in the article predicts a mass or a coupling.

### The d'Alembertian

The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_t=1,\vec e_x,\vec e_y,\vec e_z$, $\vec e_k^2=-e_t$, and central imaginary $i$. The coordinates are $Q_\mu$, with $Q_t=ict'$ on the material sector. The gradient is $\tilde\nabla=\sum_\mu e_\mu\partial/\partial Q_\mu$, and the d'Alembertian is the single one of the series,

$$
\Box=\langle\tilde\nabla\rangle_{\natural}
=\mathrm{Sc}\left(\tilde\nabla^{\natural}\tilde\nabla\right)
=\frac{\partial^2}{\partial Q_t^2}+\Delta_Q
=\Delta_Q-c^{-2}\frac{\partial^2}{\partial t'^2}
\quad\text{on }\mathbb{M}_- .
$$

In the $x$ coordinates $x_0=ct'$, $x_k$, where $Q_t=ix_0$ and $Q_k=x_k$, the same operator is
$$
\Box=-\sum_{\mu,\nu}g_{\mu\nu}\frac{\partial^2}{\partial x_\mu\partial x_\nu}
=-\frac{1}{c^2}\frac{\partial^2}{\partial t'^2}+\Delta ,
\qquad
g=\mathrm{diag}(+1,-1,-1,-1).
$$
The $Q$ form is the Euclidean transcription, obtained by $\partial/\partial Q_t=-ic^{-1}\partial/\partial t'$.

Throughout, $c=1/\sqrt{\epsilon\mu}$ is the speed of light in the medium, and $\hbar$ is the reduced Planck constant. The $\mu$ of that formula is the permeability of the medium; the mass parameter $\mu=mc/\hbar$ is a different quantity, and the letter is overloaded in the corpus.

## The Operator and Its Symbol

### The norm of the gradient

The d'Alembertian is central: it is a multiple of the identity as an operator, and it acts coefficient by coefficient,

$$
\Box\tilde Q_{\mathrm f}=\sum_\mu\left(\Box Q_{\mathrm f,\mu}\right)e_\mu .
$$

The gradient itself does not have this property. Its square is

$$
\tilde\nabla^2=\left(\frac{\partial^2}{\partial Q_t^2}-\Delta_Q\right)e_t+2\frac{\partial}{\partial Q_t}\vec\nabla,
$$

with a vector remainder. The scalar part of this square is $\partial^2/\partial Q_t^2-\Delta_Q$, not $\Box$; the norm is the scalar part of the conjugate product, $\tilde\nabla\tilde\nabla^\natural=\Box e_t$, where the conjugation flips the sign of the spatial part. The first-order root is therefore not $\tilde\nabla$ itself: the gradient is a first-order operator whose square is not central, while the root is a first-order operator whose square is central, a multiple of the identity. The root is a different object, and it is matrix-valued.

### The symbol and the mass shell

On a plane wave the gradient acts as left multiplication by the symbol $\tilde K_{\mathrm s}$. The sign of the exponential is immaterial below, because every condition is quadratic in the symbol. The corpus four-wavevector is $\tilde K=i\omega/c\,e_t+\vec k$, and the symbol is its $i$ multiple,

$$
\tilde K=\frac{\tilde P}{\hbar}=\frac{i\omega}{c}e_t+\vec k,
\qquad
\tilde K_{\mathrm s}=i\tilde K=\frac{i\tilde P}{\hbar}=-\frac{\omega}{c}e_t+i\vec k ,
\qquad
\tilde K_{\mathrm s}=K_te_t+K_x\vec e_x+K_y\vec e_y+K_z\vec e_z .
$$

The norm of the symbol is the symbol of the d'Alembertian,

$$
\Box\;\longmapsto\;\langle\tilde K_{\mathrm s}\rangle_{\natural}
=\tilde K_{\mathrm s}\tilde K_{\mathrm s}^{\natural}
=\frac{\omega^2}{c^2}-|\vec k|^2 ,
$$

and the mass shell is the level set

$$
\langle\tilde K_{\mathrm s}\rangle_{\natural}=\mu^2
\quad\Longleftrightarrow\quad
\frac{\omega^2}{c^2}-|\vec k|^2=\frac{m^2c^2}{\hbar^2}
\quad\Longleftrightarrow\quad
E^2=\vec p^{\,2}c^2+m^2c^4 .
$$

Equivalently, on the shell $\langle\tilde K\rangle_{\natural}=-\mu^2$ and $\langle\tilde P\rangle_{\natural}=-m^2c^2$, with $\tilde P=iE/c\,e_t+\vec p$. The operator and its on-shell condition are the same norm, evaluated on the gradient and on the four-momentum. This is the structural fact that the rest of the article uses.

In the $x$ coordinates the four-wavevector has components $k_\mu=(\omega/c,\vec k)$. The spatial sign is carried by the frame, since $(iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}})^2=-I_4$, and not by a raised label. On the plane wave $e^{-ik_0x_0+i\vec k\cdot\vec x}$ the derivative part $\mathsf D$ has symbol $iR_{\vec e_x}^{\mathrm{axf}}k_{0}-\sum_k iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}k_{k}$, whose square is $\sum_{\mu,\nu}g_{\mu\nu}k_\mu k_\nu I=(\omega^2/c^2-|\vec k|^2)I$, the symbol of $\Box$.

A first-order operator with symbol $iR_{\vec e_x}^{\mathrm{axf}}k_{0}-\sum_k iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}k_{k}+B$ is singular exactly when its determinant vanishes. If its square is $(\langle\tilde K_{\mathrm s}\rangle_{\natural}-\mu^2)I$, the determinant vanishes exactly on the mass shell, so the first-order equation has nonzero plane-wave solutions exactly where the Klein–Gordon equation does.

## The Root Condition

### The ansatz

Let

$$
D=\mathsf D+B,
\qquad
\mathsf D=i\sum_\mu\Bigl(iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}\Bigr)\frac{\partial}{\partial x_\mu},
$$

with the cells $iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}$ and the zero-order matrix $B$ constant in $M_n(\mathbb{C})$. Written out in the Lorentz frame,

$$
\mathsf D=i\Bigl(iR_{\vec e_x}^{\mathrm{axf}}\Bigr)\frac{1}{c}\frac{\partial}{\partial t'}
+i\sum_k\Bigl(iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\Bigr)\frac{\partial}{\partial x_k}.
$$

Two imaginary units stand side by side in each term: the inner $i$ belongs to the generator cell, the outer one to the operator. Their product is $i^2=-1$, so the same operator reads

$$
\mathsf D=-R_{\vec e_x}^{\mathrm{axf}}\frac{1}{c}\frac{\partial}{\partial t'}
-\sum_k L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\frac{\partial}{\partial x_k},
$$

whose coefficients square to $(-1,+1,+1,+1)$. The cell form is kept because it is the one whose Clifford relations are $2g_{\mu\nu}$; the minus sign is carried by the metric there, and is not a separate convention.

This is the form in which the root condition is solved, not the most general first-order operator: a general constant-coefficient operator $\sum_\mu A_\mu\partial/\partial x_\mu+B$ whose square is $(\Box-\mu^2)I$ has $\{A_\mu,A_\nu\}=2g_{\mu\nu}I$, so its $A_\mu$ form a Clifford system conjugate to the frame cells, and $\mathsf D$ is the representative of that class. The coefficients are constant because the classification below is a classification of the algebraic form; position-dependent coefficients are a separate problem, taken up in §*What the Root Does Not Carry*.

### The expansion

Because the partial derivatives commute, only the symmetric part of the quadratic term survives: the antisymmetric part of $iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}\,iL_{e_\nu}^{\mathrm{axf}}R_{\vec e_{\nu(\nu)}}^{\mathrm{axf}}$ multiplies the symmetric $\partial^2/\partial x_\mu\partial x_\nu$ and drops out, leaving the anticommutator. Hence

$$
D^2
=-\tfrac12\{iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}},iL_{e_\nu}^{\mathrm{axf}}R_{\vec e_{\nu(\nu)}}^{\mathrm{axf}}\}\frac{\partial^2}{\partial x_\mu\partial x_\nu}
+i\{iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}},B\}\frac{\partial}{\partial x_\mu}
+B^2 .
$$

This is an identity for every choice of the cells and of $B$; it assumes nothing about them. Requiring

$$
D^2=\left(\Box-\mu^2\right)I_n
=-\sum_{\mu,\nu}g_{\mu\nu}\frac{\partial^2}{\partial x_\mu\partial x_\nu}-\mu^2I_n
$$

and matching the three monomials gives three conditions:

$$
\{iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}},iL_{e_\nu}^{\mathrm{axf}}R_{\vec e_{\nu(\nu)}}^{\mathrm{axf}}\}=2g_{\mu\nu}I_n,
\qquad
\{iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}},B\}=0,
\qquad
B^2=-\mu^2I_n .
$$

The first is the Clifford relation on the derivative part: the four cells $iR_{\vec e_x}^{\mathrm{axf}}$ and $iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ carry the Clifford relations of $g=\operatorname{diag}(+1,-1,-1,-1)$, with $2g_{00}=+2$ and $2g_{kk}=-2$. The second says the mass must anticommute with every generator. The third fixes the magnitude of the mass. The three are independent: the first is about the derivative part, the second about the mixing of the derivative and the mass, the third about the mass alone.

The signs are those of $\Box$ in the $x$ coordinates, where the metric is $g=\mathrm{diag}(+1,-1,-1,-1)$. The $Q$ coordinates carry the Euclidean transcription, in which all four generators square to $+1$ and the spatial ones acquire a factor $i$; that frame is not used here.

## Four Generators

### The Clifford algebra

Four generators with $\{iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}},iL_{e_\nu}^{\mathrm{axf}}R_{\vec e_{\nu(\nu)}}^{\mathrm{axf}}\}=2g_{\mu\nu}I_4$ generate the complex Clifford algebra $\mathrm{Cl}_{1,3}(\mathbb{C})\cong M_4(\mathbb{C})$. The algebra is simple, so every nonzero representation is faithful, and its smallest module is $\mathbb{C}^4$. A representation on $\mathbb{C}^2$ would be a two-dimensional module for $M_4(\mathbb{C})$, which does not exist. Hence

$$
n\ge 4,
$$

and $n=4$ is both minimal and realised. The real dimension of the minimal module is eight, the same as the real dimension of $\mathbb{B}$.

The counting can be seen without naming the algebra. Four anticommuting matrices in $M_n(\mathbb{C})$ generate, together with their products, $16$ linearly independent matrices: the identity, the four generators, the six products $iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}\,iL_{e_\nu}^{\mathrm{axf}}R_{\vec e_{\nu(\nu)}}^{\mathrm{axf}}$ with $\mu<\nu$, the four products $iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}\,(-iR_{\vec e_z}^{\mathrm{axf}})$, and $-iR_{\vec e_z}^{\mathrm{axf}}$. Sixteen independent matrices require $n^2\ge16$, hence $n\ge4$. The bound is attained by the frame of five cells below.

The minimal realisation is explicit, and it uses both sides of the algebra. With $L_{a}R_{b}$,

$$
iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}},
\qquad
iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},
\qquad
iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},
\qquad
iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},
\qquad
-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}},
$$

and the split of each cell between the two sides is

| $T$ | $L$ | $R$ |
|---|---|---|
| $iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}$ | $L_{e_t}^{\mathrm{axf}}=I$ | $R_{\vec e_x}^{\mathrm{axf}}$ |
| $iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ | $iL_{\vec e_k}^{\mathrm{axf}}$ | $R_{\vec e_y}^{\mathrm{axf}}$ |
| $-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ | $L_{e_t}^{\mathrm{axf}}=I$ | $-iR_{\vec e_z}^{\mathrm{axf}}$ |

The fourth generator has $L=I$: it is a pure right multiplication, which is why the biquaternion algebra alone does not contain it. The three space generators have both factors. The split is what the next two subsections use: the three space generators carry a left factor from $\mathbb{B}$, the fourth carries only a right factor.

The five cells are the four generators and the chirality. The product of the four generators is

$$
\Bigl(iR_{\vec e_x}^{\mathrm{axf}}\Bigr)\Bigl(iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\Bigr)
\Bigl(iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\Bigr)\Bigl(iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\Bigr)
=-R_{\vec e_z}^{\mathrm{axf}},
$$

which squares to $-I_4$ and is $-i$ times the chirality. The chirality cell is the $i$ multiple, $-iR_{\vec e_z}^{\mathrm{axf}}$, which squares to $+I_4$ and anticommutes with all four generators. Since $-iR_{\vec e_z}^{\mathrm{axf}}$ is $-i$ times the right multiplication, the product is $(-i)(-iR_{\vec e_z}^{\mathrm{axf}})=-R_{\vec e_z}^{\mathrm{axf}}$: the two differ by the factor $-i$, and $(-i)(-i)=-1$ is the whole difference. The corpus calls $-iR_{\vec e_z}^{\mathrm{axf}}$ the volume element. The mass of the single square is built on the chirality, which squares to $+I_4$, and not on the product, which squares to $-I_4$; that sign is the reason the mass uses the first.

### Three inside the biquaternions

The biquaternion algebra contains three mutually anticommuting generators of square $-1$:

$$
\vec e_k^2=-e_t,
\qquad
\{\vec e_j,\vec e_k\}=0,\quad j\neq k .
$$

They act by left multiplication on a minimal left ideal $S\cong\mathbb{C}^2$, and their images are $-i$ times the Pauli matrices,

$$
\mathsf M_2(\vec e_x)=-i\sigma_1,
\qquad
\mathsf M_2(\vec e_y)=-i\sigma_2,
\qquad
\mathsf M_2(\vec e_z)=-i\sigma_3 .
$$

So $\mathbb{B}$ supplies three of the four generators, and the module $S$ is two-dimensional.

No fourth element of $\mathbb{B}$ anticommutes with all three. Write a general element as $X=a_te_t+a_x\vec e_x+a_y\vec e_y+a_z\vec e_z$ with $a_\mu\in\mathbb{C}$. The anticommutator with $\vec e_x$ is

$$
\{X,\vec e_x\}=2a_t\vec e_x-2a_x e_t=0,
$$

which forces $a_t=a_x=0$. Anticommuting with $\vec e_y$ then forces $a_y=0$, leaving $X=a_z\vec e_z$. But this commutes with the third generator, so it does not anticommute with it. The only solution is $X=0$.

This is the coefficient proof of the Klein–Gordon article, read as a statement about the fourth generator. The obstruction is not that the algebra lacks room for a fourth direction; it is that the fourth direction cannot be a left multiplication.

### The fourth direction is the second side

The fourth generator acts on a second factor. The minimal module is

$$
\mathbb{C}^4\cong\mathbb{C}^2_{\mathrm{mult}}\otimes S,
$$

with $\mathbb{C}^2_{\mathrm{mult}}$ the multiplicity factor and $S$ the biquaternion spinor module. The tensor frame is the image of the cell frame, not a second frame: a cell maps to a Kronecker product of its two multipliers,

$$
L_{a}R_{b}\;\longmapsto\;\mathsf M_2(b)^{\mathsf T}\otimes\mathsf M_2(a),
$$

so the cell form is the primary one and the tensor form is its transcription. On the four frame cells the dictionary gives

$$
iR_{\vec e_x}^{\mathrm{axf}}=\sigma_1\otimes I_2,
\qquad
iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}=i\sigma_2\otimes\sigma_k,
\qquad
-iR_{\vec e_z}^{\mathrm{axf}}=-\sigma_3\otimes I_2 .
$$

The first acts on the multiplicity factor alone and as the identity on $S$; the three space generators act on $S$ by $\sigma_k=\mathsf M_2(i\vec e_k)$, dressed by $i\sigma_2$ on the multiplicity, so their product squares to $-1$. The multiplicity factor is what $\mathbb{B}$ alone does not supply. Adjoining it is the passage to the two-sided algebra.

The cell form exhibits the same fact. The fourth generator is

$$
iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}=R_{i\vec e_x}^{\mathrm{axf}},
$$

a right multiplication, and it commutes with every left multiplication, so it lies in the commutant $\mathbb{B}_R$ of the left copy $\mathbb{B}_L$. A right multiplication is invisible to $\mathbb{B}_L$; this is the precise sense in which the fourth direction is the second side. The algebra generated by $\mathbb{B}_L$ and $\mathbb{B}_R$ is

$$
\mathbb{B}\otimes\mathbb{B}^{\mathrm{opp}}\cong M_2(\mathbb{C})\otimes M_2(\mathbb{C})\cong M_4(\mathbb{C}).
$$

The three space generators are cells that use both sides, $iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$, and the anticommutator with $iR_{\vec e_x}^{\mathrm{axf}}$ comes from the right factors, $R_{\vec e_y}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}=-R_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$.

The real dimension count is consistent. The module $\mathbb{C}^4$ has real dimension eight, the same as $\mathbb{B}$. The root does not enlarge the field space relative to a biquaternion field; it changes the module structure. Relative to a single complex scalar, of course, it is a fourfold complex enlargement.

## The Mass Condition and the Two Masses

### The condition

The second root condition is

$$
\{B,iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}\}=0\quad\text{for all }\mu .
$$

The anticommutant of the four generators is one-dimensional, and it is spanned by the chirality cell, which anticommutes with all four. If $B$ anticommutes with every generator $\Gamma=iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}$, then $B(-iR_{\vec e_z}^{\mathrm{axf}})$ commutes with $\Gamma$: each factor changes sign and the two signs cancel. The four generate $M_4(\mathbb{C})$, whose commutant is $\mathbb{C}I_4$, so $B(-iR_{\vec e_z}^{\mathrm{axf}})=cI_4$. The chirality cell is its own inverse, $(-iR_{\vec e_z}^{\mathrm{axf}})^2=I_4$, so

$$
B=c\,(-iR_{\vec e_z}^{\mathrm{axf}})=-ic\,R_{\vec e_z}^{\mathrm{axf}}.
$$

The third condition then gives

$$
B^2=c^2\,(-iR_{\vec e_z}^{\mathrm{axf}})^{2}=c^2I_4=-\mu^2I_4,
\qquad
c=\pm i\mu .
$$

The factor $-i$ of the chirality cell and $c=\pm i\mu$ combine, $(-i)(\pm i\mu)=\pm\mu$, so the mass term carries no imaginary unit at all:

$$
B=\pm\mu R_{\vec e_z}^{\mathrm{axf}}.
$$

So the single-square roots are

$$
\mathsf D_{\mathrm{ps},\pm}=\mathsf D\pm\mu R_{\vec e_z}^{\mathrm{axf}},
\qquad
\mathsf D_{\mathrm{ps},\pm}^2=\left(\Box-\mu^2\right)I_4 ,
$$

with $\mathsf D$ the derivative part of §*The ansatz*.

The mass term is proportional to $R_{\vec e_z}^{\mathrm{axf}}$, which is $i$ times the chirality cell $-iR_{\vec e_z}^{\mathrm{axf}}$. It is a **pseudoscalar** mass.

### The single square

The pseudoscalar mass is not an accident of the construction. It is the only mass that anticommutes with all four generators. In the basis where $-iR_{\vec e_z}^{\mathrm{axf}}$ is diagonal, the term $\mu R_{\vec e_z}^{\mathrm{axf}}$ is diagonal: it takes opposite values on the two chiralities, and it does not mix them.

The invariant statement is the anticommutator, not the matrix shape. The scalar mass commutes with $\mathsf D$; the pseudoscalar mass anticommutes with it. No change of frame alters which of the two holds, because the two conditions are statements about the algebra and not about a basis.

The corpus knows this channel. It is the $\chi$-type coupling of *The Dirac Equation in Biquaternionic Form*, the pseudoscalar potential that multiplies the central imaginary $i$ and is the $-iR_{\vec e_z}^{\mathrm{axf}}$-type in the matrix dictionary. The single first-order root is therefore not new machinery; it is the corpus's pseudoscalar channel read as a mass.

The sign is fixed by the conventions:

$$
-iR_{\vec e_z}^{\mathrm{axf}}=\rho(\chi),
$$

so the pseudoscalar mass reads $\mu R_{\vec e_z}^{\mathrm{axf}}=i\mu(-iR_{\vec e_z}^{\mathrm{axf}})\leftrightarrow i\mu\chi$ in the biquaternion dictionary; here $i\cdot(-i)=-i^2=+1$ is what cancels the two imaginary units. The chirality is the cell $\gamma_5=-iR_{\vec e_z}^{\mathrm{axf}}$; the central element $\chi$ is its central form, and the cell $-iR_{\vec e_z}^{\mathrm{axf}}=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ is its representative in the reference frame.

The term is parity-odd. A parity-odd mass is not the mass of the Dirac equation, and it is not the mass the Standard Model generates. The single root exists, but it is not the physical one.

### The scalar mass and the factorisation

The physical mass is a scalar: it multiplies the identity and commutes with every generator. It fails the second condition,

$$
\{\mu I,iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}\}=2\mu\,iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}\neq0,
$$

so no single operator of the form $\mathsf D+B$ with a scalar mass squares to the Klein–Gordon operator. Each factor alone carries a first-order remainder:

$$
\mathsf D_{\mathrm{sc},\pm}=\mathsf D\pm\mu I,
\qquad
\mathsf D_{\mathrm{sc},\pm}^2=\left(\Box+\mu^2\right)I\pm2\mu\mathsf D .
$$

The cross term is the price of the scalar mass. It cancels in the product:

$$
\mathsf D_{\mathrm{sc},-}\mathsf D_{\mathrm{sc},+}
=\left(\mathsf D-\mu I\right)\left(\mathsf D+\mu I\right)
=\left(\Box-\mu^2\right)I .
$$

The physical first-order equation is one factor, $\mathsf D_{\mathrm{sc},-}\psi=0$ or $\mathsf D_{\mathrm{sc},+}\psi=0$; the other factor carries the opposite mass. The product is the Klein–Gordon operator, so each factor implies Klein–Gordon without squaring to it. This is the precise sense in which the scalar mass needs a pair: not two independent equations, but a factorisation whose two factors carry opposite mass. The algebraic content of the chiral pair of the corpus is the same factorisation,

$$
\tilde\nabla\tilde\Psi_R=\mu\tilde\Psi_L,
\qquad
\tilde\nabla^{\natural}\tilde\Psi_L=\mu\tilde\Psi_R,
$$

with the same $\mu$ as above, which the companion writes as $m$ in natural units. Substituting the first into the second and using $\tilde\nabla^{\natural}\tilde\nabla=\Box$ gives $\Box\tilde\Psi_R=\mu^2\tilde\Psi_R$, so each half satisfies Klein–Gordon. The pair is the scalar-mass case written in the biquaternion chiral basis, not a second, independent root.

The dichotomy is therefore sharp:

- a **pseudoscalar** mass anticommutes with the generators and admits a single first-order operator whose square is Klein–Gordon;
- a **scalar** mass commutes with the generators and admits only the factorisation, whose physical factor is the Dirac equation.

The physical mass is the second. The corpus's use of the chiral pair is not an arbitrary choice of basis; it is the biquaternion form of the factorisation forced by the scalar mass.

### The scalar field has no root

A central scalar field has a one-dimensional module. Four nonzero scalars commute, so they cannot satisfy the Clifford relation. Equivalently, a one-dimensional module cannot carry $M_4(\mathbb{C})$. The Klein–Gordon field itself, taken as a central scalar, therefore has no first-order root. A first-order root requires promoting the field to the Clifford module. This is the no-go of the Klein–Gordon article, recovered as a module-dimension statement. The three cases are collected in the table.

| Field | Module | Mass term | Equation | Single square? |
|---|---|---|---|---|
| Central scalar | $\mathbb{C}$ | — | none | no |
| Pseudoscalar-mass spinor | $\mathbb{C}^4$ | $\mu R_{\vec e_z}^{\mathrm{axf}}$ | $\mathsf D_{\mathrm{ps},\pm}\psi=0$ | yes, $\mathsf D_{\mathrm{ps},\pm}^2=(\Box-\mu^2)I_4$ |
| Scalar-mass spinor | $\mathbb{C}^4$ | $\mu I$ | $\mathsf D_{\mathrm{sc},\pm}\psi=0$ (chiral pair) | no, $\mathsf D_{\mathrm{sc},-}\mathsf D_{\mathrm{sc},+}=(\Box-\mu^2)I_4$ |

### The determinant face

The corpus records two determinant identities for the gradient:

$$
\det A_+(\tilde\nabla)=\Box,
\qquad
\det\mathsf M_4^L(\tilde\nabla)=\Box^2,
$$

where $A_+(\tilde\nabla)$ is the chiral block of the left regular matrix. These are identities of the **even** face: a second-order scalar operator is the determinant of a first-order matrix. They are not a square root in the matrix sense. The determinant is a product of eigenvalues; a massless root is a single operator $D$ with

$$
D^2=\Box\,I .
$$

The two questions are different. The determinant identity says that the scalar wave operator is the determinant of a first-order matrix; the root asks for one first-order operator whose square is the scalar operator. The massless root has $\det\mathsf D=\Box^2$, the same determinant as the left regular matrix of the gradient. The massive root has

$$
\det\mathsf D_{\mathrm{ps},\pm}=\left(\Box-\mu^2\right)^2,
$$

which reduces to $\Box^2$ at $\mu=0$. The determinant depends on $\mu$ only through $\mu^2$, so the two signs in $B=\pm\mu R_{\vec e_z}^{\mathrm{axf}}$ give the same value. This is a consistency check on the classification, not a construction of the root.

## What the Root Does Not Carry

The classification is a statement of form, and its boundaries are part of the result.

1. **It is stronger than Klein–Gordon.** A first-order equation selects a subspace of the second-order solution space. The single root and the Dirac factor select different subspaces, and neither is equivalent to the second-order equation. For a fixed momentum on the shell the second-order equation allows all four polarisations, while a first-order equation allows two; both retain the two frequency branches, so what the root halves is the polarisation space and not the spectrum. At $\mu=0$ the single root reduces to $\mathsf D$, whose kernel is two-dimensional with one state of each chirality, while the scalar-mass factorisation reduces to $\mathsf D^2=\Box$; the massless limit does not select one channel.
2. **No mass, no coupling, and no sign is predicted.** The classification says which first-order structures have the Klein–Gordon square; it does not say which one nature uses, and it does not determine $\mu$. The sign of the mass is not physical either: $\mathsf D_{\mathrm{ps},+}$ and $\mathsf D_{\mathrm{ps},-}$ are exchanged by $\mu\to-\mu$, so only the relative sign of the mass and the chirality is meaningful. Whether a pseudoscalar mass is realised is a dynamical question that the classification leaves open; the corpus's $\chi$-type coupling suggests an axial channel but supplies no dynamics.
3. **The coefficients are constant and the background flat.** Position-dependent coefficients add commutator terms, and a gauged derivative adds a field strength; the Clifford structure is then deformed, and the constant-coefficient classification is the starting point rather than the answer. On a curved background the partial derivatives become covariant derivatives and the Clifford algebra is the tangent-space algebra; the dimension count is unchanged, but the spin connection enters the root. The $x$ coordinates are flat; the $Q$ form is the Euclidean transcription of the same operator, not a different root.
4. **The real structure and the index are open.** The article works over $\mathbb{C}$. The two real forms of the Lorentzian complex algebra are $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$ and $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$; the choice between them is the Majorana/Dirac question, and the charge-conjugation pairing is a real-structure question that this article does not settle. The massless root is odd under the chirality grading and $\Box$ is even, so the index of $\mathsf D$ is an invariant of the graded module; whether the biquaternion grading gives a nontrivial index on a gauge background is open.

## The Even and the Odd Face

The article's result can be stated as a division of labour between two matrix sizes.

- **The even face is $M_2$.** The Klein–Gordon operator is central; the determinant of the chiral block of the left regular matrix is $\Box$. The three generators $\vec e_k$ and the determinant identity live at the $M_2(\mathbb{C})$ level; the chiral pair is written in the biquaternion module before the fourth generator is adjoined.
- **The odd face is $M_4$.** The first-order structure — the single square $\mathsf D_{\mathrm{ps},\pm}$ or the Dirac factor of the scalar-mass case — needs the fourth generator, the multiplicity factor, and the two-sided algebra. For the single square, $\det\mathsf D_{\mathrm{ps},\pm}=(\Box-\mu^2)^2$, which reduces to $\Box^2$ at $\mu=0$ and matches the determinant of the left regular matrix of the gradient.

The division answers the $M_2$/$M_4$ question. The Klein–Gordon **equation** does not require $M_4$: its operator is central and its field can be a single complex scalar. The Klein–Gordon **root** does require $M_4$: the fourth Clifford direction is the second side of the algebra. The two statements are compatible because they are about different objects. The scalar equation lives in the centre; its first-order root lives in the two-sided algebra.

The regular representation's doubling is not a prediction of doubled particles. The two minimal left ideals are the two chiral copies of the same module; the doubling is the price of the fourth generator, not a doubling of the spectrum.

## Verification

The identities were recomputed before they were written. The cell frame was built from $L_{a}R_{b}$ as $4\times4$ complex matrices, and the tensor description from the Pauli matrices and the $2\times2$ images of $\vec e_k$. The residuals are the largest absolute entries over the stated samples; $K$ is a complex four-wavevector drawn from a fixed seed and $\mu$ a fixed real mass.

| Check | Result |
|---|---|
| $\{iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}},iL_{e_\nu}^{\mathrm{axf}}R_{\vec e_{\nu(\nu)}}^{\mathrm{axf}}\}-2g_{\mu\nu}I_4$ | $0$ (exact) |
| $(-iR_{\vec e_z}^{\mathrm{axf}})^{2}-I_4$ and $\{-iR_{\vec e_z}^{\mathrm{axf}},iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}\}$ | $0$ (exact) |
| $-iR_{\vec e_z}^{\mathrm{axf}}+R_{\vec e_x}^{\mathrm{axf}}\,iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\,iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\,iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ | $0$ (exact) |
| $\mathsf D+R_{\vec e_x}^{\mathrm{axf}}\partial/\partial x_0+\sum_k L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\partial/\partial x_k$ | $0$ (exact) |
| Tensor dictionary reproduces the five cells and satisfies the same Clifford relations | $0$ (exact) |
| Anticommutant of all four generators | rank $15$, nullity $1$ |
| $\{\mu R_{\vec e_z}^{\mathrm{axf}},iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}\}$ and $(\mu R_{\vec e_z}^{\mathrm{axf}})^2+\mu^2I_4$ | $0$ (exact) |
| $\mathsf D_{\mathrm{ps},+}^2-(\Box-\mu^2)I_4$ on $100$ random $K$ | $4.0\times10^{-15}$ |
| $\mathsf D_{\mathrm{sc},-}\mathsf D_{\mathrm{sc},+}-(\Box-\mu^2)I_4$ on $100$ random $K$ | $4.0\times10^{-15}$ |
| $\left(iR_{\vec e_x}^{\mathrm{axf}}k_{0}-\sum_k iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}k_{k}\right)^2-g_{\mu\nu}k_\mu k_\nu I_4$ on $100$ random $K$ | $4.0\times10^{-15}$ |
| $\det\mathsf D_{\mathrm{ps},\pm}-(\Box-\mu^2)^2$ on $100$ random $K$ | $3.8\times10^{-13}$ |
| $\det\mathsf D-\Box^2$ on $100$ random $K$ | $2.9\times10^{-13}$ |
| Frame squares $(+1,-1,-1,-1)$ and anticommutators | $0$ (exact) |

The numerical checks are checks of polynomial identities at random points. The proof is the algebra of the preceding sections; the numbers guard against a sign or factor error in the transcription.

## The Gamma Formulation

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra. The five are the frame cells written as matrices:
$$
\gamma_0=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\qquad
\gamma_1=iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\qquad
\gamma_2=iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\qquad
\gamma_3=iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\qquad
\gamma_5=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}.
$$

The same in the axis-free display:

$$
\gamma_0=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}},\qquad
\gamma_1=iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\qquad
\gamma_2=iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\qquad
\gamma_3=iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\qquad
\gamma_5=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}.
$$

They satisfy $\{\gamma_\mu,\gamma_\nu\}=2g_{\mu\nu}I_4$, $(\gamma_0)^2=+I_4$, $(\gamma_k)^2=-I_4$, $\{\gamma_\mu,\gamma_5\}=0$ and $\gamma_5=i\gamma_0\gamma_1\gamma_2\gamma_3$. The product of the first four is $\gamma_0\gamma_1\gamma_2\gamma_3=-R_{\vec e_z}^{\mathrm{pau}}$, and $i$ times it is $\gamma_5$; the corpus's volume element $-iR_{\vec e_z}^{\mathrm{pau}}$ is $\gamma_5$ itself.

In the tensor frame the same five are the images under $L_{a}R_{b}\mapsto\mathsf M_2(b)^{\mathsf T}\otimes\mathsf M_2(a)$,
$$
\gamma_0=\sigma_1\otimes I_2,\qquad
\gamma_k=i\sigma_2\otimes\sigma_k,\qquad
\gamma_5=-\sigma_3\otimes I_2,
$$
and the split between the two sides is the cell table of §*Four Generators*.

The root and the mass conditions read in gammas as
$$
\mathsf D=i\sum_\mu\gamma_\mu\frac{\partial}{\partial x_\mu}=i\gamma_\mu\frac{\partial}{\partial x_\mu},\qquad
\mathsf D_{\mathrm{ps},\pm}=\mathsf D\pm i\mu\gamma_5=\mathsf D\pm\mu R_{\vec e_z}^{\mathrm{pau}},\qquad
\mathsf D_{\mathrm{sc},\pm}=\mathsf D\pm\mu I,
$$

In the axis-free display:

$$
\mathsf D=i\sum_\mu\gamma_\mu\frac{\partial}{\partial x_\mu}=i\gamma_\mu\frac{\partial}{\partial x_\mu},\qquad
\mathsf D_{\mathrm{ps},\pm}=\mathsf D\pm i\mu\gamma_5=\mathsf D\pm\mu R_{\vec e_z}^{\mathrm{axf}},\qquad
\mathsf D_{\mathrm{sc},\pm}=\mathsf D\pm\mu I,
$$

The only single-square mass term is $B=c\gamma_5$ with $c=\pm i\mu$; the second equality for $\mathsf D_{\mathrm{ps},\pm}$ uses $i\gamma_5=R_{\vec e_z}^{\mathrm{pau}}$.

The checks of §*Verification*, transcribed into these symbols, are $\{\gamma_\mu,\gamma_\nu\}-2g_{\mu\nu}I_4$, $\gamma_5^2-I_4$, $\{\gamma_5,\gamma_\mu\}$, $\gamma_5-i\gamma_0\gamma_1\gamma_2\gamma_3$ and $(\sum_\mu \gamma_\mu k_\mu)^2-g_{\mu\nu}k_\mu k_\nu I_4$; the first and the last are polynomial identities in the symbol $k$, so they hold for every $k$, not only on shell.

**The identities the bodies cite.** In the $\gamma$ reading, with $\epsilon_{0123}=+1$,
$$
\{\gamma_\mu,\gamma_\nu\}=2g_{\mu\nu}I_4,\qquad
(\gamma_k)^2=-I_4,\qquad
\gamma_5^2=I_4,\qquad
\{\gamma_\mu,\gamma_5\}=0,
$$
$$
[\gamma_\mu,\gamma_\nu]=2\gamma_\mu\gamma_\nu\quad(\mu\ne\nu),\qquad
[\gamma_a,S_{cd}]=g_{ac}\gamma_d-g_{ad}\gamma_c,\qquad
S_{cd}=\tfrac14[\gamma_c,\gamma_d],
$$
$$
\mathrm{tr}(\gamma_\mu\gamma_\nu)=4g_{\mu\nu},\qquad
\mathrm{tr}(\gamma_5\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)=-4i\,\epsilon_{\mu\nu\rho\sigma},
$$
$$
\mathrm{tr}(\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)
=4\bigl(g_{\mu\nu}g_{\rho\sigma}-g_{\mu\rho}g_{\nu\sigma}+g_{\mu\sigma}g_{\nu\rho}\bigr).
$$
The four contraction sums hold in the Euclidean frame, where every generator squares to $+I_4$:
$$
\sum_\mu\gamma_\mu\gamma_\mu=4I_4,\qquad
\sum_\mu\gamma_\mu\gamma_\alpha\gamma_\mu=-2\gamma_\alpha,\qquad
\sum_\mu\gamma_\mu\gamma_\alpha\gamma_\beta\gamma_\mu=4\delta_{\alpha\beta}I_4,
$$
$$
\sum_\mu\gamma_\mu\gamma_\delta\gamma_\beta\gamma_\alpha\gamma_\mu
=\epsilon\,2\gamma_\delta\gamma_\beta\gamma_\alpha,
\qquad
\epsilon=\begin{cases}+1,&\alpha,\beta,\delta\ \text{all distinct},\\ -1,&\text{otherwise}.\end{cases}
$$
The sign of the last sum is the parity of the label pattern, not a convention: three distinct labels give $+2\gamma_\delta\gamma_\beta\gamma_\alpha$, and any repeated label gives $-2\gamma_\delta\gamma_\beta\gamma_\alpha$. All four sums were recomputed in the Euclidean frame, with zero residual for every label pattern. In the $\mathbb{M}_-$ frame the metric enters and $\sum_\mu\gamma_\mu\gamma_\mu=-2I_4$.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{e_\mu}^{\mathrm{axf}}=C_{\Pi}L_{e_\mu}^{\mathrm{pau}}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

The first-order root of the biquaternion Klein–Gordon operator exists, and its carrier is fixed by the Clifford relation. The root acts on a module of $\mathrm{Cl}_{1,3}(\mathbb{C})\cong M_4(\mathbb{C})$, whose minimal module is $\mathbb{C}^4$. The biquaternion algebra supplies the three spatial generators $\vec e_x,\vec e_y,\vec e_z$, and no fourth; the fourth (time) generator acts on the multiplicity factor and, in the regular picture, is the right multiplication $R_{i\vec e_x}^{\mathrm{axf}}$, which lies in the commutant $\mathbb{B}_R$. The root therefore lives in $\mathbb{B}\otimes\mathbb{B}^{\mathrm{opp}}\cong M_4(\mathbb{C})$, while the Klein–Gordon operator itself remains central.

The mass term is constrained by $\{B,iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}\}=0$. The anticommutant is spanned by the chirality cell, so the only single-operator solution is $B=\pm\mu R_{\vec e_z}^{\mathrm{axf}}$, a pseudoscalar mass. A scalar mass commutes with the generators, so no single operator with a scalar mass squares to Klein–Gordon; the scalar mass admits only the factorisation $\mathsf D_{\mathrm{sc},-}\mathsf D_{\mathrm{sc},+}$, which is the corpus's chiral pair. The physical mass is the scalar one, so the physical first-order equation is one factor of that factorisation.

The two equations are therefore distinct, and the article's notation keeps them so: $\mathsf D_{\mathrm{ps},\pm}\psi=0$ is the single square in the two-sided operator algebra, and $\mathsf D_{\mathrm{sc},\pm}\psi=0$ is the chiral pair. Only the second is physical.

The scalar Klein–Gordon field, taken as a central scalar, has no first-order root. The results are a classification of form: no mass, no coupling, and no dynamics are predicted. The open questions are the gauged, curved, position-dependent, and real-structure extensions.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_k^2=-e_t$ |
| $i$ | Central scalar imaginary, $i^2=-1$ |
| $Q_\mu$ | Algebra coordinates, $Q_t=ict'$ on $\mathbb{M}_-$ |
| $x_\mu$ | Lorentz coordinates, $x_0=ct'$, $x_k$ spatial |
| $g_{\mu\nu}$ | Lorentz metric, $\mathrm{diag}(+1,-1,-1,-1)$ |
| $\tilde\nabla=\sum_\mu e_\mu\partial/\partial Q_\mu$ | Biquaternionic gradient |
| $\Box=\langle\tilde\nabla\rangle_{\natural}=\partial^2/\partial Q_t^2+\Delta_Q=-\sum_{\mu,\nu}g_{\mu\nu}\partial^2/\partial x_\mu\partial x_\nu$ | d'Alembertian, series convention and Lorentz form |
| $c=1/\sqrt{\epsilon\mu}$ | Speed of light in the medium; the $\mu$ here is the permeability |
| $\mu=mc/\hbar$ | Mass parameter (inverse reduced Compton wavelength) |
| $\tilde P=iE/c\,e_t+\vec p$ | Material four-momentum |
| $\tilde K=\tilde P/\hbar=i\omega/c\,e_t+\vec k$ | Corpus four-wavevector |
| $\tilde K_{\mathrm s}=i\tilde K$ | Symbol of the gradient; $K_\mu$ its components |
| $\langle\tilde K_{\mathrm s}\rangle_{\natural}=\mu^2$ | Mass shell |
| $iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}$ | Generator cells of the root, $\{iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}},iL_{e_\nu}^{\mathrm{axf}}R_{\vec e_{\nu(\nu)}}^{\mathrm{axf}}\}=2g_{\mu\nu}I_4$ |
| $\nu(\mu)$ | Index map of the generators, $\nu(t)=x$ and $\nu(k)=y$ |
| $-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}=-iR_{\vec e_z}^{\mathrm{axf}}$ | Chirality cell, $-iR_{\vec e_z}^{\mathrm{axf}}=\rho(\chi)$ |
| $-R_{\vec e_z}^{\mathrm{axf}}=iR_{\vec e_x}^{\mathrm{axf}}\,iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\,iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\,iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ | Product of the four generators, $-i$ times the chirality cell |
| $\mathsf D=i\sum_\mu\bigl(iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}\bigr)\partial/\partial x_\mu$ | Lorentz-frame Dirac operator, $\mathsf D^2=\Box I_4$ |
| $iR_{\vec e_x}^{\mathrm{axf}}k_{0}-\sum_k iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}k_{k}$ | Symbol of $\mathsf D$ on a plane wave, $k_\mu=(\omega/c,\vec k)$ |
| $\mathsf D_{\mathrm{ps},\pm}=\mathsf D\pm\mu R_{\vec e_z}^{\mathrm{axf}}$ | Single-square roots (pseudoscalar mass) |
| $\mathsf D_{\mathrm{sc},\pm}=\mathsf D\pm\mu I$ | Scalar-mass factors (chiral pair) |
| $S\cong\mathbb{C}^2$ | Minimal left ideal (biquaternion spinor module) |
| $L_a,R_b$ | Left and right multiplication operators |
| $L_{a}R_{b}$ | Two-sided cell |

## Further Reading

- P. A. M. Dirac, "The quantum theory of the electron," *Proceedings of the Royal Society A* **117** (1928) 610–624, for the first-order equation and its second-order consequence.
- O. Klein, "Elektrodynamik und Wellenmechanik vom Standpunkt des Korrespondenzprinzips," *Zeitschrift für Physik* **41** (1927) 407–442, and W. Gordon, "Der Comptoneffekt nach der Schrödingerschen Theorie," *Zeitschrift für Physik* **40** (1926) 117–133, for the second-order relativistic wave equation.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the identity $(\mathsf D-\mu)(\mathsf D+\mu)=\Box-\mu^2$ and the plane-wave spinors.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the Clifford algebra, the gamma matrices, and the mass shell.
- P. Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2001), for the classification of Clifford algebras, the minimal modules, and the square root of the wave operator.
- H. B. Lawson and M.-L. Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the complex and real Clifford algebras and their irreducible modules.
- I. R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the periodicity and the module dimensions.
- V. V. Kravchenko, *Quaternionic Analysis and Its Applications* (Birkhäuser, 2003), for the quaternionic Dirac operator and its relation to the Euclidean Clifford algebra.
- The corpus articles *The Klein–Gordon Equation in Biquaternionic Form*, *Klein–Gordon from the Dirac Square in Biquaternionic Form*, *The Dirac Equation in Biquaternionic Form*, *The Biquaternion D'Alembertian and Its Green's Functions*, and *Algebra and Element Conventions* for the conventions and the results this article builds on.
- The corpus articles *Two-Sided Operators on the Biquaternion Algebra*, *Element and Operator Representations: The Three Actions*, and *The Polarized Module of the Biquaternion Algebra* for the two-sided algebra, the nilpotent that swaps the minimal left ideals, and the $M_2$/$M_4$ dictionary.
