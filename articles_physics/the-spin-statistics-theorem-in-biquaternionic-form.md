# __The Spin–Statistics Theorem in Biquaternionic Form__

## Introduction

The **spin–statistics theorem** is the statement that the spin of a field and the bracket that quantizes it are not independent. In a relativistic quantum field theory on Minkowski space whose inner product is positive definite and whose Hamiltonian is bounded below, a field of integer spin must be quantized with **commutators** and a field of half-integer spin with **anticommutators**: integer-spin fields are bosons, half-integer-spin fields are fermions. The theorem is a statement about the *choice of bracket*, not about the representation of the Lorentz group; the representation fixes the spin, and the theorem says that locality, positivity and Lorentz invariance together fix the bracket that goes with it.

The theorem is not among the results the companion articles derive. *Canonical Quantization of the Biquaternion Dirac Field* imposes anticommutation relations on the free biquaternion spinor field and lists the boundedness of the energy, together with microcausality and positivity, among the reasons the anticommutator is the appropriate one; it explicitly leaves the theorem itself to a dedicated article. *Fock Space and Creation/Annihilation Operators in Biquaternionic Form* finds that the algebra $\mathbb{B}$ hosts exactly one fermionic mode and no bosonic mode, and is careful to say that this is a *realization* and not a derivation of fermionic statistics. *The KMS Condition and the Biquaternion Framework* identifies a $\mathbb{Z}/2$ grading of the operator algebra as an additional structure that the biquaternion algebra does not by itself supply. This article is the dedicated treatment those three forward references call for. It does not rederive the parents' quantizations, plane waves or spin sums, which are used unchanged.

The division between what is established and what is only transcribed is stated at the outset and kept explicit.

- **Established, and recomputed below.** The rotation group acts inside $\mathbb{B}$ through the rotor group of unit real quaternions, which is the double cover of $SO(3)$; the rotor through $2\pi$ about any axis is $-e_t$. Under the rotor action the half-integer-spin representations are the odd tensor powers of the spinor module, on which $-e_t$ acts as $-\mathrm{id}$, while the integer-spin representations — the material sector and the even tensor powers — are the ones that descend to the Lorentz group, on which $-e_t$ acts as $+\mathrm{id}$. For the free spin-$\tfrac12$ field the equal-time **anticommutator** is a delta and the equal-time **commutator** is not: the former receives a $\delta^{(3)}(\vec\Delta)$ from the $\cos\theta\,I_4$ term of the spin sum, the latter only a Bessel kernel that is nonzero at every spatial separation. In the single-mode truncation of the algebra the spin ladder operators *are* the mode ladder operators, $\vec\Upsilon_x=\tilde S_+/\hbar$, with $\{\vec\Upsilon_x,\vec\Upsilon_y\}=e_t$, and the fermion-parity grading is the inner automorphism by the Hermitian involution $(-1)^F=i\vec e_z=2\tilde S_z/\hbar$. The algebra hosts one such fermionic mode and no bosonic mode, for a reason that is a trace identity.
- **Transcribed, not derived.** The force of the theorem — that among the four pairings of spin class with bracket only two survive — is imported from relativistic quantum field theory. What the biquaternion presentation adds is that the two surviving pairings are the two *inequivalent structures the algebra actually carries*: the double-valued module for half-integer spin and the single-valued rotations of the material sector for integer spin, together with the trace identity that decides which bracket the finite algebra can host.
- **Gap, left visible.** The article does not *derive* spin–statistics from the biquaternion algebra. The one-mode coincidence is exact but finite-dimensional, and it does not lift to the field. This gap is stated in the sections where it arises and collected in the open questions.

## The Theorem and Its Ingredients

The theorem has three independent inputs, and it is useful to record which of them the biquaternion framework supplies.

1. **The Lorentz representation.** Spin is the intrinsic angular momentum of a particle: in the rest frame it is the label $s$ of the $SU(2)$ little-group representation, with $S^2=\hbar^2s(s+1)$ and $S_z=\hbar m_s$, and for a massless particle it is helicity. In the biquaternion framework that label is carried by the representation of the double cover $SL(2,\mathbb{C})$ of the restricted Lorentz group. The covering homomorphism has kernel $\{\pm e_t\}$, so a representation either descends to $SO^+(1,3)$ — the integer-spin case — or is a genuine two-valued representation of the cover — the half-integer-spin case.
2. **Locality (microcausality).** Observables at spacelike separation must commute. A spinor field is not an observable; its bilinears are. If $\psi$ anticommutes with itself at spacelike separation the bilinears commute, while if it commutes the bilinears do not, because the spinor commutator is then a nonzero kernel. Locality therefore bears on the bracket, but only through the bilinears, and it is one of two constraints that must agree.
3. **Positivity.** The inner product on the state space must be positive definite and the Hamiltonian bounded below. For a half-integer-spin field, commuting modes give negative-norm states and a Hamiltonian unbounded below; anticommuting modes give the positive-definite fermionic Fock space and a bounded Hamiltonian.

The third ingredient is what makes the theorem non-trivial: the two-valuedness of the spinor makes $\psi$ and $-\psi$ physically indistinguishable, so the sign that separates commuting from anticommuting quantization is invisible in the classical field, and it has to be recovered from $\psi\psi^{*}$, that is from the norm. Locality and positivity are logically independent, and the theorem is the assertion that they always select the same bracket; for spin $\tfrac12$ both exclude the commuting one, and both exclusions are computed below.

The biquaternion framework supplies the first ingredient geometrically and the third ingredient only at the level of the finite single-mode algebra; it transcribes the second with the parents' plane-wave fields. The five sections that follow take them up in the order representation, mode, locality, positivity.

## Spin as a Representation of the Rotor Group

Rotations are realised in $\mathbb{B}$ by rotor conjugation. A rotation through $\theta$ about the unit axis $\vec u$ is generated by the unit real quaternion

$$
\tilde u(\theta,\vec u)=\cos\tfrac{\theta}{2}\,e_t+\sin\tfrac{\theta}{2}\,\sum_k \vec u_k\vec e_k\in\mathbb{H}_{\mathbb{B}},\qquad \tilde u\tilde u^{*}=e_t .
$$

It is the exponential of the spin angular momentum along $\vec u$. With $\tilde S_k=\tfrac{\hbar}{2}i\vec e_k\in\mathbb{M}_+$ for $k=x,y,z$,

$$
\tilde u(\theta,\vec u)=\exp\Big(-i\theta\sum_k\vec u_k\tilde S_k/\hbar\Big)=\exp\Big(\tfrac{\theta}{2}\sum_k\vec u_k\vec e_k\Big),
$$

the second form following from the first because $-i\tilde S_k/\hbar=\tfrac12\vec e_k$: the two imaginary units cancel, one from the exponent and one from $\tilde S_k$, by $i^2=-1$. Conjugation by $\tilde u$ rotates the vectors of the material sector $\mathbb{M}_-$, while left multiplication by $\tilde u$ acts on the spinor module and hence on states; the map $\tilde{Q}\mapsto\tilde u\tilde{Q}\tilde u^{*}$ on $\mathbb{M}_-$ has kernel $\{\pm e_t\}$ and is the covering homomorphism onto the rotation group. The rotation group is the quotient of the rotor group, which is $SU(2)$, by $\{\pm e_t\}$. These facts are established in the companion articles on angular momentum and on the Lorentz group, and are recalled here because the spin–statistics dichotomy is a statement about which side of the cover a representation lives on.

