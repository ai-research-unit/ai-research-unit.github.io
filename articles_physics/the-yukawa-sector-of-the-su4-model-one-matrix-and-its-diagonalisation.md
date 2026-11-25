# __The Yukawa Sector of the $\mathrm{SU}(4)$ Model: One Matrix and Its Diagonalisation__

## Introduction

**One operator, one matrix, two masses, and no phase.** The Yukawa sector of this model is $\mathcal{L}_{Y}=y_{\alpha\beta}\,\bar\xi^{\alpha\dagger}Ξ\,\xi^{\beta}+\text{h.c.}$, with $y$ a $2\times2$ complex matrix on the copy index. **That is the whole sector**: no second Higgs, no second condensate, and no matrix whose diagonalisation could disagree with the first one's.

**What it fixes and what it cannot.**

- **It fixes the fermion masses up to two numbers.** $y$ has eight real parameters, six of them are rotations that nothing in the model can see, and **two survive: the eigenvalues.**
- **It ties the lepton mass to the quark mass, with a ratio of three.** The condensate is $v\operatorname{diag}(-3,1,1,1)$, so a fermion on the lepton line is three times heavier than a fermion on a colour line with the same eigenvalue. **$m_{\ell}=3m_{q}$ within a copy**, and that is the sector's one quantitative statement.
- **It cannot produce a mixing angle or a phase.** One matrix, one mass basis, and no gauge vertex that changes the copy index. **The sector conserves $CP$ exactly**, and the reason is a count.
- **It cannot produce a hierarchy among the three generations, because the model has no generation index.** The copy index is a two-valued degeneracy, not a family label; **the three generations are not in this model.**

**The honest verdict, stated first.** $m_{e}=3m_{d}$ is wrong by a factor $27$, so **the model's Yukawa sector is its sharpest falsifiable statement and it is falsified.** That is not an arithmetic error and it is not patched below: it is the boundary of the model, and it is the reason a second condensate and a second matrix are needed below $M_C$.

## Why There Is No Mass Term Before the Breaking

**A Dirac mass needs a left-handed and a right-handed field of the same charge, and the sixteen supply them in pairs.** So a mass term $\bar\xi\xi$ is allowed by the gauge symmetry — **and it is not written.** The reason is a choice of the model's ledger and not a theorem: **$Ξ$ is what gives the sixteen their masses, and a bare mass would be a second source that the ledger does not carry.**

**The consequence is the one that matters downstream.** Every fermion is massless in the symmetric phase, the electroweak-scale ratios are set by $y$ alone, and **there is no see-saw, because there is no gauge-singlet mass to give a right-handed neutrino.**

**What replaces the usual "no mass term" argument.** In the Standard Model the mass term is forbidden because $\bar Q_L H d_R$ and $\bar Q_L\tilde H u_R$ are the only renormalisable options. **Here the argument is different and weaker**: the term is allowed and omitted, and the article says so rather than pretending the group forbids it.

## The One Operator, and Its Parameter Count

**The operator, written with the indices visible.**

$$
\mathcal{L}_{Y}=y_{\alpha\beta}\,\bar\xi^{\alpha\dagger}_{\,i}\,Ξ_{ij}\,\xi^{\beta}_{j}+\text{h.c.},
\qquad i,j\in\{t,x,y,z\},\quad \alpha,\beta\in\{1,2\}.
$$

**It is invariant and the invariance is one line of representation arithmetic.** $\xi$ is a $\mathbf 4$, $\bar\xi$ a $\bar{\mathbf4}$, and $Ξ$ a Hermitian $4\times4$, which is $\mathbf{15}\oplus\mathbf1$. **$\bar{\mathbf4}\otimes\mathbf4=\mathbf{15}\oplus\mathbf1$ contains the identity, so the product contracts to a singlet**, and the contraction is the matrix trace read in the quartet index.

