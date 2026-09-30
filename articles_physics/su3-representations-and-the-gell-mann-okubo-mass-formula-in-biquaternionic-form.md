# __SU(3) Representations and the Gell-Mann–Okubo Mass Formula in Biquaternionic Form__

## Introduction

This article records the $\mathrm{SU}(3)$ representation theory and the mass splitting that the spinor-structure programme uses to organise the hadron spectrum: the irreducible representations as traceless bisymmetric tensors of degree $N(p,q)$, the Okubo basis of $\mathfrak{su}(3)$ with its three $\mathfrak{su}(2)$ subalgebras, the condition that selects the "admissible" hadron supermultiplets, the reduction of the octet into isospin multiplets, and the Gell-Mann–Okubo mass formula with its Zeeman-effect reading.

It is recorded with an explicit standing, stated at the outset so that it is not misread as a framework result. The companion *The Gauge Group Ceiling* shows that the biquaternion algebra's compact structure reaches $\mathrm{SU}(2)$ and stops, and *The Gluon: An Octet Outside the Biquaternion Algebra* states the boundary. The $\mathrm{SU}(3)$ structure below is therefore **not an algebra of $\mathbb{B}$**. It is the external machinery by which the hadron spectrum is classified, and it appears in the corpus because the spinor-structure programme attaches it to the spinor structure through the spin–charge Hilbert space — the spin factor of that space is the framework's own, the charge factor is this external $\mathrm{SU}(3)$.

The article is organised as follows. A section gives the representations as traceless bisymmetric tensors and the degree formula. A section fixes the Okubo basis and the three $\mathfrak{su}(2)$ subalgebras. A section states the admissibility condition and lists the allowed degrees. A section reduces the octet into isospin multiplets. A section derives and then checks the Gell-Mann–Okubo mass formula. A closing section states the biquaternion reading.

**Conventions.** The Okubo basis and the degree formula are transcribed from the spinor-structure programme (V. V. Varlamov, arXiv:1409.1400, §§4–6) and from Okubo's *Lecture Notes in Physics* **94**; the mass relations are the standard Gell-Mann–Okubo relations and are checked against the Particle Data Group values. The companion *The Spin–Charge Hilbert Space and the SU(3) Supermultiplets in Biquaternionic Form* supplies the space on which these representations act, and *The Spin–Mass Formula and the Spectrum of Elementary Particles in Biquaternionic Form* supplies the mass $m_0$ of a supermultiplet.

- Companion article *The Spin–Charge Hilbert Space and the SU(3) Supermultiplets in Biquaternionic Form*, for the space $\mathcal{H}_S\otimes\mathcal{H}_Q\otimes\mathcal{H}_\infty$ on which these representations act.
- Companion article *The Spin–Mass Formula and the Spectrum of Elementary Particles in Biquaternionic Form*, for the mass $m_0$ of the supermultiplet and the representation degrees on the spin lines.
- Companion articles *The Gauge Group Ceiling: Why the Biquaternion Algebra Reaches SU(2) but Not SU(3)* and *The Gluon: An Octet Outside the Biquaternion Algebra*, for why $\mathrm{SU}(3)$ is external.
- Corpus article *The Pion and the Chiral Lagrangian in Biquaternionic Form*, for the octet's scalar sector and the Gell-Mann–Oakes–Renner relation, a different mass formula.
- Corpus article *The CKM Matrix and CP Violation in Biquaternionic Form*, for the flavour-factor reading of the mixing that $\mathrm{SU}(3)$ does not carry.

## Representations of SU(3)

An irreducible representation of $\mathrm{SU}(3)$ is carried by a **traceless bisymmetric tensor** $T^{a_1\dots a_p}_{b_1\dots b_q}$, symmetric in the upper and in the lower indices and traceless on any contraction. The pair $(p,q)$ of non-negative integers labels the representation, and its **degree** is

$$
N(p,q) = \tfrac12\,(p+1)(q+1)(p+q+2).
$$

