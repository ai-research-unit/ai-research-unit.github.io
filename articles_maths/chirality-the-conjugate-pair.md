# __Chirality: The Conjugate Pair__

## Introduction

**Chirality is the grading of the conjugate pair, not the sign of the Peirce decomposition.** The Peirce sign is an inner involution of the regular module; its two eigenspaces are minimal left ideals and both are isomorphic to the simple module $S$. The chiral sign is the nontrivial central involution of the complexification $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{B}_{\mathbb{R}}$; its two eigenspaces are $S$ and its conjugate $S^{\mathrm{c}}$, which are not isomorphic. The article proves the two no-go statements that separate the notions, constructs the chiral grading, identifies it with the central idempotents $\tfrac12(1\pm ij)$, and shows that the mass is the off-diagonal invariant pairing between the two halves, not an algebra element and not a Peirce nilpotent. A final section separates the four uses of the word spin in the corpus: the highest weight, the Peirce index, the chirality and the adjoint action. No Clifford algebra is used.

The Peirce decomposition is *The Peirce Decomposition of the Biquaternion Algebra*; the simple module and its endomorphisms are *The Category of Modules*; the conjugate module is *Conjugate-Linear Maps and the Conjugate Dual*; the matrix model and its $\epsilon$ are *$M_2(\mathbb{C})$ Representation : The Conjugations and the Adjoints*; the invariant form of the spinor module is *The Canonical Hermitian Form on the Regular Module of the Biquaternion Algebra*. The physical interpretation is *Biquaternion Physical Interpretation of Chirality*.

## The Peirce Sign

**Definition.** Let

$$
\tilde\Pi_+=\tfrac12(e_t+i\vec e_z),\qquad
\tilde\Pi_-=\tfrac12(e_t-i\vec e_z),
$$

and let $S_\pm=\mathbb{B}\tilde\Pi_\pm$ be the two Peirce carriers. The **Peirce sign** is the right multiplication

$$
P=R_{i\vec e_z}=R_{\tilde\Pi_+}-R_{\tilde\Pi_-}.
$$

The two off-diagonal nilpotents are

$$
\vec\Upsilon_x=\tfrac12(i\vec e_x-\vec e_y),\qquad
\vec\Upsilon_y=\tfrac12(i\vec e_x+\vec e_y).
$$

**Proposition (the Peirce table).** The nilpotents satisfy $\vec\Upsilon_x^2=\vec\Upsilon_y^2=0$, and

$$
\vec\Upsilon_x\vec\Upsilon_y=\tilde\Pi_+,\qquad
\vec\Upsilon_y\vec\Upsilon_x=\tilde\Pi_-,
$$

$$
\tilde\Pi_+\vec\Upsilon_x=\vec\Upsilon_x,\qquad
\vec\Upsilon_x\tilde\Pi_-=\vec\Upsilon_x,\qquad
\tilde\Pi_-\vec\Upsilon_y=\vec\Upsilon_y,\qquad
\vec\Upsilon_y\tilde\Pi_+=\vec\Upsilon_y.
$$

*Proof.* The table is the multiplication table of the matrix units $E_{11},E_{12},E_{21},E_{22}$ under the model $\mathsf{M}_2(\vec e_x)=-i\sigma_1$, $\mathsf{M}_2(\vec e_y)=-i\sigma_2$, $\mathsf{M}_2(\vec e_z)=-i\sigma_3$. The computation is in *The Peirce Decomposition of the Biquaternion Algebra*, and the identification of the nilpotents with the matrix units is in *The Column Ideals of a Matrix Ring*.

**Proposition.** $P^2=\mathrm{id}$, $P$ commutes with every left multiplication, and

$$
P(s)=s\quad(s\in S_+),\qquad P(s)=-s\quad(s\in S_-).
$$

*Proof.* $i\vec e_z=\tilde\Pi_+-\tilde\Pi_-$. Right multiplication by $\tilde\Pi_+$ is the identity on $S_+$ and zero on $S_-$, because $s\tilde\Pi_+=s$ for $s\in S_+$ and $s\tilde\Pi_+=0$ for $s\in S_-$; right multiplication by $\tilde\Pi_-$ is the opposite. Right multiplication commutes with left multiplication by associativity.