**The matrix $y$ is on the copy index and on nothing else.** It cannot carry a colour index (invariance), it cannot carry a momentum (locality), and it cannot carry a generation label (there is none). **So the sector's whole freedom is a $2\times2$ complex matrix**, and the next paragraph counts what of it is physical.

| step | real parameters | what removes them |
| --- | --- | --- |
| $y$ as written | $8$ | — |
| rephasing $\xi^{\alpha}$ | $-2$ | two independent phase rotations of the quartet fields |
| rephasing $\bar\xi^{\alpha}$ | $-2$ | two independent phase rotations of the conjugate fields |
| rotating the copy basis | $-2$ | one $\mathrm{U}(2)$ acting on $\alpha$ in both fields at once |
| **physical** | $\mathbf 2$ | the two eigenvalues, real and positive by convention |

**The count is $8-6=2$, and the six are not approximate.** A bi-unitary transformation $y\to W^{\dagger}yV$ with $W,V\in\mathrm{U}(2)$ can always be chosen to make $y$ diagonal with real non-negative entries — **the singular-value decomposition, and it exists for every $2\times2$ matrix.** So the sector's physical content is two numbers.

**Those two numbers are masses and nothing else.** A mixing angle would need a vertex that changes $\alpha$, and §*What the Algebra Forbids* of [the vertex article](the-fermion-gauge-vertex-in-the-quartet-basis-the-fifteen-read-on-the-sixteen.html) shows that no generator has one. **An unobservable angle is not a parameter**, and the sector does not have one.

## After the Breaking: the Mass Matrix and the Factor Three

**The condensate is $v\operatorname{diag}(-3,1,1,1)$, and the mass matrix is the Yukawa matrix multiplied by the entry of the condensate that the fermion sits on.**

$$
M_{\alpha\beta}^{\ \ \ \imath\jmath}=y_{\alpha\beta}\,v\,D_{\imath}\,\delta_{\imath\jmath},
\qquad D=\operatorname{diag}(-3,1,1,1).
$$

**The matrix is diagonal in the quartet index and proportional to $y$ in the copy index.** That sentence is the whole structure of the sector, and it has three consequences.

**The first is the factor three.** A fermion on the lepton line gets $-3v\,y_{\alpha\beta}$ and one on a colour line gets $+v\,y_{\alpha\beta}$: **the same eigenvalue, multiplied by three on the lepton line.** Nothing in $y$ can undo it, because $y$ multiplies both.

**The second is the colour degeneracy.** The three colour lines have the same entry $+v$, so **the three colours of a quark are exactly degenerate.** That is a prediction and it is exact: the condensate does not break colour, so no colour-split mass can appear at this level.

**The third is that the four masses of one generation are two numbers.** With $y$ diagonalised to $(y_{1},y_{2})$:

| field | line | mass |
| --- | --- | --- |
| $\nu$ | lepton, copy $1$ | $3v\,|y_{1}|$ |
| $u^{r},u^{g},u^{b}$ | colour, copy $1$ | $v\,|y_{1}|$ |
| $e$ | lepton, copy $2$ | $3v\,|y_{2}|$ |
| $d^{r},d^{g},d^{b}$ | colour, copy $2$ | $v\,|y_{2}|$ |

**Eight mass eigenstates, four distinct values, two parameters, and a ratio of three fixed by the condensate.** A reader who wants the Standard Model's four independent masses has to add three parameters that this model does not have.

## Diagonalisation, and Why No Phase Survives

**Bi-unitary diagonalisation is the standard step, and here it is a step with no residue.**

$$
y=W\,\operatorname{diag}(y_{1},y_{2})\,V^{\dagger},
\qquad y_{1},y_{2}\ge 0,
$$

**with $W,V\in\mathrm{U}(2)$.** The two unitary factors are the copy-basis changes of $\bar\xi$ and $\xi$, and **neither of them appears in any vertex**, because no vertex carries the copy index.