### The Degree Table

The degree counts the particles in the supermultiplet the representation carries. The lower-left corner of the table is

| $N(p,q)$ | $q=0$ | $q=1$ | $q=2$ | $q=3$ | $q=4$ | $q=5$ | $q=6$ |
|---|---|---|---|---|---|---|---|
| $p=0$ | $1$ | $3$ | $6$ | $10$ | $15$ | $21$ | $28$ |
| $p=1$ | $3$ | $8$ | $15$ | $24$ | $35$ | $48$ | $63$ |
| $p=2$ | $6$ | $15$ | $27$ | $42$ | $60$ | $81$ | $105$ |
| $p=3$ | $10$ | $24$ | $42$ | $64$ | $90$ | $120$ | $154$ |
| $p=4$ | $15$ | $35$ | $60$ | $90$ | $125$ | $165$ | $210$ |
| $p=5$ | $21$ | $48$ | $81$ | $120$ | $165$ | $216$ | $273$ |
| $p=6$ | $28$ | $63$ | $105$ | $154$ | $210$ | $273$ | $343$ |

The singlet is $(0,0)$, degree $1$; the fundamental triplet is $(1,0)$, degree $3$, and its conjugate $(0,1)$, also $3$; the adjoint (the **octet**) is $(1,1)$, degree $8$; the decuplet is $(3,0)$, degree $10$; the $(2,2)$ is the $27$. These are the degrees the programme's particle assignments use.

## The Okubo Basis and the Three SU(2) Subalgebras

To fix a subalgebra $\mathfrak{su}(2)\subset\mathfrak{su}(3)$ it is convenient to use Okubo's basis $A^{i}_{\ k}$ ($i,k=1,2,3$) of $\mathfrak{su}(3)$, with

$$
A^{1}_{\ 1}=\mathrm{diag}\bigl(\tfrac23,-\tfrac13,-\tfrac13\bigr),\quad
A^{2}_{\ 2}=\mathrm{diag}\bigl(-\tfrac13,\tfrac23,-\tfrac13\bigr),\quad
A^{3}_{\ 3}=\mathrm{diag}\bigl(-\tfrac13,-\tfrac13,\tfrac23\bigr),
$$

the off-diagonal units $A^{i}_{\ k}$ ($i\ne k$) carrying one unit entry, and $A^{1}_{\ 1}+A^{2}_{\ 2}+A^{3}_{\ 3}=0$. The commutation relations are

$$
\bigl[A^{i}_{\ k},A^{l}_{\ m}\bigr] = \delta^{i}_{\ m}A^{l}_{\ k}-\delta^{l}_{\ k}A^{i}_{\ m}.
$$

This basis makes the three $\mathfrak{su}(2)$ subalgebras transparent. Projecting with a fixed index gives

$$
a^{i}_{\ j} = A^{i}_{\ j}-\tfrac12\delta^{i}_{\ j}A^{k}_{\ k},
$$

whose units satisfy the $\mathfrak{su}(2)$ relations, so **I-spin** is $\mathfrak{su}(2)$ in the $(1,2)$ plane. The rank of $\mathfrak{su}(3)$ is two, so any Cartan operator is a combination of $A^{1}_{\ 1}$ and $A^{3}_{\ 3}$, and the three choices of which $\mathfrak{su}(2)$ to single out give the three spins

$$
I_3 = A^{1}_{\ 1}+\tfrac12 A^{3}_{\ 3},
\qquad
U_3 = A^{3}_{\ 3}+\tfrac12 A^{1}_{\ 1},
\qquad
V_3 = A^{1}_{\ 1}+\tfrac12 A^{2}_{\ 2},
$$

the **I-spin**, **U-spin** and **V-spin** of the eightfold way. A charge operator on a representation of degree $N$ then has the form

$$
Q^{(N)} = \alpha\,A^{1}_{\ 1}(N)+\beta\,A^{3}_{\ 3}(N)+\gamma\,\mathbf{1}_N,
$$