**Theorem (the Peirce sign is a copy index).** $S_+\cong S_-\cong S$ as left $\mathbb{B}$-modules. The map $R_{\vec\Upsilon_x}:S_+\to S_-$ is an isomorphism, with inverse $R_{\vec\Upsilon_y}$.

*Proof.* For $s\in S_+$, $s=s\tilde\Pi_+$; the table gives $s\vec\Upsilon_x=s\tilde\Pi_+\vec\Upsilon_x=s\vec\Upsilon_x$, and $(s\vec\Upsilon_x)\tilde\Pi_-=s(\vec\Upsilon_x\tilde\Pi_-)=s\vec\Upsilon_x$, so the image lies in $S_-$. The composite $R_{\vec\Upsilon_y}R_{\vec\Upsilon_x}$ is $R_{\vec\Upsilon_x\vec\Upsilon_y}=R_{\tilde\Pi_+}$, the identity on $S_+$; the other composite is the identity on $S_-$. Hence $S_+\cong S_-$. Both are minimal left ideals, hence isomorphic to the unique simple module $S$.

**Theorem (every inner $\pm$ grading of the regular module is a copy grading).** Every $\mathbb{B}$-linear endomorphism of $\mathbb{B}$ is a right multiplication $R_q$. If $R_q^2=\mathrm{id}$, then $q^2=e_t$, and either $q=\pm e_t$, in which case $R_q=\pm\mathrm{id}$, or $q$ is a nontrivial involution and the eigenspaces of $R_q$ are the minimal left ideals

$$
\mathbb{B}\tilde\Pi_+(q)=\mathbb{B}\tfrac12(e_t+q),\qquad
\mathbb{B}\tilde\Pi_-(q)=\mathbb{B}\tfrac12(e_t-q),
$$

both isomorphic to $S$.

*Proof.* An endomorphism $T$ of the left module $\mathbb{B}$ is determined by $T(e_t)=q$, and then $T(a)=T(ae_t)=aT(e_t)=aq=R_q(a)$. The composite of right multiplications is $R_qR_{q'}=R_{q'q}$, so $R_q^2=\mathrm{id}$ is $q^2=e_t$. The polynomial $X^2-1$ has distinct roots, so a non-central $q$ with $q^2=e_t$ has eigenvalues $+1$ and $-1$, each with a one-dimensional eigenspace in the matrix model; the two idempotents $\tfrac12(e_t\pm q)$ are primitive and their left ideals are minimal. If $q$ is central, then $q=\pm e_t$ because $Z(\mathbb{B})=\mathbb{C}e_t$ and the only central idempotents of $\mathbb{C}$ are $0$ and $e_t$.

**Corollary (the no-go for the regular module).** No element of $\mathbb{B}$ grades $\mathbb{B}$ into two non-isomorphic summands. The regular module is $S\oplus S$, and every inner $\pm$ grading of it grades copies of $S$.

This is the precise sense in which the Peirce sign is not a chirality. It is a legitimate sign, it is Lorentz invariant because it is $\mathbb{B}$-linear, and the nilpotent $R_{\vec\Upsilon_x}$ is odd under it, $P R_{\vec\Upsilon_x}=-R_{\vec\Upsilon_x}P$; but both of its sides carry the same representation.

## The Centre Has No Nontrivial Idempotent

**Theorem.** The centre of $\mathbb{B}_{\mathbb{R}}$ is $\mathbb{C}e_t$, and its only idempotents are $0$ and $e_t$. Hence $\mathbb{B}_{\mathbb{R}}$ has no nontrivial central idempotent and no nontrivial central involution.

*Proof.* The algebra is $\mathbb{B}\cong M_2(\mathbb{C})$; its centre is the scalar matrices $\mathbb{C}I$, of real dimension two. An idempotent $\lambda I$ satisfies $\lambda^2=\lambda$, so $\lambda\in\{0,1\}$. The central involutions are $\pm e_t$.

**Corollary.** Every nontrivial involution $q\in\mathbb{B}_{\mathbb{R}}$ is non-central, and the grading $R_q$ is a copy grading by the previous theorem. A nontrivial central $\pm$ requires an extension of the algebra.

The corollary is the reason chirality cannot be an element of the biquaternion algebra. The algebra has one central sign, the trivial one; every other sign is a sign inside the fibre $S$, not a sign between two inequivalent fibres.