The representations of the cover split into two classes, and the theorem's spin input is exactly that split. The biquaternion algebra acts on itself by left multiplication, and this is where its irreducible modules live. As a module over $\mathbb{B}$, the algebra affords only $s=\tfrac12$ — the defining module $S$, since $\mathbb{B}\cong M_2(\mathbb{C})$ is simple and its left regular module is $S\oplus S$ — so the half-integer-spin structure is **native to the algebra as a module**, and it is double-valued, because $-e_t$ acts on a module element as $-\mathrm{id}$. The integer-spin representations are not modules of the algebra. $s=0$ is the centre under conjugation, where every rotor acts trivially; $s=1$ is the **adjoint action** on the three vector units $\vec e_k$ — equivalently on the three imaginary units $i\vec e_k$, since the central $i$ passes through a conjugation unchanged; and conjugation on the four-dimensional $\mathbb{M}_-$ is the direct sum $0\oplus1$ under rotations, the scalar $e_t$ fixed and the vector $\vec e_k$ rotating, which is the four-vector once the boosts are included. Tensor powers fill the rest. The $n$-fold tensor power of the module splits into spins $s=\tfrac{n}{2},\tfrac{n}{2}-1,\dots$, down to $\tfrac12$ for odd $n$ and to $0$ for even $n$, and on every summand $-e_t$ acts as $(-1)^{n}$, one factor of $-1$ from each of the $n$ module elements. So the odd powers carry only half-integer spins and the even powers only integer ones, and the dichotomy is the parity of the power.

| Representation | Carrier | Action of the rotor | Action of $-e_t$ | Spin |
|---|---|---|---|---|
| Defining spinor module | $\mathbb{C}^2$ (module) | left multiplication $\psi\mapsto\tilde U\psi$ | $-\mathrm{id}$ | $\tfrac12$ |
| Odd tensor powers | tensors over the module | left multiplication | $-\mathrm{id}$ | half-integer |
| Vector (adjoint) | the vector units $\vec e_k$ | conjugation $\vec Q\mapsto\tilde U\vec Q\tilde U^{*}$ | $+\mathrm{id}$ | $1$ |
| Even tensor powers | tensors over the module | tensor action | $+\mathrm{id}$ | integer |

On a representation of the cover with spin $s$ the nontrivial kernel element $-e_t$ acts as $(-1)^{2s}$, which is $+1$ for integer $s$ and $-1$ for half-integer $s$, and the table lists the elementary instances. This is the representation-theoretic content of the theorem's spin input, and it is the content of the companion article on the Lorentz group's classification, where the descent condition $m+n\in\mathbb{Z}$ separates the two cases.

## The Sign of the Two-Pi Rotation

Evaluate the rotor at $\theta=2\pi$ and $\theta=4\pi$:

$$
\boxed{\;\tilde u(2\pi,\vec u)=\cos\pi\,e_t=-e_t,\qquad \tilde u(4\pi,\vec u)=\cos 2\pi\,e_t=e_t\;}.
$$

The $2\pi$ rotation is the nontrivial element of the kernel $\{\pm e_t\}$ of the covering, whatever the axis. Its action therefore separates the two classes of the table above in the sharpest possible way.

- On a **four-vector** $\tilde{Q}\in\mathbb{M}_-$, conjugation by $-e_t$ is trivial, $(-e_t)\tilde{Q}(-e_t)^{*}=\tilde{Q}$. A rotation by $2\pi$ returns a vector to itself; the vector representation is single-valued.
- On a **spinor** $\psi$ in the module, $2\pi$ means left multiplication by $-e_t$, so $\psi\mapsto-\psi$. The spinor representation is double-valued; only a rotation by $4\pi$ returns the spinor to itself.

The sign is not an artefact of a basis. It is the image of the nontrivial element of $\pi_1(SO^+(1,3))\cong\mathbb{Z}/2$ under the covering homomorphism, and it is why a spinor has no single-valued representative.

For an **observable** the sign cancels. The gauge-invariant bilinears of a spinor field are quadratic, $\psi^{\dagger}iR_{\vec e_x}^{\mathrm{axf}}\,\mathcal{O}\psi$ with $\mathcal{O}$ a fixed operator of the frame, and under $\psi\mapsto-\psi$ they are unchanged. This is the precise sense in which $\psi$ and $-\psi$ are physically indistinguishable, and it is why the classical spinor field contains no information about whether its quanta are bosons or fermions. The $2\pi$ sign is a representation-theoretic fact about the spinor module; it is *half* of the spin–statistics connection, not the whole of it.

At the level of the operator algebra the two signs are worth distinguishing, because they act on different objects. A rotation by $2\pi$ multiplies the field by $-e_t$, so $\psi^{\mathrm{fop}}\mapsto-\psi^{\mathrm{fop}}$. The parity element $(-1)^F$ acts by inner automorphism on the algebra of the single mode, and it flips exactly the odd elements: $(-1)^F\vec\Upsilon_x(-1)^F=-\vec\Upsilon_x$ and likewise $\vec\Upsilon_y$, while $\tilde\Pi_-$ and $e_t$ are fixed. Both operations are $-\mathrm{id}$ on the odd part and $+\mathrm{id}$ on the even part, and that is the operator-level form of $(-1)^{2s}=(-1)^F$ at $s=\tfrac12$. It is a consistency of two structures; it does not yet say that the bracket *must* anticommute.

## The Algebra's Own One Fermionic Mode

The finite-dimensional algebra contains one fermionic mode, and the mode operators are the spin ladder operators. This is the finding of the Fock-space article, and it is the one place where the spin-$\tfrac12$ structure and the fermionic canonical relation are the same elements of $\mathbb{B}$ rather than two structures placed side by side.

The spin operators are $\tilde S_k=\tfrac{\hbar}{2}i\vec e_k\in\mathbb{M}_+$ for $k=x,y,z$, with the ladder combinations $\tilde S_\pm=\tfrac{\hbar}{2}(i\vec e_x\mp \vec e_y)$. The Fock-space article's truncated ladder is

$$
\vec\Upsilon_x=\tfrac12(i\vec e_x-\vec e_y)=\frac{\tilde S_+}{\hbar},\qquad
\vec\Upsilon_y=\tfrac12(i\vec e_x+\vec e_y)=\frac{\tilde S_-}{\hbar},
$$

and direct computation gives

$$
\boxed{\;\vec\Upsilon_x^2=0,\qquad (\vec\Upsilon_y)^2=0,\qquad
\{\vec\Upsilon_x,\vec\Upsilon_y\}=e_t,\qquad
[\vec\Upsilon_x,\vec\Upsilon_y]=i\vec e_z\ne e_t\;}.
$$

So the truncated ladder satisfies the **fermionic** canonical anticommutation relations exactly, with no truncation error, while its commutator fails the bosonic relation by a nonzero, non-central element. The number operator and the fermion-parity element are

$$
\tilde\Pi_-=\vec\Upsilon_y\vec\Upsilon_x=\tfrac12(e_t-i\vec e_z),\qquad
(-1)^F=e_t-2\tilde\Pi_-=i\vec e_z=\frac{2\tilde S_z}{\hbar},
$$