with the constant $\gamma$ a shift. The three subalgebras matter because different mass relations are statements in different ones: the Gell-Mann–Okubo relation is a U-spin statement, and the equal-spacing relation of the decuplet is an I-spin statement.

## Admissible Supermultiplets

Hadrons are classified into supermultiplets of equal baryon number, spin and parity, one supermultiplet per irreducible representation. A representation can carry hadrons only if the eigenvalues of the charge and hypercharge operators on it are integers. That selects the **admissible** representations

$$
p-q\equiv 0 \pmod 3,
$$

that is, $p-q\in\{0,\pm3,\pm6,\dots\}$. Reading the table above, the admissible degrees are

$$
1,\,8,\,10,\,27,\,28,\,35,\,55,\,64,\,80,\,81,\,91,\,125,\,136,\,143,\,154,\dots
$$

For example $N(0,0)=1$, $N(1,1)=8$, $N(3,0)=N(0,3)=10$, $N(2,2)=27$, $N(0,6)=N(6,0)=28$, $N(4,1)=N(1,4)=35$, $N(0,9)=55$, $N(1,7)=80$, $N(5,2)=81$, $N(3,3)=64$, $N(4,4)=125$, $N(3,6)=N(6,3)=154$; all satisfy $p-q\equiv0\pmod3$. The non-admissible degrees — $3$, $6$, $15$, $24$, $42$, $48$, $60$, $\dots$ — correspond to representations whose charge eigenvalues would be fractional, as the triplet $(1,0)$ and sextet $(2,0)$ illustrate: the quark and antiquark are the degrees of freedom, and their fractional charges are why the triplet is not an admissible hadron supermultiplet while the octet built from three of them is.

## Reduction of the Octet into Isospin Multiplets

### The Octet Reduction

The eightfold way's octets sit on the adjoint representation $(1,1)$. On the subgroup $\mathrm{SU}(2)\subset\mathrm{SU}(3)$ the adjoint representation is reducible, and its reduction is

$$
\mathrm{Sym}_0^{(1,1)} = \Phi_3\oplus\Phi_2\oplus\Phi_2^*\oplus\Phi_0,
$$

where $\Phi_3$ is an isospin **triplet**, $\Phi_2$ and $\Phi_2^*$ are a **doublet** and its conjugate, and $\Phi_0$ is a **singlet**: dimensions $3+2+2+1=8$. The baryon octet $F_{1/2}$ therefore reduces to

$$
\Phi_3=\{\Sigma^+,\Sigma^0,\Sigma^-\},\qquad
\Phi_2=\{p,n\},\qquad
\Phi_2^*=\{\Xi^-,\Xi^0\},\qquad
\Phi_0=\{\Lambda\},
$$

and the meson octets $B_0$ (spin $0$, negative parity) and $B_1$ (spin $1$, negative parity) reduce in the same pattern:

$$
\Phi_3=\{\pi^+,\pi^0,\pi^-\},\qquad
\Phi_2=\{K^-,K^0\},\qquad
\Phi_2^*=\{K^+,K^0\}\ \text{(conjugate)},\qquad
\Phi_0=\{\eta\},
$$

for $B_0$. The reduction is the representation-theoretic content behind "the eightfold way": the eight states of the octet fall into one triplet, two doublets and one singlet, and the two doublets are conjugate because they carry opposite hypercharge. The charge multiplet structure of the companion spin–charge article is this reduction, with each isospin multiplet carrying the charge values of its members.

## The Gell-Mann–Okubo Mass Formula

Within a supermultiplet the particles have different masses; the difference is the mass splitting, and $\mathrm{SU}(3)$ symmetry alone predicts its form. The programme's account follows the **Zeeman analogy**. In the atomic Zeeman effect the energy operator splits as $H=H_0+H_1$ with $H_1=d_{\alpha\beta}H^{\alpha\beta}$, a magnetic moment contracted with the field; the mass operator of a supermultiplet splits in the same way,