## The Conjugate Module

**Definition.** Let $S$ be the simple left $\mathbb{B}$-module. The **conjugate module** $S^{\mathrm{c}}$ is the same additive group with the scalar action

$$
\lambda\cdot s=\bar\lambda s,\qquad a\cdot s=as,
$$

for $\lambda\in\mathbb{C}$ and $a\in\mathbb{B}_{\mathbb{R}}$.

**Proposition.** $S^{\mathrm{c}}$ is a complex module over the real algebra $\mathbb{B}_{\mathbb{R}}$. The action map $a\mapsto L_a$ is conjugate-linear in $a$, so $S^{\mathrm{c}}$ is not a complex $\mathbb{B}$-module. The identity map $\mathrm{id}:S\to S^{\mathrm{c}}$ is a real-linear isomorphism and is $\mathbb{B}_{\mathbb{R}}$-linear; it is not complex-linear.

*Proof.* For $\lambda\in\mathbb{C}$ and $a\in\mathbb{B}_{\mathbb{R}}$, $L_a(\lambda\cdot s)=L_a(\bar\lambda s)=\bar\lambda L_a(s)=\lambda\cdot L_a(s)$, so the action is complex-linear in the vector and the module axioms hold. In the algebra variable, $L_{\lambda a}=\bar\lambda L_a$ on $S^{\mathrm{c}}$, so the action is conjugate-linear in $a$. The identity satisfies $\mathrm{id}(as)=a\cdot\mathrm{id}(s)$, and $\mathrm{id}(\lambda s)=\lambda s$ while $\lambda\cdot\mathrm{id}(s)=\bar\lambda s$, so it is not complex-linear.

**Theorem (real isomorphism, complex inequivalence).** $S$ and $S^{\mathrm{c}}$ are isomorphic as real $\mathbb{B}_{\mathbb{R}}$-modules and are not isomorphic as complex $\mathbb{B}_{\mathbb{R}}$-modules. Every $\mathbb{B}_{\mathbb{R}}$-linear map $T:S\to S^{\mathrm{c}}$ is zero.

*Proof.* The identity is the real isomorphism. For the complex statement, a $\mathbb{C}$-linear map $T:S\to S^{\mathrm{c}}$ is, on the underlying space, a conjugate-linear map $T(s)=C\bar s$, and $T(as)=aT(s)$ reads $C\bar A=AC$ for every $A\in M_2(\mathbb{C})$. Taking $A=E_{12}$ and $A=E_{21}$ gives $C=cI$; taking $A=\operatorname{diag}(1,i)$ gives $c\operatorname{diag}(1,-i)=c\operatorname{diag}(1,i)$, hence $c=0$. So $T=0$.

**Corollary.** Chirality is a complex phenomenon: the two halves are real-isomorphic and complex-inequivalent. The distinction is invisible to the real algebra and visible to its complex representations.

The theorem is the module-level content of the complex type. It is also the reason the two halves can carry different gauge representations: a gauge action that is complex-linear sees the difference, while a real-linear action need not.

## Chirality: The Central Sign of the Complexification

**Theorem (the complexification).** Let $j$ be a new central imaginary unit, $j^2=-1$, commuting with $i$. Then

$$
\mathbb{B}[j]=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{B}_{\mathbb{R}}\cong\mathbb{B}\oplus\mathbb{B}
$$

as real algebras, and the central idempotents are

$$
e_+=\tfrac12(1+ij),\qquad e_-=\tfrac12(1-ij),\qquad
e_++e_-=e_t,\qquad e_+e_-=0.
$$

*Proof.* The map $a+bj\mapsto(a+ib,\,a-ib)$ is an isomorphism of real algebras onto $\mathbb{B}\oplus\mathbb{B}$, with inverse $(A,B)\mapsto\tfrac12(A+B)+\tfrac{1}{2i}(A-B)j$. The images of $e_\pm$ are $(0,e_t)$ and $(e_t,0)$ in one order, so $e_\pm$ are the central idempotents.

**Definition.** The **chirality** is

$$
\chi=ij=e_+-e_-.
$$

**Proposition.** $\chi^2=e_t$, $\chi$ is central, and $\chi\notin\mathbb{B}_{\mathbb{R}}$.