with $\tilde\Pi_-^2=\tilde\Pi_-$, so that $\tilde\Pi_-$ is a pure-state idempotent and the single-mode occupation is valued in $\{0,1\}$. Here $i\vec e_z$ is a root of $+1$, $(i\vec e_z)^2=e_t$, and $\tilde\Pi_+$ and $\tilde\Pi_-$ are its two associated idempotents. The parity element is Hermitian, squares to $e_t$, and gives the $\mathbb{Z}/2$ grading by inner automorphism,

$$
(-1)^F\vec\Upsilon_x\,(-1)^F=-\vec\Upsilon_x,\qquad
(-1)^F\tilde\Pi_-\,(-1)^F=\tilde\Pi_-.
$$

This is a sharp statement about the $\mathbb{Z}/2$ grading that the KMS article identifies as missing: for one mode it is not missing at all. It is realized **inside** $\mathbb{B}$ as conjugation by a Hermitian involution of the informational sector, and its odd subspace is the two-complex-dimensional span of $\vec\Upsilon_x$ and $\vec\Upsilon_y$. What the KMS article requires for a field is a grading on the *operator algebra of all modes*; the single-mode element above is not that, and the field grading is not an element of $\mathbb{B}$ by the dimension count. The two statements are compatible: the grading is algebraic for one mode and external for the field.

The bosonic counterpart fails for a sharper reason, a trace identity, worth recording separately from the dimension count. In $\mathbb{B}$ a canonical commutator would have to be central, $[\vec\Upsilon_x,\vec\Upsilon_y]=c\,e_t$ with $c\in\mathbb{C}$, since the centre is $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_t$. It is not central: the computed value is $i\vec e_z$, which anticommutes with $\vec e_x$ and with $\vec e_y$ and so lies outside the centre. That alone rules the relation out. The trace argument then rules out a central value independently, and it is worth recording because it uses nothing but linearity: with $\operatorname{Tr}_2$ the trace on the $2\times2$ reading of an element, $\operatorname{Tr}_2(e_t)=2\,\mathrm{Sc}(e_t)=2$, so

$$
0=\operatorname{Tr}_2\big([\vec\Upsilon_x,\vec\Upsilon_y]\big)=c\,\operatorname{Tr}_2(e_t)=2c,
$$

and hence $c=0$. No pair in $\mathbb{B}$ realizes the Heisenberg relation. The algebra hosts one fermionic mode and no bosonic mode; the second relation, $\vec\Upsilon_x\vec\Upsilon_y=e_t-\vec\Upsilon_y\vec\Upsilon_x$, which a fermionic mode satisfies and a bosonic mode cannot, is the identity that decides it.

The dimension count makes the same point. $\dim_\mathbb{C}M_2(\mathbb{C})=4=\dim_\mathbb{C}\mathbb{B}$, and the four elements $e_t,\vec\Upsilon_x,\vec\Upsilon_y,\vec\Upsilon_x\vec\Upsilon_y=\tilde\Pi_+$ span the algebra; one mode saturates it, so no second mode can be added, since $m$ fermionic modes generate $M_{2^m}(\mathbb{C})$, of dimension $4^m$, which exceeds four as soon as $m\ge2$. Whether the framework *selects* the fermionic structure, or merely has room for exactly one instance of it, is the open question the Fock-space article raises and this article does not decide. The single-mode coincidence is exact; it is a coincidence of dimensions until something more is said.

## Microcausality: The Equal-Time Brackets

The operator-level content of the theorem is a computation with the parents' free field. The mode expansion is

$$
\psi^{\mathrm{fop}}(x)=\int\!\frac{d^3p}{(2\pi)^3}\,\frac{1}{\sqrt{2E_{\vec p}}}
\sum_r\Big[a^{\mathrm{fop}}_r(\vec p)\,w^{(r)}(\vec p)\,\exp(-ip\cdot x)
+b^{\mathrm{fop}\dagger}_r(\vec p)\,v^{(r)}(\vec p)\,\exp(+ip\cdot x)\Big],
$$

with $\psi^{\mathrm{fop}\dagger}$ the adjoint and $w^{(r)}$, $v^{(r)}$ the parents' spinors. Write $L_aR_b\psi=a\psi b$ for the two-sided multiplier, with $L_aL_b=L_{ab}$, $R_aR_b=R_{ba}$, and every left multiplication commuting with every right one. The four cells of the reference frame are