$$
m^2 = m_0^2+\delta m^2,
$$

where $m_0^2$ is $\mathrm{SU}(3)$-symmetric — proportional to the identity on the representation — and $\delta m^2 = D^{a}_{\ b}Z^{b}_{\ a}$ is a unitary moment $D$ contracted with a unitary field $Z$,

$$
D^{a}_{\ b} = \lambda\delta^{a}_{\ b}\mathbf{1}+\mu A^{a}_{\ b}+\nu A^{a}_{\ c}A^{c}_{\ b}+\dots,
$$

$$
Z = C\begin{pmatrix}\tfrac13&0&0\\0&\tfrac13&0\\0&0&-\tfrac23\end{pmatrix}
+C'\begin{pmatrix}\tfrac23&0&0\\0&-\tfrac13&0\\0&0&-\tfrac13\end{pmatrix},
\qquad |C'|\ll|C| .
$$

The first term of $Z$ splits the supermultiplet into I-multiplets of **different hypercharge** $Y$; the second, much smaller, splits the members **within** an I-multiplet by charge $Q$. Writing the two contributions as $\delta m^2=\xi A^{3}_{\ 3}+\eta A^{3}_{\ c}A^{c}_{\ 3}$ and $\delta m^{2\prime}=\xi'A^{1}_{\ 1}+\eta'A^{1}_{\ c}A^{c}_{\ 1}$ with $\xi'=\theta\xi$, $\eta'=\theta\eta$, $|\theta|\ll1$, and expressing them through the Casimir operators of $\mathrm{SU}(3)$ and $\mathrm{SU}(2)$, gives the **Gell-Mann–Okubo mass formula**