*Proof.* $i$ and $j$ commute, $i^2=j^2=-1$, so $(ij)^2=1$. Centrality is inherited from $i$ and $j$. If $\chi\in\mathbb{B}_{\mathbb{R}}$, then $j=\chi/i\in\mathbb{B}_{\mathbb{R}}$ because $i^{-1}\in\mathbb{B}_{\mathbb{R}}$ and $\mathbb{B}_{\mathbb{R}}$ is a subalgebra. But $j\notin\mathbb{B}_{\mathbb{R}}$: every element of $\mathbb{B}_{\mathbb{R}}=1\otimes\mathbb{B}_{\mathbb{R}}$ has first tensor factor $1$, while $j=i_{\mathrm{new}}\otimes1$ has first factor $i_{\mathrm{new}}$.

**The Dirac module.** Let

$$
\Delta=S\oplus S^{\mathrm{c}}.
$$

In the $\epsilon$-dressed model of $S^{\mathrm{c}}$, with

$$
\epsilon=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
$$

the real algebra acts by

$$
\rho(a)=\operatorname{diag}\bigl(\mathsf{M}_2(a),\ \epsilon\,\overline{\mathsf{M}_2(a)}\,\epsilon^{-1}\bigr),
$$

and the action extends to $\mathbb{B}[j]$ by $\rho(j)=iI_4$. Then

$$
\rho(i)=\operatorname{diag}(iI_2,-iI_2),\qquad
\rho(\chi)=\rho(i)\rho(j)=\operatorname{diag}(-I_2,I_2).
$$

*Proof.* The first display is the definition of the $\epsilon$-dressed conjugate action: on $S$ the element $i$ acts as $iI$, and on $S^{\mathrm{c}}$ it acts as $\epsilon\overline{iI}\epsilon^{-1}=-iI$. The second is the product with the scalar $iI_4$ that represents $j$.

**Theorem (the chiral projectors).** The operators

$$
P_L=\tfrac12(e_t-\chi)=\tfrac12(1-\chi),\qquad
P_R=\tfrac12(e_t+\chi)=\tfrac12(1+\chi)
$$

are idempotent, orthogonal and complete, and on $\Delta$

$$
P_L(s,t)=(s,0),\qquad P_R(s,t)=(0,t).
$$

*Proof.* $\chi^2=1$ gives $P_L^2=P_L$, $P_R^2=P_R$, $P_LP_R=0$, $P_L+P_R=1$. The matrix form $\chi=\operatorname{diag}(-I,I)$ gives the displayed action.

**Theorem (uniqueness of the chiral grading).** $\operatorname{End}_{\mathbb{B}_{\mathbb{R}}}(\Delta)=\mathbb{C}\oplus\mathbb{C}$, consisting of the maps $(s,t)\mapsto(\alpha s,\beta t)$. The nontrivial central involution of this ring is $\chi$, up to sign. Hence the chiral grading is canonical.

*Proof.* $S$ and $S^{\mathrm{c}}$ are simple and non-isomorphic, so Schur's lemma gives $\operatorname{Hom}(S,S)=\mathbb{C}$, $\operatorname{Hom}(S^{\mathrm{c}},S^{\mathrm{c}})=\mathbb{C}$ and $\operatorname{Hom}(S,S^{\mathrm{c}})=\operatorname{Hom}(S^{\mathrm{c}},S)=0$. The endomorphism ring is therefore $\mathbb{C}\oplus\mathbb{C}$, with the two idempotents $(1,0)$ and $(0,1)$; the nontrivial central involutions are $\pm(1,-1)$.

**Theorem (chirality is not a biquaternion).** No element of $\mathbb{B}_{\mathbb{R}}$ acts as $\chi$ on $\Delta$. In the matrix model, an element $a$ acts as $\operatorname{diag}(A,\epsilon\bar A\epsilon^{-1})$ with $A=\mathsf{M}_2(a)$, and $\operatorname{diag}(A,\epsilon\bar A\epsilon^{-1})=\operatorname{diag}(-I,I)$ would require $A=-I$ and $\epsilon\bar A\epsilon^{-1}=I$, hence $\bar A=I$, which contradicts $A=-I$.