**So the mixing matrix is unobservable, and with it the phase.** In the quark sector of the Standard Model the product $W_{u}^{\dagger}W_{d}$ survives as the CKM matrix because the up and the down masses come from two different matrices. **Here they come from one matrix**, so the product is $W^{\dagger}W=\mathbb 1$ after diagonalisation, **and the phase that a second matrix would have left behind has nothing to multiply.**

**The $CP$ statement, exactly.** The gauge sector is real in this basis (the structure constants are integers and the generators are real or $i$ times real), and the Yukawa sector is one matrix diagonalisable to real positive entries. **So the model conserves $CP$ exactly, in both sectors, and the reason is a count: one matrix, not two.** That is a statement about this model and not about the world; **the observed $CP$ violation belongs below $M_C$**, where a second matrix exists.

**The Jarlskog invariant is zero and the computation is one line.** $J=\operatorname{Im}\det[y_{u}y_{u}^{\dagger},y_{d}y_{d}^{\dagger}]$; with $y_{u}=y_{d}=y$ the commutator vanishes, so $J=0$. **Two sectors, one matrix, no invariant.**

## What This Predicts, and the Factor $27$

**The sector makes exactly one ratio prediction, and the measurement rejects it.**

| quantity | the model | the measurement | verdict |
| --- | --- | --- | --- |
| $m_{e}/m_{d}$ | $3$ | $0.109$ | wrong by $27$ |
| $m_{\nu}/m_{u}$ | $3$ | below $10^{-6}$ | wrong by more than $10^{6}$ |
| $m_{u}/m_{d}$ | free, $y_{1}/y_{2}$ | $0.47$ | no statement |
| $m_{u}/m_{c}$ | no generation index | $0.0022$ | absent |
| colour degeneracy | exact | exact | holds |
| $CP$ violation | $0$ | $J\approx3\times10^{-5}$ | absent |

**The first row is the one to quote.** $m_{e}=0.511$ MeV and $m_{d}\simeq4.7$ MeV at $2$ GeV give $0.109$; the model gives $3$; **the ratio of the two is $27.4$.** The arithmetic is three lines and the conclusion is not negotiable.

**The reason is structural and cannot be repaired inside the model.** The factor three is the ratio of the condensate's entries, $-3$ against $+1$, and it is the same number that makes the leptoquark heavy. **A model whose lepton and quark masses differ by a fixed factor has no freedom left to fix them**, and that is the definition of the boundary this sector hits.

**What the transition must add, stated as a requirement and not as a promise.** A second condensate, so that the lepton line and the colour lines can receive different factors; a second Yukawa matrix, so that a phase can survive; and a generation index, so that a hierarchy can exist. **None of the three is in this model, and the article's claim is only that the three are necessary.**

## Neutrinos

**The neutrino is a Dirac fermion here and its mass is tied to the up quark's.** The lepton line of the conjugate quartet at $B-L=+1$ is the right-handed neutrino's slot, so **the neutrino gets a Dirac mass $3v|y_{1}|$ and no Majorana mass**: a Majorana term would need $\xi\xi$, which is not invariant, because $\mathbf4\otimes\mathbf4$ does not contain a singlet.

**There is no see-saw and no light neutrino.** $m_{\nu}=3m_{u}$ is the sector's statement, and the measurement makes it the sector's worst failure. **The corpus's position is that the fault is in the number of condensates and not in the group**, which is the same diagnosis the lepton–quark ratio receives.

**What is not claimed.** No PMNS matrix, no mass ordering, no absolute scale: **all three need structure below $M_C$**, and the model has no mechanism that could produce any of them.

## What the Sector Does Not Do

**No three generations.** The model has a two-valued copy index and no family label. **The three generations are not in this model**, and a sentence about $m_{\mu}/m_{e}$ has no referent here.

**No loop and no running.** The masses above are tree-level and defined at the scale of the condensate. **A comparison with $m_{d}(2\,\text{GeV})$ imports a renormalisation-group evolution the model does not contain**, and the factor $27$ survives it: the evolution moves $m_d$ by tens of per cent, not by a factor of thirty.