$$
m^2 = m_0^2+\alpha+\beta Y+\gamma\Bigl(I(I+1)-\tfrac14Y^2\Bigr)
+\alpha'+\beta'Y+\gamma'\Bigl(U(U+1)-\tfrac14Q^2\Bigr),
\qquad
\frac{\alpha'}{\alpha}=\frac{\beta'}{\beta}=\frac{\gamma'}{\gamma}=\theta .
$$

The prime terms are the charge splitting and the unprimed terms the hypercharge splitting; the ratio $\theta$ is the small parameter.

### The Linear Form

Since the charge splitting is small, the leading hypercharge splitting is

$$
m = m_0+\alpha+\beta Y+\gamma\Bigl(I(I+1)-\tfrac14 Y^2\Bigr),
$$

the **linear** Gell-Mann–Okubo formula, valid when $\delta m^2/m_0^2\ll1$.

### The Baryon Octet

For the baryon octet $F_{1/2}$ the hypercharge splitting gives the four masses

| multiplet | $I$ | $Y$ | $m_{\text{exp}}$ (MeV) | $m_{\text{th}}$ |
|---|---|---|---|---|
| $\Xi$ | $\tfrac12$ | $-1$ | $1318$ | $m_0+\alpha-\beta+\tfrac12\gamma$ |
| $\Sigma$ | $1$ | $0$ | $1192$ | $m_0+\alpha+2\gamma$ |
| $\Lambda$ | $0$ | $0$ | $1115$ | $m_0+\alpha$ |
| $N$ | $\tfrac12$ | $1$ | $939$ | $m_0+\alpha+\beta+\tfrac12\gamma$ |

Eliminating the four parameters $m_0,\alpha,\beta,\gamma$ gives the relations

$$
m_\Xi+m_N = \tfrac12\bigl(3m_\Lambda+m_\Sigma\bigr),
\qquad
m_\Xi+m_N = 2m_0+2\alpha+\gamma .
$$

The first is the Gell-Mann–Okubo relation for the baryon octet. The second identifies the combination $2m_0+2\alpha+\gamma$ with the sum, so that with $m_0=\frac14(m_N+m_\Lambda+m_\Sigma+m_\Xi)$ the relation becomes a statement about the octet average.

**Check.** With the Particle Data Group values $m_N=938.918$, $m_\Lambda=1115.683$, $m_\Sigma=1193.154$, $m_\Xi=1318.0$ MeV:

$$
m_N+m_\Xi = 2256.9\ \text{MeV},
\qquad
\tfrac12(3m_\Lambda+m_\Sigma) = 2270.1\ \text{MeV},
$$

a discrepancy of $0.58\%$. The relation is satisfied to better than one percent by the physical masses, which is the standard statement of $\mathrm{SU}(3)$ flavour symmetry's accuracy, and it is a genuine test because the four masses are independent inputs.

## The Supermultiplet Mass $m_0$

The parameter $m_0$ is $\mathrm{SU}(3)$-invariant and therefore **not determined by $\mathrm{SU}(3)$**; it is an external parameter, one value per supermultiplet, and it is the average of the masses of the charge multiplets in the supermultiplet. For the baryon octet,

$$
m_0 = \tfrac14\bigl(m_N+m_\Lambda+m_\Sigma+m_\Xi\bigr).
$$

The programme closes the system by identifying $m_0$ with the mass of the spin representation that carries the supermultiplet. That is the companion mass formula's $m^{(s)}=\frac{\mu_0}{4}\deg\tau^{l\dot l}$, with $l,\dot l$ the representation of the octet's spin line. The two chapters therefore connect: the representation degree fixes the **centre** of the supermultiplet's mass multiplet, and the Gell-Mann–Okubo formula fixes the **splitting** about that centre. The companion article's numbers — $1770\,m_e$, $2278\,m_e$, $264.5\,m_e$ for the nucleon, $\Sigma$ and $\pi$ — are these centres, and the splittings about them are the $\pm\beta\mp\tfrac12\gamma$ and $2\gamma$ of the table above.

## The Biquaternion Reading

The reading is short because the framework's own limit is known. The $\mathrm{SU}(3)$ representations, the Okubo operators $A^{i}_{\ k}$, the unitary field $Z$ and the mass splitting are **not elements of the biquaternion algebra**. The companion *Gauge Group Ceiling* shows the algebra's compact structure stops at $\mathrm{SU}(2)$, so no $\mathfrak{su}(3)$ with an octet of generators can be built from $\mathbb{B}$; the Okubo matrices are $3\times3$, and the algebra of three-by-three matrices is not the biquaternion algebra. The $\mathrm{SU}(3)$ machinery is external, and the article's purpose is to record it accurately beside the framework's own statements, not to claim it.

What the framework can host is the **structure of the splitting**. The Gell-Mann–Okubo formula separates a symmetric part $m_0$ from a symmetry-breaking part $\delta m$ built from the Cartan directions of the algebra; the framework knows the analogous separation — a central, $\mathrm{SU}(2)$-invariant part and a breaking part along a distinguished direction — in its own sector structure and in the hypercharge direction of the charge factor. Whether the hypercharge splitting has a biquaternion image is not established here; the honest statement is that the algebra hosts the singlet/triplet/doublet isospin reduction (since those are $\mathrm{SU}(2)$ representations) and not the octet of $\mathrm{SU}(3)$.

One further point is worth recording because the programme itself flags it. The **unitary field** $Z$ — the analogue of the external magnetic field in the Zeeman effect — has, the programme says, no known physical sense; it differs between supermultiplets only by two real parameters, and it is suggested that it be read as a non-local substrate in the sense of decoherence, a field whose coupling localises particles into the energy levels of a supermultiplet. The corpus's companion articles on information in the gauge orbit and on the Higgs mechanism as erasure are the natural place to compare such a reading; here it is recorded as the programme's speculation, not as a framework claim.

## What the Framework Establishes, Transcribes, and Does Not

**Established, and recomputed.**

- The degree formula $N(p,q)=\frac12(p+1)(q+1)(p+q+2)$ and the table: $N(0,0)=1$, $N(1,1)=8$, $N(3,0)=10$, $N(2,2)=27$, $N(0,6)=28$, $N(4,1)=35$, $N(1,7)=80$, $N(5,2)=81$, $N(3,3)=64$, $N(4,4)=125$, $N(3,6)=154$. Recomputed (see the `.context` for the transcript).
- The admissibility condition $p-q\equiv0\pmod3$ and the resulting degree list $1,8,10,27,28,35,\dots$; consistent with the table.
- The octet reduction $\mathrm{Sym}_0^{(1,1)}=\Phi_3\oplus\Phi_2\oplus\Phi_2^*\oplus\Phi_0$, dimensions $3+2+2+1=8$.
- The Gell-Mann–Okubo relation $m_\Xi+m_N=\frac12(3m_\Lambda+m_\Sigma)$ against the PDG baryon masses: $2256.9$ versus $2270.1$ MeV, a $0.58\%$ discrepancy. Recomputed.

**Transcribed, not derived.**

- The Okubo basis, the commutators, the three $\mathfrak{su}(2)$ subalgebras and the charge operator.
- The Zeeman analogy, the unitary moment and field, and the derivation of the formula through the Casimirs.
- The particle content of the octets and the identification of $m_0$ with the spin–mass formula's value.

**Gap, left visible.**

- $\mathrm{SU}(3)$ is not an algebra of $\mathbb{B}$; the whole structure is external to the framework, and the article says so in its opening and its closing sections.
- The physical sense of the unitary field $Z$ is unknown, by the programme's own statement.
- The charge-splitting parameter $\theta$ and the constants $\alpha,\beta,\gamma$ are fitted to the measured masses; $\mathrm{SU}(3)$ symmetry predicts the *form* of the splitting, not its size.

## Open Questions

1. **Does the hypercharge direction have a biquaternion image?** The corpus has a preferred direction, the $ict$ axis of the material sector, and a central phase. Is the hypercharge splitting's distinguished direction one of these, or is the correspondence spurious? The gauge-ceiling article implies the latter unless a larger algebra is used.

2. **$m_0$ and the mass formula.** The identification of $m_0$ with the spin–mass formula's $m^{(s)}$ is a choice. Does the equality hold for the meson octets as well as the baryon octet, and does the companion mass formula's error (a few percent) propagate into the average?

3. **The decuplet's equal spacing.** The decuplet $(3,0)$ obeys equal spacing, $m_\Omega-m_{\Xi^*}=m_{\Xi^*}-m_{\Sigma^*}=m_{\Sigma^*}-m_\Delta$, a different relation from the octet's. Is it a statement in I-spin or U-spin, and is the corpus's representation ring able to derive the two relations at once?

4. **The unitary field and decoherence.** The programme's speculation that $Z$ describes a non-local substrate that localises particles overlaps the corpus's information-theoretic articles. Is there a biquaternion reading of $Z$ that is not a fitting parameter?

5. **Charm and the fourth flavour.** The programme records that adding the charm quark extends $\mathrm{SU}(3)$ to $\mathrm{SU}(4)$. Does the admissibility condition generalise, and does the degree formula have an $\mathrm{SU}(N)$ form the corpus can state?

## Summary

An irreducible representation of $\mathrm{SU}(3)$ is a traceless bisymmetric tensor labelled by $(p,q)$ with degree $N(p,q)=\frac12(p+1)(q+1)(p+q+2)$; the singlet is $(0,0)$, the triplets $(1,0)$ and $(0,1)$, the octet $(1,1)$ of degree $8$, the decuplet $(3,0)$ of degree $10$. Hadron supermultiplets are the admissible representations with $p-q\equiv0\pmod3$, degrees $1,8,10,27,28,35,\dots$. The octet reduces on $\mathrm{SU}(2)$ as $\Phi_3\oplus\Phi_2\oplus\Phi_2^*\oplus\Phi_0$, the triplet, the nucleon doublet, its conjugate and the $\Lambda$. Within a supermultiplet the mass splits as $m=m_0+\alpha+\beta Y+\gamma(I(I+1)-\frac14Y^2)$ in the hypercharge direction, giving the Gell-Mann–Okubo relation $m_\Xi+m_N=\frac12(3m_\Lambda+m_\Sigma)$, which the physical masses satisfy to $0.58\%$. The centre $m_0$ is $\mathrm{SU}(3)$-invariant and is the companion spin–mass formula's value.

The framework's relation to all this is negative and clean: $\mathrm{SU}(3)$ is not an algebra of the biquaternion algebra, the gauge-group ceiling stops at $\mathrm{SU}(2)$, and the Okubo matrices are three-by-three. The article records the structure accurately, checks its numerical content, and states that the splitting pattern — not the group — is what borders the framework's own sector structure.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(p,q)$, $p,q\in\mathbb{Z}_{\ge0}$ | Labels of an irreducible representation of $\mathrm{SU}(3)$ |
| $T^{a_1\dots a_p}_{b_1\dots b_q}$ | Traceless bisymmetric tensor carrying the representation |
| $N(p,q)=\tfrac12(p+1)(q+1)(p+q+2)$ | Degree of the representation |
| $A^{i}_{\ k}$ | Okubo basis of $\mathfrak{su}(3)$, traceless and Hermitian |
| $I_3,U_3,V_3$ | I-spin, U-spin, V-spin of the three $\mathfrak{su}(2)$ subalgebras |
| $Y,Q,I,U$ | Hypercharge, charge, and the I-spin and U-spin quantum numbers |
| $m^2=m_0^2+\delta m^2+\delta m^{2\prime}$ | Mass operator split into symmetric and breaking parts |
| $Z$, $D^{a}_{\ b}$ | Unitary field and unitary moment of the Zeeman analogy |
| $\theta$ | Ratio of charge to hypercharge splitting, $\lvert\theta\rvert\ll1$ |
| $m_\Xi+m_N=\tfrac12(3m_\Lambda+m_\Sigma)$ | Gell-Mann–Okubo relation, baryon octet |
| $p-q\equiv0\pmod3$ | Admissibility condition for a hadron supermultiplet |

## Further Reading

- M. Gell-Mann, "Symmetries of baryons and mesons," *Physical Review* **125** (1962) 1067–1084, for the eightfold way and the mass formula.
- Y. Ne'eman, "Derivation of strong interactions from a gauge invariance," *Nuclear Physics* **26** (1961) 222–229, for the independent proposal of the $\mathrm{SU}(3)$ classification.
- S. Okubo, "Note on unitary symmetry in strong interactions," *Progress of Theoretical Physics* **27** (1962) 949–966, for the mass formula and the Okubo basis.
- S. Okubo, *Introduction to Octonion and Other Non-Associative Algebras in Physics*, and *Lecture Notes in Physics* **94**, for the Okubo operators and the Zeeman analogy.
- M. Gell-Mann and Y. Ne'eman, *The Eightfold Way* (Benjamin, 1964), for the octets, the decuplet and the mass relations.
- Particle Data Group, *Review of Particle Physics*, for the hadron masses used in the checks.
- V. V. Varlamov, "Spinor Structure and Internal Symmetries," *International Journal of Theoretical Physics* **54** (2015) 3533–3576 (arXiv:1409.1400), for the representation theory, the Zeeman analogy and the identification of $m_0$ recorded here.
- Companion articles: *The Spin–Charge Hilbert Space and the SU(3) Supermultiplets in Biquaternionic Form*; *The Spin–Mass Formula and the Spectrum of Elementary Particles in Biquaternionic Form*; *The Gauge Group Ceiling: Why the Biquaternion Algebra Reaches SU(2) but Not SU(3)*; *The Gluon: An Octet Outside the Biquaternion Algebra*; *The Pion and the Chiral Lagrangian in Biquaternionic Form*.