**Remark (the two signs).** The Peirce sign $P=R_{i\vec e_z}$ is inner, implemented by the element $i\vec e_z\in\mathbb{B}$, and grades $S_+\cong S_-$; the chiral sign $\chi=ij$ is not in $\mathbb{B}$ and grades $S\not\cong S^{\mathrm{c}}$. The first is inner and non-central; the second is central and outside the algebra. The two signs are different objects, and only the second is chirality.

## The Mass Is the Off-Diagonal Pairing

**The invariant pairing.** In the $\epsilon$-dressed model, let

$$
\beta(s,t)=s^{\dagger}t
$$

on $S\times S^{\mathrm{c}}$. For $g\in SL_2(\mathbb{C})$ the right half transforms by $(g^{\dagger})^{-1}=\epsilon\bar g\epsilon^{-1}$, so

$$
\beta\bigl(gs,(g^{\dagger})^{-1}t\bigr)
=s^{\dagger}g^{\dagger}(g^{\dagger})^{-1}t
=\beta(s,t).
$$

The form is sesquilinear, nondegenerate and invariant. It is the unique invariant pairing up to a scalar: a sesquilinear form on $S\times S^{\mathrm{c}}$ is a linear map $\bar S\otimes S^{\mathrm{c}}\to\mathbb{C}$, and Schur's lemma gives $\operatorname{Hom}_{SL_2(\mathbb{C})}(\bar S\otimes S^{\mathrm{c}},\mathbb{C})=\mathbb{C}$ because the trivial representation occurs once in $\bar S\otimes S^{\mathrm{c}}$.

**The mass.** The mass term is

$$
m\,\beta(s,t)+\overline{m\,\beta(s,t)}.
$$

The algebra fixes the shape $\beta$ and not the number $m$; the number is the mass.

**Proposition (the mass operator is off-diagonal and chirality-odd).** Relative to the positive Hermitian form on $\Delta$, the operator $D_m$ defined by $\beta(s,t)=\langle (s,0),D_m(0,t)\rangle$ is

$$
D_m=\begin{pmatrix}0&m\\ \bar m&0\end{pmatrix},
\qquad
\chi D_m\chi=-D_m.
$$

*Proof.* The pairing is off-diagonal, so $D_m$ maps $S$ to $S^{\mathrm{c}}$ and $S^{\mathrm{c}}$ to $S$; the matrix form follows. The sign is $\chi D_m\chi=(-1)(+1)D_m=-D_m$ on each off-diagonal block.

**Proposition (the mass is not a module map).** For $m\neq0$, $D_m$ is not $\mathbb{B}_{\mathbb{R}}$-linear. A $\mathbb{B}_{\mathbb{R}}$-linear off-diagonal map $S\to S^{\mathrm{c}}$ would be an intertwiner, and $\operatorname{Hom}_{\mathbb{B}_{\mathbb{R}}}(S,S^{\mathrm{c}})=0$.

*Proof.* The off-diagonal block of a $\mathbb{B}_{\mathbb{R}}$-linear $D_m$ is a $\mathbb{B}_{\mathbb{R}}$-linear map $S\to S^{\mathrm{c}}$; by the non-isomorphism theorem it is zero, so $m=0$. The same argument applies to the other off-diagonal block.

The proposition is the precise reason the mass is a pairing and not an operator of the algebra. It exists because the two halves are inequivalent: there is no equivariant map between them, but there is an invariant bilinear between them. The mass is the scale of that bilinear.

**The Peirce nilpotent is not the chiral mass.** The right multiplication $R_{\vec\Upsilon_x}:S_+\to S_-$ is $\mathbb{B}$-linear, hence $\mathbb{B}_{\mathbb{R}}$-linear, and it flips the Peirce index. It is a copy flip. The chiral mass $D_m$ is not $\mathbb{B}_{\mathbb{R}}$-linear and flips the chiral index. The two couplings act on different pairs of spaces and have different invariance; they must not be identified.

## The Other Uses of the Word Spin

The corpus uses "spin" for four different objects. They are not rivals; they answer different questions, and conflating them is the source of the "Peirce chirality" misnomer.