$$
c_0=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}=iR_{\vec e_x}^{\mathrm{axf}},\qquad
c_k=iL_{e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\quad(k=x,y,z),
$$

and they obey $\{c_\mu,c_\nu\}=2\varepsilon_\mu\delta_{\mu\nu}I_4$ for each pair of indices, with $\varepsilon=(1,-1,-1,-1)$ and no sum implied. The index of $c_\mu$ is the coordinate index: with $x_0=t'$ the material time, $c_0$ is the cell paired with $\partial/\partial t'$ and $c_k$ the cell paired with $\partial/\partial x_k$. The same objects are the frame of *The Legacy Pauli Gamma Formulation* below, where they carry the gamma names, and where the fifth cell $c_5=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ joins them; only there are they called gammas.

The field satisfies the corpus's Dirac equation in cells,

$$
i\left(c_0\nabla_t+\sum_kc_k\nabla_k\right)\psi=m\psi,
$$

whose plane-wave form is $\slashed p\,w=mw$ with the momentum cell $\slashed p=c_0p_0-\sum_kc_kp_k$, because $\nabla_t\to-iE_{\vec p}$ and $\nabla_k\to+ip_k$ on $\exp(-ip\cdot x)$. Explicitly,

$$
\left(E_{\vec p}\,c_0-\sum_kp_k\,c_k-m\right)w=0,
$$

and $(\slashed p+m)v=0$ for the negative-frequency spinor. The minus on the spatial momentum is the sign convention of $\slashed p$, shared with *Canonical Quantization of the Biquaternion Dirac Field* and the propagator articles, and every sign below follows from it. A reader who instead takes the spatial cells with the opposite sign — the lowered generators of the textbook, which are the negatives of these — has the opposite sign in every display. The two conventions differ by $\vec p\mapsto-\vec p$, they give the same brackets, and this article keeps the corpus's.

The parents' spin sums read $\sum_r w^{(r)}\bar w^{(r)}=E_{\vec p}\,c_0-\sum_k p_k\,c_k+m$ and $\sum_r v^{(r)}\bar v^{(r)}=E_{\vec p}\,c_0-\sum_k p_k\,c_k-m$, with $p_0=E_{\vec p}$, the sign of the spatial term being the one of $\slashed p$ fixed above. Multiplying on the right by $c_0$ gives the adjoint spin sums

$$
\sum_r w^{(r)}w^{(r){}^{*}}=E_{\vec p}I_4+m\,c_0+c_0\sum_k c_k\,p_k,\qquad
\sum_r v^{(r)}v^{(r){}^{*}}=E_{\vec p}I_4-m\,c_0+c_0\sum_k c_k\,p_k,
$$

and the passage uses the algebra three times: $c_0^2=(iR_{\vec e_x}^{\mathrm{axf}})^2=-R_{\vec e_x^2}^{\mathrm{axf}}=I_4$, because $\vec e_x^2=-e_t$ and $i^2=-1$; $c_kc_0=-c_0c_k$, because the cells anticommute; and $c_0c_k=L_{e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$, because $R_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}=R_{\vec e_y\vec e_x}^{\mathrm{axf}}=R_{-\vec e_z}^{\mathrm{axf}}$ and $i^2=-1$ again. The two factors of $i$ multiply to $-1$ and the reversal of the two right multipliers flips the sign back, so the double imaginary $i\cdot i$ leaves a real cell: the spinorial part of the spin sum carries no imaginary unit.

The field is a spinor-module field; the biquaternion content is the module on which it is built and the notation, and the mode algebra is imposed. Two choices are available. The **Fermi choice** imposes

$$
\{a^{\mathrm{fop}}_r(\vec p),a^{\mathrm{fop}\dagger}_s(\vec k)\}=(2\pi)^3\delta_{rs}\delta^{(3)}(\vec p-\vec k),\qquad
\{b^{\mathrm{fop}}_r(\vec p),b^{\mathrm{fop}\dagger}_s(\vec k)\}=(2\pi)^3\delta_{rs}\delta^{(3)}(\vec p-\vec k),
$$

with all other brackets vanishing, and the **Bose choice** replaces both braces by brackets.

**The anticommutator (Fermi choice).** At equal times $x_0=y_0$ the two branches enter with opposite phases, and with $\theta=\vec p\cdot\vec\Delta$, where $\vec\Delta=\vec x-\vec y$ is the separation and $\vec x=x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$ (the sign of $\theta$ is fixed by the mode-expansion convention and drops out of the anticommutator, only $\cos\theta$ surviving there),

$$
\sum_r\Big[w^{(r)}w^{(r){}^{*}}\exp(+i\theta)+v^{(r)}v^{(r){}^{*}}\exp(-i\theta)\Big]
=2E_{\vec p}\cos\theta\,I_4
+2im\sin\theta\,c_0
+2\cos\theta\,c_0\sum_k c_k\,p_k .
$$

The map $\vec p\mapsto-\vec p$ sends $\theta\mapsto-\theta$ and $c_0\sum_k c_k\,p_k\mapsto-c_0\sum_k c_k\,p_k$. The first term is even and the second and third are odd, so the odd terms vanish under symmetric integration and

$$
\boxed{\;\{\psi^{\mathrm{fop}}_a(x,t'),{\psi^{\mathrm{fop}}_b}^\dagger(y,t')\}=\delta_{ab}\,\delta^{(3)}(\vec\Delta)\;}.
$$

The spinorial part, $2\cos\theta\,c_0\sum_kc_kp_k$, shares the phase $\cos\theta$ of the scalar term but not its fate. The scalar term is even in $\vec p$ and survives; the spinorial term carries the odd factor $\sum_kc_kp_k$, so it is odd as a whole and integrates to zero. Same phase, different parity — the two are decided by the momentum dependence, not by the phase, and that is the distinction the check is there to make. Division by $2E_{\vec p}$ leaves the even part $\cos\theta\,I_4$, which integrates to $\delta^{(3)}(\vec\Delta)$, and the anticommutator is local.

**The commutator (Bose choice for the same field).** Replacing the plus between the branches by a minus, the same spin sums give

$$
\sum_r\Big[w^{(r)}w^{(r){}^{*}}\exp(+i\theta)-v^{(r)}v^{(r){}^{*}}\exp(-i\theta)\Big]
=2iE_{\vec p}\sin\theta\,I_4
+2m\cos\theta\,c_0
+2i\sin\theta\,c_0\sum_k c_k\,p_k .
$$

Here the first term is odd and the last two are even, so dropping the odd term and dividing by $2E_{\vec p}$ leaves

$$
[\psi^{\mathrm{fop}}(x,t'),\psi^{\mathrm{fop}\dagger}(y,t')]
=c_0\Big(m-i\sum_k c_k\nabla_k\Big)F(\vec\Delta),
\qquad
F(\vec\Delta)=\int\!\frac{d^3p}{(2\pi)^3}\,\frac{1}{E_{\vec p}}\cos(\vec p\cdot\vec\Delta),
$$

with $\nabla_k=\partial/\partial\Delta_k$. The cell $c_0$ multiplies both surviving terms and factors out, and the remaining $i$ is the one of the derivative, because $\int\frac{d^3p}{(2\pi)^3}\,\frac{p_k\sin\theta}{E_{\vec p}}=-\nabla_kF$. In the multipliers, where $-ic_k=L_{e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$, the same identity reads $[\psi^{\mathrm{fop}},\psi^{\mathrm{fop}\dagger}]=iR_{\vec e_x}^{\mathrm{axf}}(m+\sum_k L_{e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\nabla_k)F(\vec\Delta)$. For $m>0$ the kernel is $F(\vec\Delta)=\dfrac{m}{2\pi^2|\vec\Delta|}\,K_1\!\big(m|\vec\Delta|\big)$, the modified Bessel function of the second kind. The identity $\int_0^\infty\frac{p}{E}\sin(p\Delta)\,dp=mK_1(m\Delta)$ is the derivative in $\Delta$ of $\int_0^\infty\frac{\cos(p\Delta)}{E}\,dp=K_0(m\Delta)$, and both were checked numerically for $m=1$ and $\Delta=0.5,2,5,10$ to eleven digits. The kernel is nonzero for **every** $\vec\Delta\ne 0$; it decays exponentially for large separations, but it does not vanish. So at equal times and spatial separation $\vec\Delta\ne 0$ — a spacelike separation — the commutator of the spin-$\tfrac12$ field is nonzero, while the anticommutator is zero. The Bose choice fails microcausality for a half-integer-spin field.

The two-sided structure has a compact covariant form. The gradient and its quaternion conjugate are

$$
\tilde\nabla=e_t\frac{\partial}{\partial Q_t}+\vec e_x\frac{\partial}{\partial Q_x}+\vec e_y\frac{\partial}{\partial Q_y}+\vec e_z\frac{\partial}{\partial Q_z},\qquad
\tilde\nabla^{\natural}=e_t\frac{\partial}{\partial Q_t}-\vec e_x\frac{\partial}{\partial Q_x}-\vec e_y\frac{\partial}{\partial Q_y}-\vec e_z\frac{\partial}{\partial Q_z},
$$

with $\tilde\nabla\tilde\nabla^{\natural}=\tilde\nabla^{\natural}\tilde\nabla=\Box$, and the mass couples the two chiralities through the pair

$$
\tilde\nabla\tilde\Psi_R=m\tilde\Psi_L,
$$

with $\tilde\Psi_R$ the right-handed chiral half, and

$$
\tilde\nabla^{\natural}\tilde\Psi_L=m\tilde\Psi_R,
$$

with $\tilde\Psi_L$ the left-handed half. The two are the two Dirac equations of the framework, one per chirality, and each is a one-sided action: the first is the left action of the gradient on the right-handed half, the second the left action of its conjugate on the left-handed half. They are displayed separately because they act on different objects: one equation per chirality, both from the left, and the conjugate gradient $\natural$ is what separates them. Together they are the pair operator $\mathbb{D}$ acting on $(\tilde\Psi_R,\tilde\Psi_L)$, with $\mathbb{D}^2=\Box$, and the mass is the off-diagonal coupling of the two halves rather than a term inside either. With the field quantized by anticommutators, the general two-point functions are

$$
\{\psi^{\mathrm{fop}}(x),\psi^{\mathrm{fop}\dagger}(y)iR_{\vec e_x}^{\mathrm{axf}}\}=(\mathbb{D}+m)\,\Delta_{\mathrm{A}}(x-y),
\qquad
\langle0|[\psi^{\mathrm{fop}}(x),\psi^{\mathrm{fop}\dagger}(y)iR_{\vec e_x}^{\mathrm{axf}}]|0\rangle=(\mathbb{D}+m)\,G_{\mathrm{S}}(x-y),
$$

where $\Delta_{\mathrm{A}}$ is the antisymmetric combination of the two branch phases — the Pauli–Jordan-type kernel, supported inside the light cone and vanishing for spacelike separation — and $G_{\mathrm{S}}$ is the symmetric combination, which does not vanish there. The anticommutator is a $c$-number and equals its own vacuum expectation; under anticommutation relations the commutator is not a $c$-number, and the second identity is its vacuum expectation, whose $c$-number part is what carries $G_{\mathrm{S}}$. The anticommutator inherits the vanishing of $\Delta_{\mathrm{A}}$; the commutator's vacuum expectation inherits the non-vanishing of $G_{\mathrm{S}}$. At equal times these reduce to the delta and to the Bessel kernel computed above. The exact normalizations of $\Delta_{\mathrm{A}}$ and $G_{\mathrm{S}}$ carry the conventional factor of $i$; the covariant form is the standard textbook identity and is recorded as such, and the equal-time form is what was recomputed here.

## The Energy and the Norm

The third ingredient is positivity, and it is where the finite algebra has a native statement. With the mode expansion, the Hamiltonian of the free spinor field is

$$
H=\sum_r\int\!\frac{d^3p}{(2\pi)^3}\,E_{\vec p}\,
\big(a^{\mathrm{fop}\dagger}_ra^{\mathrm{fop}}_r-b^{\mathrm{fop}}_rb^{\mathrm{fop}\dagger}_r\big).
$$

The sign of the antiparticle term is decided by the bracket. With the **Fermi choice**, $b^{\mathrm{fop}}b^{\mathrm{fop}\dagger}=1-b^{\mathrm{fop}\dagger}b^{\mathrm{fop}}$, so after normal ordering

$$
H=\sum_r\int\!\frac{d^3p}{(2\pi)^3}\,E_{\vec p}\,
\big(a^{\mathrm{fop}\dagger}_ra^{\mathrm{fop}}_r+b^{\mathrm{fop}\dagger}_rb^{\mathrm{fop}}_r\big)+E_0,
$$

which is non-negative on the Fock space up to the c-number $E_0$ that normal ordering removes. With the **Bose choice**, $b^{\mathrm{fop}}b^{\mathrm{fop}\dagger}=1+b^{\mathrm{fop}\dagger}b^{\mathrm{fop}}$, and the antiparticle contribution enters with the opposite sign, $a^{\mathrm{fop}\dagger}a^{\mathrm{fop}}-b^{\mathrm{fop}\dagger}b^{\mathrm{fop}}$: the energy is unbounded below as antiparticle number grows, and the vacuum is unstable. The same sign appears in the norm: the anticommutator gives the positive-definite fermionic Fock space, the commutator gives an indefinite metric. This is the parent quantization article's argument, and it is stated here because it is half of the theorem's force.

The finite algebra shows the same identity in miniature. The single fermionic mode satisfies $\vec\Upsilon_x\vec\Upsilon_y=e_t-\vec\Upsilon_y\vec\Upsilon_x$, so the normal-ordered Hamiltonian of one mode is $\hbar\omega\,\vec\Upsilon_y\vec\Upsilon_x\ge 0$ on the module, with spectrum $\{0,\hbar\omega\}$ because $\tilde\Pi_-$ is an idempotent. Its would-be bosonic partner would need $\vec\Upsilon_x\vec\Upsilon_y=e_t+\vec\Upsilon_y\vec\Upsilon_x$, i.e. $[\vec\Upsilon_x,\vec\Upsilon_y]=e_t$, which the trace identity excludes. The positivity of the energy and the fermionic bracket are the same statement about the sign in $\vec\Upsilon_x\vec\Upsilon_y=e_t\mp\vec\Upsilon_y\vec\Upsilon_x$.

## The Four Quantizations

Collecting the two spin classes and the two brackets, four pairings are possible, and the theorem is the statement that two of them fail.

| Spin class | Bracket | Representation of the cover | Outcome |
|---|---|---|---|
| Integer | Commutator | descends, $-e_t\mapsto+1$ | consistent: scalar field, Maxwell field |
| Half-integer | Anticommutator | genuine spin rep, $-e_t\mapsto-1$ | consistent: Dirac field, positive norm, bounded energy |
| Half-integer | Commutator | genuine spin rep | fails microcausality (Bessel kernel above) and has unbounded energy |
| Integer | Anticommutator | descends | fails microcausality: the field itself is an observable, so its **commutator** must vanish at spacelike separation, but under anticommutation relations the commutator is no longer the $c$-number antisymmetric (Pauli–Jordan) kernel and does not vanish |

The integer-spin row is the parents' integer-spin case. The biquaternion Maxwell field lives in $\mathbb{M}_-$, the vector representation, on which $-e_t$ acts trivially, and its canonical quantization uses commutators; the scalar (Klein–Gordon) field has a commutator equal to the antisymmetric Pauli–Jordan kernel, which vanishes for spacelike separation, while its symmetric kernel does not. The half-integer rows are the spinor-module case computed above. The two surviving pairings are precisely the two inequivalent structures the algebra carries: the double-valued module paired with anticommutators, and the single-valued material-sector representation paired with commutators.

The table also displays what the framework does and does not explain. The *spin class* column is algebraic: integer versus half-integer is the descent condition for the rotor action, and the $2\pi$ sign is the action of $-e_t$, both recomputed in $\mathbb{B}$. The *bracket* column is transcribed from field theory; the algebra does not, at the level developed here, force the pairing. And the two columns are tied together only through the theorem, which is why the one-mode coincidence of *The Algebra's Own One Fermionic Mode* is suggestive but not decisive: it exhibits one entry of the table — half-integer spin, anticommutator — inside $\mathbb{B}$, and says nothing about the other three.

## What the Framework Establishes and What It Only Transcribes

**Established, and recomputed.**

- The rotor group of unit real quaternions is the double cover of the rotation group; the rotor through $2\pi$ about any axis is $-e_t$, and through $4\pi$ is $e_t$.
- Under the rotor action, the half-integer-spin representations live on the odd tensor powers of the spinor module, where $-e_t$ acts as $(-1)^{2s}=-1$, while the integer-spin representations live on the material sector $\mathbb{M}_-$ and on the even tensor powers, where $-e_t$ acts as $+1$. The algebra affords $s=\tfrac12$ as a module, $s=0$ on the centre under conjugation, and $s=1$ through the adjoint action on the three vector units $\vec e_k$, the spatial part of $\mathbb{M}_-$.
- The single-mode ladder operators are the spin ladder operators, $\vec\Upsilon_x=\tilde S_+/\hbar$, and satisfy $\{\vec\Upsilon_x,\vec\Upsilon_y\}=e_t$; the number operator is the idempotent $\tilde\Pi_-$; and the fermion-parity grading is the inner automorphism by $(-1)^F=i\vec e_z=2\tilde S_z/\hbar$, an element of $\mathbb{M}_+$.
- No bosonic mode exists in $\mathbb{B}$. The target relation $[\vec\Upsilon_x,\vec\Upsilon_y]=e_t$ has $\operatorname{Tr}_2=2$, while the trace of any commutator is $0$; and the computed commutator $i\vec e_z$ is not central, so no rescaling of it can produce a central value either.
- For the free spin-$\tfrac12$ field built on the module, the equal-time anticommutator is $\delta_{ab}\delta^{(3)}(\vec\Delta)$ and the equal-time commutator is a nonzero Bessel kernel at every $\vec\Delta\ne 0$. The spinorial part of the anticommutator, $2\cos\theta\,c_0\sum_k c_kp_k$, is odd in $\vec p$ and cancels, while the scalar term is even and survives.
- The sign in $\vec\Upsilon_x\vec\Upsilon_y=e_t\mp\vec\Upsilon_y\vec\Upsilon_x$ is the sign of the antiparticle term in the Hamiltonian and the sign that decides positivity of the norm.

**Transcribed, not derived.**

- That the bracket is *forced* by the conjunction of locality, positivity and Lorentz invariance. The article exhibits the failure of the wrong choices; it does not prove that no other structure evades it.
- The covariant identities $\{\psi^{\mathrm{fop}},\psi^{\mathrm{fop}\dagger}iR_{\vec e_x}^{\mathrm{axf}}\}=(\mathbb{D}+m)\Delta_{\mathrm{A}}$ and $[\psi^{\mathrm{fop}},\psi^{\mathrm{fop}\dagger}iR_{\vec e_x}^{\mathrm{axf}}]=(\mathbb{D}+m)G_{\mathrm{S}}$, and the Pauli–Jordan-type and symmetric kernels.
- The scalar-field and Maxwell-field contrast, and the standard microcausality argument for integer spin.

**Gap, left visible.**

- The framework does not *derive* spin–statistics. The spin dichotomy is algebraic; the bracket pairing is imposed. The one-mode coincidence that relates the spin ladder to the fermionic mode is exact but finite-dimensional, and the field algebra is infinite-dimensional, where both the exterior and the symmetric algebra are available on the same footing.
- Higher spin is not algebraic in the same sense. The $s=1$ representation is the adjoint action, not a module, and higher spins need tensor products; whether the framework's integer-spin structure has a native quantization of its own is not established here.

## Open Questions

**1. Does the framework derive spin–statistics or only transcribe it?** The central question. The spin dichotomy is algebraic and the $2\pi$ sign is an element of the algebra; the bracket pairing is imported. The single-mode realization is the only place where the two meet inside $\mathbb{B}$, and it is finite-dimensional. Whether some structure of the algebra — a graded extension, a crossed product, or the full tensor algebra of the module — forces the pairing is open and is not decided here.

**2. Is the one-mode coincidence structural or dimensional?** The four elements $e_t,\vec\Upsilon_x,\vec\Upsilon_y,\vec\Upsilon_x\vec\Upsilon_y$ span $\mathbb{B}$, so the single fermionic mode fits exactly, and the same element that is the spin ladder is the fermionic mode ladder. Is this a reflection of the spin-$\tfrac12$ structure of the module, or a coincidence of dimensions? The article's honest answer is that it is a coincidence until something more is said.

**3. What is the grading for a field?** The single-mode parity $(-1)^F=i\vec e_z$ is an element of $\mathbb{B}$; the field grading is not, by the dimension count, and the KMS article's requirement of a $\mathbb{Z}/2$ grading on the field algebra stands. Can an extension of $\mathbb{B}$ carry it, and does that extension have a biquaternion interpretation?

**4. Integer-spin quantization in the algebra.** The vector representation appears through the adjoint action on the vector units, and its quantization is standard and imported. Is there a native construction of the integer-spin Fock space from the algebra that mirrors the single-mode fermionic one, and if not, what obstructs it beyond the trace identity?

**5. The massless limit and chirality.** The microcausality failure of the commutator was computed at $m>0$, where the surviving kernel is the Bessel function $K_1$. As $m\to 0$ the kernel becomes $1/(2\pi^2|\vec\Delta|^2)$ and still does not vanish, so the massless case is not qualitatively different. At $m=0$ the chiral pair decouples into the two Weyl equations $\tilde\nabla\tilde\Psi_R=0$ and $\tilde\nabla^{\natural}\tilde\Psi_L=0$, each carrying one helicity; how the two-sided structure and the helicity–chirality locking enter the theorem is not developed here.

**6. Empirical content.** The construction reproduces standard field theory. Any deviation would have to appear where the algebra is used beyond transcription — for example in a modification of the one-mode identification or in the coupling to the material sector; none is visible at the level developed here.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The bracket is the frame, on the generators as on the metric, $\gamma_\mu[\mathbb{M}_-]$ or $\gamma_\mu[\mathbb{B}]$, so that a glyph names a display and not an object of the algebra.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})\cong M_4(\mathbb{C})$, not a different algebra, and this section is the only place where they are named: in the body the cells do the work, and the five symbols below are the same five objects.

### The Frame

With $L_a\psi=a\psi$ and $R_b\psi=\psi b$ the left and right multiplications, and with $c(M)$ the coefficient matrix of $M$ in the basis of the sixteen products,

$$
\gamma_0[\mathbb{M}_-]=c_0=iR_{\vec e_x}^{\mathrm{pau}},\qquad
\gamma_k[\mathbb{M}_-]=c_k=iL_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\qquad
\gamma_5[\mathbb{M}_-]=c_5=-iR_{\vec e_z}^{\mathrm{pau}},
$$

The same in the axis-free display:

$$
\gamma_0[\mathbb{M}_-]=c_0=iR_{\vec e_x}^{\mathrm{axf}},\qquad
\gamma_k[\mathbb{M}_-]=c_k=iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\qquad
\gamma_5[\mathbb{M}_-]=c_5=-iR_{\vec e_z}^{\mathrm{axf}},
$$

with $c_5$ the fifth cell, the one that anticommutes with the four and squares to $+I_4$. A single product is a pure tensor; the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four, with $\ell(M)=\operatorname{rank}c(M)$.

### The Chirality

$\gamma_5[\mathbb{M}_-]$ is the reference-frame cell of the chirality operator; the central grading $\chi=i\tilde\Xi_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$ — is a different object, represented by $\gamma_5[\mathbb{M}_-]$ on the Dirac module.

### The Real Forms

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

### The Identities

In the $\gamma$ reading, with $\epsilon_{0123}=+1$,
$$
\{\gamma_\mu[\mathbb{M}_-],\gamma_\nu[\mathbb{M}_-]\}=2\varepsilon_\mu\delta_{\mu\nu}I_4,\qquad
(\gamma_k[\mathbb{M}_-])^2=-I_4,\qquad
\gamma_5[\mathbb{M}_-]^2=I_4,\qquad
\{\gamma_\mu[\mathbb{M}_-],\gamma_5[\mathbb{M}_-]\}=0\ (\mu=0,1,2,3),
$$
$$
[\gamma_\mu[\mathbb{M}_-],\gamma_\nu[\mathbb{M}_-]]=2\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-]\quad(\mu\ne\nu),\qquad
[\gamma_a[\mathbb{M}_-],S_{cd}]=\varepsilon_a\delta_{ac}\gamma_d[\mathbb{M}_-]-\varepsilon_a\delta_{ad}\gamma_c[\mathbb{M}_-],\qquad
S_{cd}=\tfrac14[\gamma_c[\mathbb{M}_-],\gamma_d[\mathbb{M}_-]],
$$
$$
\mathrm{tr}(\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-])=4\varepsilon_\mu\delta_{\mu\nu},\qquad
\mathrm{tr}(\gamma_5[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-]\gamma_\rho[\mathbb{M}_-]\gamma_\sigma[\mathbb{M}_-])=-4i\,\epsilon_{\mu\nu\rho\sigma},
$$
$$
\mathrm{tr}(\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-]\gamma_\rho[\mathbb{M}_-]\gamma_\sigma[\mathbb{M}_-])
=4\bigl(\varepsilon_\mu\delta_{\mu\nu}\varepsilon_\rho\delta_{\rho\sigma}-\varepsilon_\mu\delta_{\mu\rho}\varepsilon_\nu\delta_{\nu\sigma}+\varepsilon_\mu\delta_{\mu\sigma}\varepsilon_\nu\delta_{\nu\rho}\bigr).
$$