**No hadronic physics.** $m_{d}$ is a Lagrangian parameter and no lattice input is used. **The comparison is at the level of parameters, which is the only level at which the model makes a statement.**

## The Checks

| check | computation | result |
| --- | --- | --- |
| parameters in $y$ | $2\times2$ complex | $8$ real |
| removed by rephasing and rotation | $2+2+2$ | $6$ |
| physical parameters | $8-6$ | $2$ |
| the operator's invariance | $\bar{\mathbf4}\otimes\mathbf4\supset\mathbf1$ | $\mathbf{15}\oplus\mathbf1$ |
| lepton-line mass | $3v\,|y_{\alpha}|$ | $3\times$ the colour case |
| colour degeneracy | three lines, one entry | exact |
| distinct masses per generation | two copies, two line types | $4$ values from $2$ numbers |
| the mixing matrix | $W^{\dagger}W$ | $\mathbb 1$ |
| the Jarlskog invariant | one matrix, commutator $0$ | $0$ |
| $m_{e}/m_{d}$ predicted | $3$ | $3$ |
| $m_{e}/m_{d}$ measured | $0.511/4.7$ | $0.109$ |
| disagreement | $3/0.109$ | $27.4$ |
| Majorana term | $\mathbf4\otimes\mathbf4\not\supset\mathbf1$ | forbidden |

## Summary

**One operator, one matrix, two masses, no phase.** The Yukawa sector is a $2\times2$ complex matrix on the copy index, reduced by rephasing and rotation to two real eigenvalues, and the condensate multiplies them by $-3v$ on the lepton line and $+v$ on the colour lines.

**The factor three is the sector's only prediction, and $m_{e}=3m_{d}$ is wrong by $27$.** That failure is structural: it comes from the same ratio that makes the leptoquark heavy, and no choice of $y$ can repair it.

**$CP$ is conserved exactly, because one matrix cannot disagree with itself.** A phase needs two matrices, the model has one, and the observed $CP$ violation therefore belongs below $M_C$.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $y_{\alpha\beta}$ | the Yukawa matrix on the copy index, $2\times2$ complex |
| $\xi^{\alpha}_{i}$, $\bar\xi^{\alpha}_{i}$ | the sixteen Weyl fields, quartet index $i$, copy index $\alpha$ |
| $Ξ$ | the Hermitian $4\times4$ scalar, $\mathbf{15}\oplus\mathbf1$, $16$ real components |
| $D=\operatorname{diag}(-3,1,1,1)$ | the condensate direction |
| $v$ | the condensate's scale, $v^{2}=-\mu^{2}/2\lambda$ |
| $y_{1}$, $y_{2}$ | the two eigenvalues, real and positive |
| $W$, $V$ | the bi-unitary factors, unobservable because no vertex carries $\alpha$ |
| $J$ | the Jarlskog invariant, zero for one matrix |

## Further Reading

- [The $\mathrm{SU}(4)$ Model](the-su4-model-four-colours-fifteen-generators-one-declaration.html). The content, the condensate, and the ledger this sector sits in.
- [The Classification of the Fermions](classification-of-the-fermions-in-the-su4-model-sixteen-weyl-fields-closed-under-c-and-cp.html). Why the model is closed under $C$ and $CP$, and where the copy index sits.
- [The Fermion–Gauge Vertex in the Quartet Basis](the-fermion-gauge-vertex-in-the-quartet-basis-the-fifteen-read-on-the-sixteen.html). The proof that no vertex carries the copy index, which is the reason no phase survives.
- [The Feynman Rules](the-feynman-rules-of-the-su4-model-the-vertices-of-the-fifteen-and-the-sixteen.html). The Lagrangian this sector is one line of.
- [An Introduction to Flavour](an-introduction-to-flavour.html). What a generation index would have to supply, and why this model has none.
- [The Breaking of the Primordial Force](the-breaking-of-the-primordial-force-and-the-mass-of-the-six-leptoquarks.html). The same condensate, read on the gauge side.