**The highest weight.** In *The Weight of a Frame Root and the Spin Quantum Number*, a root $h=2e-1$ acts on a carrier, its eigenvalues are weights, and the spin is half the highest weight, $j=\lambda/2$. On the Peirce carrier the weights are $\pm1$, so $j=\tfrac12$; on the traceless part under the adjoint action the weights are $+2,0,-2$, so $j=1$. This spin is a **magnitude**: it measures the size of the representation. The factor $\tfrac12$ is the normalisation of the spin, and it is the same factor that makes a spinor rotation periodic in $4\pi$ rather than $2\pi$.

**The Peirce index.** The sign $P=R_{i\vec e_z}$ grades $S_+\cong S_-$. This is a **copy label**, not a chirality and not a magnitude. It says which of two isomorphic copies a vector lies in.

**The chirality.** The central sign $\chi=ij$ grades $S$ against $S^{\mathrm{c}}$. This is a **sign**, not a magnitude: it says which of two inequivalent halves a field lies in. A field can carry both a spin magnitude and a chiral sign; the two are independent labels.

**The adjoint action.** In *Integer-Spin Quantization and the Adjoint Action on the Material Sector in Biquaternionic Form*, the spin-one representation is the adjoint action of the rotation algebra on the material sector $\mathbb{M}_-$, and the higher integer spins are symmetric traceless tensors of that sector. This is a **representation** of the rotation group, not a grading. It supplies the integer-spin multiplets, not the chiral halves.

| Use | Object | Carrier | What it labels | Chirality? |
| --- | --- | --- | --- | --- |
| Highest weight | $h=2e-1$, weights $\lambda$, $j=\lambda/2$ | a carrier $W$ | the size of the representation | no |
| Peirce index | $P=R_{i\vec e_z}$ | $S_+\oplus S_-$ | the copy | no |
| Chirality | $\chi=ij$ | $S\oplus S^{\mathrm{c}}$ | the chiral half | yes |
| Adjoint / integer spin | $\operatorname{ad}_{\vec e_k}$ on $\mathbb{M}_-$ | $\mathbb{M}_-$, symmetric traceless tensors | the integer-spin multiplet | no |

The highest-weight spin and the adjoint spin are representation labels; the Peirce index is a copy label; only the chirality is a grading into inequivalent halves. A theory needs all four labels, and the algebra supplies each of them at a different level: the root supplies the weights, the Peirce decomposition supplies the copies, the adjoint action supplies the integer-spin multiplets, and the complexification supplies the chiral grading.

## Summary

Chirality is the central sign of the complexification, not the inner sign of the Peirce decomposition. The Peirce sign $P=R_{i\vec e_z}$ is implemented by the element $i\vec e_z\in\mathbb{B}$ and grades the two minimal left ideals $S_+\cong S_-\cong S$. The chiral sign $\chi=ij$ is the nontrivial central involution of

$$
\mathbb{B}[j]=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{B}_{\mathbb{R}}\cong\mathbb{B}\oplus\mathbb{B},
\qquad
e_\pm=\tfrac12(1\pm ij),
$$

and it grades the Dirac module $\Delta=S\oplus S^{\mathrm{c}}$ into two non-isomorphic halves. The two halves are real-isomorphic and complex-inequivalent: $S\not\cong S^{\mathrm{c}}$ as complex $\mathbb{B}_{\mathbb{R}}$-modules, while the identity is a real isomorphism. The mass is the unique $SL_2(\mathbb{C})$-invariant sesquilinear pairing $S\times S^{\mathrm{c}}\to\mathbb{C}$, off-diagonal and chirality-odd; it is not a $\mathbb{B}_{\mathbb{R}}$-linear operator, and it is not the Peirce nilpotent.

$$
\boxed{\;
\chi=ij,\quad \chi^2=e_t,\quad \chi\notin\mathbb{B},\quad
\Delta=S\oplus S^{\mathrm{c}},\quad \chi=\operatorname{diag}(-I_2,I_2),\quad
P=R_{i\vec e_z}\in\mathbb{B},\quad S_+\cong S_-\cong S.
\;}
$$