### The Contraction Sums

The sums below contract a product with the four cells, and their values are frame statements, because each term is fixed by the square of a cell. In the Euclidean frame, where every cell squares to $+I_4$,

$$
\sum_\mu\gamma_\mu[\mathbb{B}]\gamma_\mu[\mathbb{B}]=4I_4,\qquad
\sum_\mu\gamma_\mu[\mathbb{B}]\gamma_\alpha[\mathbb{B}]\gamma_\mu[\mathbb{B}]=-2\gamma_\alpha[\mathbb{B}],
$$

$$
\sum_\mu\gamma_\mu[\mathbb{B}]\gamma_\alpha[\mathbb{B}]\gamma_\beta[\mathbb{B}]\gamma_\mu[\mathbb{B}]=4\delta_{\alpha\beta}I_4,\qquad
\sum_\mu\gamma_\mu[\mathbb{B}]\gamma_\delta[\mathbb{B}]\gamma_\beta[\mathbb{B}]\gamma_\alpha[\mathbb{B}]\gamma_\mu[\mathbb{B}]=-2\gamma_\alpha[\mathbb{B}]\gamma_\beta[\mathbb{B}]\gamma_\delta[\mathbb{B}] .
$$

The first three are one rule: a pure $k$-vector picks up $(-1)^k(4-2k)$, that is $+4$, $-2$, $0$ for $k=0,1,2$. At $k=2$ the coefficient vanishes when $\alpha\ne\beta$, and only $\alpha=\beta$ survives, where $\gamma_\alpha[\mathbb{M}_-]\gamma_\beta[\mathbb{M}_-]=I_4$ is a scalar and takes the $k=0$ coefficient, which is the $4\delta_{\alpha\beta}$ of the third line. The fourth sum is the $k=3$ case, and its indices come back reversed: the result is $-2\gamma_\alpha[\mathbb{M}_-]\gamma_\beta[\mathbb{M}_-]\gamma_\delta[\mathbb{M}_-]$, not $-2$ times the product in the order it was written. For three distinct indices the reversal costs one sign, and the sum is $+2\gamma_\delta[\mathbb{M}_-]\gamma_\beta[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]$, the form in which the identity is usually quoted; the exact form is the one displayed.

In the frame of the cells themselves, where $c_0$ squares to $+I_4$ and $c_k$ to $-I_4$, only the first two keep a closed form. The first stays scalar, $\sum_\mu\gamma_\mu[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]=-2I_4$. The second picks up the metric factor, $\sum_\mu\gamma_\mu[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]=2(g_{\alpha\alpha}+1)\gamma_\alpha[\mathbb{M}_-]$, which is $4\gamma_0[\mathbb{M}_-]$ for the time index and $0$ for a spatial one. The third is no longer proportional to $\delta_{\alpha\beta}I_4$: for $\alpha\ne\beta$ it does not vanish. The fourth is no longer $-2\gamma_\alpha[\mathbb{M}_-]\gamma_\beta[\mathbb{M}_-]\gamma_\delta[\mathbb{M}_-]$; the metric enters term by term.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{e_\mu}^{\mathrm{axf}}=C_{\Pi}L_{e_\mu}^{\mathrm{pau}}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

The spin–statistics theorem pairs half-integer spin with anticommutators and integer spin with commutators. In the biquaternion framework the spin half of the theorem is algebraic and exact: the rotor group of unit real quaternions is the double cover of the rotation group, the rotor through $2\pi$ is $-e_t$, half-integer-spin representations live on the odd tensor powers of the spinor module, where $-e_t$ acts as $-\mathrm{id}$, and integer-spin representations live on the material sector $\mathbb{M}_-$ and on the even tensor powers, where it acts as $+\mathrm{id}$. The framework's finite algebra also contains one fermionic mode, whose ladder operators are the spin ladder operators, $\vec\Upsilon_x=\tilde S_+/\hbar$, and whose parity grading is the Hermitian element $(-1)^F=i\vec e_z=2\tilde S_z/\hbar$; no bosonic mode exists, because a canonical commutator would be central and traceless.