| Sign | Operator | Type | Eigenspaces | Modules |
| --- | --- | --- | --- | --- |
| Peirce index | $P=R_{i\vec e_z}$ | inner, non-central | $S_+$, $S_-$ | $S$, $S$ |
| Chirality | $\chi=ij$ | central, outside $\mathbb{B}$ | $S$, $S^{\mathrm{c}}$ | $S$, $S^{\mathrm{c}}$ |
| Sector | ${}^{*}$ | antilinear involution | $\mathbb{M}_+$, $\mathbb{M}_-$ | real subspaces |
| Spectral | $H=i\vec e_z$ | root of $+1$ in $\mathbb{B}$ | $S_+$, $S_-$ | $S$, $S$ |

The first and the fourth rows are the same decomposition read as an operator and as a root. The third row is a real-form split of the algebra, not a grading of the module. Only the second row is chirality.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra |
| $\mathbb{B}_{\mathbb{R}}$ | $\mathbb{B}$ as a real algebra |
| $S$ | the simple left $\mathbb{B}$-module, $\mathbb{C}^2$ |
| $S^{\mathrm{c}}$ | the conjugate module, $S$ with conjugated scalars |
| $\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec e_z)$ | the Peirce idempotents |
| $S_\pm=\mathbb{B}\tilde\Pi_\pm$ | the Peirce carriers, both $\cong S$ |
| $\vec\Upsilon_x=\tfrac12(i\vec e_x-\vec e_y)$, $\vec\Upsilon_y=\tfrac12(i\vec e_x+\vec e_y)$ | the off-diagonal nilpotents |
| $P=R_{i\vec e_z}$ | the Peirce sign, a copy index |
| $j$ | a new central imaginary unit, $j^2=-1$ |
| $\mathbb{B}[j]=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{B}_{\mathbb{R}}$ | the one-step complexification |
| $e_\pm=\tfrac12(1\pm ij)$ | the central idempotents |
| $\chi=ij=e_+-e_-$ | the chirality |
| $\Delta=S\oplus S^{\mathrm{c}}$ | the Dirac module |
| $P_L=\tfrac12(1-\chi)$, $P_R=\tfrac12(1+\chi)$ | the chiral projectors |
| $\epsilon=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$ | the invariant form of the spinor module |
| $\beta(s,t)=s^{\dagger}t$ | the invariant pairing $S\times S^{\mathrm{c}}\to\mathbb{C}$ |
| $D_m$ | the mass operator, off-diagonal |

## Further Reading

- [The Peirce Decomposition of the Biquaternion Algebra](the-peirce-decomposition-in-the-biquaternion-algebra.html), for the two idempotents, the four Peirce lines and the multiplication table.
- [The Column Ideals of a Matrix Ring: One Idempotent and $n-1$ Nilpotents](the-column-ideals-of-a-matrix-ring.html), for the identification of the nilpotents with the matrix units.
- [The Category of Modules](modules-over-the-biquaternion-algebra.html), for the simple module, $\operatorname{End}_{\mathbb{B}}(S)=\mathbb{C}$ and the classification of left modules.
- [The Weight of a Frame Root and the Spin Quantum Number](the-weight-of-a-frame-root-and-the-spin-quantum-number.html), for the highest weight, the half-weight normalisation and the weights of the Peirce carrier and of the traceless part.
- [Integer-Spin Quantization and the Adjoint Action on the Material Sector in Biquaternionic Form](../articles_physics/integer-spin-quantization-and-the-adjoint-action-on-the-material-sector-in-biquaternionic-form.html), for the adjoint-action reading of integer spin and the symmetric traceless tensors.
- [Conjugate-Linear Maps and the Conjugate Dual](conjugate-linear-maps-and-the-conjugate-dual.html), for the conjugate module $M^{\varsigma}$ and the semilinear maps.
- [$M_2(\mathbb{C})$ Representation : The Conjugations and the Adjoints](m2c-representation-the-conjugations-and-the-adjoints.html), for the matrix model, the $\epsilon$-dressed conjugation and the adjugate.
- [The Canonical Hermitian Form on the Regular Module of the Biquaternion Algebra](the-canonical-hermitian-form-on-the-regular-module-of-the-biquaternion-algebra.html), for the positive Hermitian form used to pass from the pairing to the mass operator.
- [The Two Chiralities of $M_4(\mathbb{C})$](the-two-chiralities-of-m4c.html), for the comparison with the matrix case, where the chirality is the $\mathbb{Z}/2$ quotient of a $\mathbb{Z}/4$ root grading.