The statistics half is transcribed with the parents' field. For the free spin-$\tfrac12$ field, the equal-time anticommutator is $\delta_{ab}\delta^{(3)}(\vec\Delta)$, the spinorial term $2\cos\theta\,c_0\sum_k c_kp_k$ cancelling as an odd function of $\vec p$; the equal-time commutator, by contrast, leaves the Bessel kernel $c_0(m-i\sum_k c_k\nabla_k)F(\vec\Delta)$ and fails to vanish at any spatial separation. The same sign that selects the anticommutator selects the positive sign in $\vec\Upsilon_x\vec\Upsilon_y=e_t-\vec\Upsilon_y\vec\Upsilon_x$, and hence a bounded Hamiltonian and a positive-definite norm.

What the framework establishes is that the two pairings which survive the theorem are the two inequivalent structures the algebra actually carries, and that the $2\pi$ sign which distinguishes them is an element of the algebra. What it does not establish is that the algebra forces the pairing; spin–statistics is exhibited in biquaternionic form, not derived from it. The one-mode coincidence is the visible edge of the question, and it is left as the article's central open problem.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_k^2=-e_t$, $\vec e_j \vec e_k=\epsilon_{jkl}\vec e_l$ $(j\ne k)$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\mathbb{M}_-,\mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{H}_{\mathbb{B}}$, $\mathbb{C}_{\mathbb{B}}$ | Real-quaternion subspace; centre $\mathbb{C}e_t$ |
| $\mathsf{M}_2(\vec e_k)=-i\sigma_k$, $\mathsf{M}_2(i\vec e_k)=\sigma_k$, $k=x,y,z$ | Isomorphism with $M_2(\mathbb{C})$; $\sigma_k$ are the three Pauli matrices |
| $\operatorname{Tr}_2(\tilde Q_1\tilde Q_2)=2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2) = 2\langle\tilde Q_1,\tilde Q_2\rangle$ | Trace reading of the plain form on the informational sector; $\operatorname{Tr}_2$ is the $2\times2$ trace, the $4\times4$ one being four times the scalar part |
| $\tilde u(\theta,\vec u)=\cos\tfrac{\theta}{2}e_t+\sin\tfrac{\theta}{2}\sum_k \vec u_k\vec e_k$ | Rotation rotor (unit real quaternion), $\vec u$ the unit axis |
| $\tilde u(2\pi,\vec u)=-e_t$, $\tilde u(4\pi,\vec u)=e_t$ | The two-valued sign of the spinor module |
| $\tilde S_k=\tfrac{\hbar}{2}i\vec e_k$, $\tilde S_\pm=\tfrac{\hbar}{2}(i\vec e_x\mp \vec e_y)$ | Spin operators in $\mathbb{M}_+$ ($k=x,y,z$); ladders in $\mathbb{B}$ (they are not Hermitian) |
| $\vec\Upsilon_x=\tfrac12(i\vec e_x-\vec e_y)=\tilde S_+/\hbar$, $\vec\Upsilon_y=\tilde S_-/\hbar$ | Single fermionic mode ladder |
| $\tilde\Pi_-=\vec\Upsilon_y\vec\Upsilon_x=\tfrac12(e_t-i\vec e_z)$ | Single-mode number operator (idempotent) |
| $(-1)^F=i\vec e_z=e_t-2\tilde\Pi_-=2\tilde S_z/\hbar$ | Fermion parity; Hermitian involution in $\mathbb{M}_+$ |
| $\{\vec\Upsilon_x,\vec\Upsilon_y\}=e_t$, $[\vec\Upsilon_x,\vec\Upsilon_y]=i\vec e_z$ | Fermionic mode relation; failure of the bosonic relation |
| $c_0=iR_{\vec e_x}^{\mathrm{axf}}$, $c_k=iL_{e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$, $c_5=-iR_{\vec e_z}^{\mathrm{axf}}$, $L_aR_b\psi=a\psi b$ | Cells of the reference frame, $L_aL_b=L_{ab}$, $R_aR_b=R_{ba}$; $\{c_\mu,c_\nu\}=2\varepsilon_\mu\delta_{\mu\nu}I_4$ for each pair, $\varepsilon=(1,-1,-1,-1)$ |
| $\slashed p=c_0p_0-\sum_kc_kp_k$, $i(c_0\nabla_t+\sum_kc_k\nabla_k)\psi=m\psi$ | Momentum cell and field equation; on a plane wave $\slashed pw=mw$, $(\slashed p+m)v=0$ |
| $\nabla_k=\partial/\partial\Delta_k$ | Gradient with respect to the spatial separation |
| $\psi^{\mathrm{fop}}$, $\psi^{\mathrm{fop}\dagger}iR_{\vec e_x}^{\mathrm{axf}}=\psi^{\mathrm{fop}\dagger}\,iR_{\vec e_x}^{\mathrm{axf}}$ | Quantized spinor-module field and its Dirac adjoint |
| $a^{\mathrm{fop}}_r(\vec p),b^{\mathrm{fop}\dagger}_r(\vec p)$ | Annihilation and antiparticle creation operators |
| $w^{(r)}(\vec p),v^{(r)}(\vec p)$ | Positive- and negative-frequency spinors (from the parents) |
| $\sum_r w^{(r)}\bar w^{(r)}=E_{\vec p}c_0-\sum_k p_kc_k+m$, $\sum_r v^{(r)}\bar v^{(r)}=E_{\vec p}c_0-\sum_k p_kc_k-m$ | Spin sums; multiplied on the right by $c_0$ they give $E_{\vec p}I_4+m\,c_0+c_0\sum_k c_kp_k$ for $w$ and the same with $-m\,c_0$ for $v$ |
| $\theta=\vec p\cdot\vec\Delta$, $\vec\Delta=\vec x-\vec y$, $\vec x=x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$ | Phase and spatial separation in the equal-time brackets |
| $\{\psi^{\mathrm{fop}}_a,{\psi^{\mathrm{fop}}_b}^\dagger\}=\delta_{ab}\delta^{(3)}(\vec\Delta)$ | Local equal-time anticommutator |
| $[\psi^{\mathrm{fop}},\psi^{\mathrm{fop}\dagger}]=c_0(m-i\sum_k c_k\nabla_k)F(\vec\Delta)$ | Nonlocal equal-time commutator |
| $F(\vec\Delta)=\frac{m}{2\pi^2|\vec\Delta|}K_1(m|\vec\Delta|)$ | Surviving commutator kernel ($m>0$) |
| $\Delta_{\mathrm{A}}(x-y)$, $G_{\mathrm{S}}(x-y)$ | Antisymmetric (Pauli–Jordan-type) and symmetric two-point kernels |
| $H=\sum_r\int\frac{d^3p}{(2\pi)^3}E_{\vec p}(a^{\mathrm{fop}\dagger}_ra^{\mathrm{fop}}_r+b^{\mathrm{fop}\dagger}_rb^{\mathrm{fop}}_r)+E_0$ | Normal-ordered Hamiltonian (Fermi choice) |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle$ | the general plain bilinear form, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2)$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{*})$; on the diagonal $\langle\tilde{Q}_1,\tilde{Q}_1\rangle_{*}=\sum_\mu\lvert Q_{1\mu}\rvert^{2}$ |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- W. Pauli, "The Connection Between Spin and Statistics," *Physical Review* **58** (1940) 716–722, for the original theorem and the positivity argument.
- M. Fierz, "Über die relativistische Theorie kräftefreier Teilchen mit beliebigem Spin," *Helvetica Physica Acta* **12** (1939) 3–37, for the antecedent representation-theoretic analysis.
- G. Lüders and B. Zumino, "Connection between Spin and Statistics," *Physical Review* **110** (1958) 1450–1453, for the general proof in the axiomatic setting.
- R. F. Streater and A. S. Wightman, *PCT, Spin and Statistics, and All That* (Benjamin, 1964), for the Wightman-axiomatic treatment and the locality–positivity hypotheses.
- R. Haag, *Local Quantum Physics* (2nd ed., Springer, 1996), for the algebraic formulation and the role of the grading.
- S. Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), and M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the standard equal-time and covariant two-point functions used here.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Fields* (McGraw–Hill, 1965), for the spin sums, the Pauli–Jordan function and the microcausality computation.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the Clifford-algebra origin of the spin group and its double cover.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the rotor realization of rotations and its two-valuedness.
- Companion articles: [Canonical Quantization of the Biquaternion Dirac Field](canonical-quantization-of-the-biquaternion-dirac-field.html); [Fock Space and Creation/Annihilation Operators in Biquaternionic Form](fock-space-and-creation-annihilation-operators-in-biquaternionic-form.html); [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html); [Angular Momentum and Spin in Biquaternionic Form](angular-momentum-and-spin-in-biquaternionic-form.html); [The Lorentz Group in Biquaternionic Form — Structure and Representations](the-lorentz-group-in-biquaternionic-form-structure-and-representations.html); [The Spinor Module in Biquaternionic Form and Its Lorentz Action](the-spinor-module-in-biquaternionic-form-and-its-lorentz-action.html); [The Spinor Representation of the Lorentz Group in Biquaternionic Form](the-spinor-representation-of-the-lorentz-group-in-biquaternionic-form.html); [The KMS Condition and the Biquaternion Framework](the-kms-condition-and-the-biquaternion-framework.html); [Canonical Quantization of the Biquaternion Maxwell Field](canonical-quantization-of-the-biquaternion-maxwell-field.html); [The Klein–Gordon Equation in Biquaternionic Form](the-klein-gordon-equation-in-biquaternionic-form.html).
