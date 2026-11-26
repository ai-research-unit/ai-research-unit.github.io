# __The Scalar Content: One Matrix, Sixteen Components, Six Eaten and Ten Survivors__

## Introduction

**The question.** What carries the vacuum at $M_C$, how many real components does it have, how many are eaten, and how many survive?

**The answer.**

$$
\boxed{\;
Ξ\in\mathbf{15}\oplus\mathbf1:\ 16\ \text{real},\ 6\ \text{eaten},\ 10\ \text{survive};\qquad
16=6+10 .
\;}
$$

**The count starts at fifteen and stops at sixteen.** $\dim\mathrm{SU}(4)=4^{2}-1=15$, and the traceless Hermitian $4\times4$ has exactly that many real entries. **The dimension is the algebra's and the space is not**: $\mathfrak{su}(4)$ is the traceless *anti-Hermitian* matrices — the generators $K$ of the corpus carry $K^{\dagger}=-K$ — and the traceless Hermitian matrices are $i\mathfrak{su}(4)$, reached by multiplying by $i$. **The scalar is what sits in the second space**, because $U\Xi U^{\dagger}$ is Hermitian whenever $\Xi$ is, and the derivation $[K,\cdot]$ of an anti-Hermitian $K$ is what keeps it there. The trace is one more real number, and the scalar may carry it, so the content is $\mathbf{15}\oplus\mathbf1$ and the count is $15+1=16$. **No further doubling is available**: the matrix is Hermitian, so its off-diagonal entries are not independent complex numbers, and no index is made local that would multiply them.

**The trace is a mode and not a constraint.** No condition is imposed on $Ξ$, and the count below is taken at the field's sixteen and not at the vacuum's fifteen. **Tracelessness belongs to the vacuum and not to the field**: $UΞ U^{\dagger}$ leaves $\operatorname{tr}Ξ$ alone, so the trace is a symmetry singlet and a dynamical degree of freedom, and *The Primordial Potential* puts the minimum at $\operatorname{tr}Ξ=0$ by giving that mode a positive quadratic coefficient. **The tempting wrong count is "fifteen generators, so fifteen scalar directions"**, and it confuses the algebra with the field: a generator is traceless because $\mathfrak{su}(4)$ removes the trace, and that removal says nothing about a boson that is not a generator.

**What this article establishes.** That the multiplet is one Hermitian matrix; why the matrix index is forced by the Yukawa operator; the decomposition of the sixteen into blocks under the residual $\mathrm{U}(3)$; the count of eaten and surviving components; and the price that count carries.

**What it does not establish.** A potential, a mass for any survivor, or a Yukawa matrix. It is a census, and the articles that need the numbers cite it rather than recounting them.

**Where the neighbours are.** The breaking that eats the six is [The Breaking of the Primordial Force](the-breaking-of-the-primordial-force-and-the-mass-of-the-six-leptoquarks.html). The transition is [The Matching at $M_C$](matching-at-m-c.html). The field that waits for the electroweak scale is [The Weak Sector Below $M_C$](the-weak-sector-below-m-c-three-neutrals-a-diagonal-charged-pair-and-the-bidoublet.html). The operator the matrix index makes possible is [The Yukawa Sector](the-yukawa-sector-of-the-su4-model-one-matrix-and-its-diagonalisation.html).

## The Field

**One Hermitian $4\times4$, and its sixteen is the algebra's.**

| object | real parameters | what it is |
| --- | --- | --- |
| the traceless Hermitian $4\times4$ | $16-1=15$ | the adjoint, $\mathbf{15}$ |
| the trace | $1$ | the singlet, $\mathbf1$ |
| **$Ξ$** | $\mathbf{16}$ | $\mathbf{15}\oplus\mathbf1$ |

**Why Hermitian and not general complex.** The scalar's kinetic term is $\operatorname{tr}(D_{\imath}Ξ)^{\dagger}(D_{\imath}Ξ)$, and its potential is built from $Ξ^{\dagger}Ξ$. **A general complex matrix would carry a phase per entry that no term in the action depends on**, so those phases are not dynamical and are removed by the same argument that removes a would-be Goldstone of an not made local symmetry. **The physical field is the Hermitian one**, and its count is the algebra's count.

**Why not a quartet.** The mass operator decides it:

$$
\bar\xi\,Ξ\,\xi\to\mathbf1
\quad\Longleftrightarrow\quad
\bar{\mathbf4}\otimesΞ\otimes\mathbf4\supset\mathbf1
\quad\Longleftrightarrow\quad
Ξ\in\bar{\mathbf4}\otimes\mathbf4=\mathbf{15}\oplus\mathbf1 .
$$

**And $\mathbf4\otimes\mathbf4=\mathbf6\oplus\mathbf{10}$ contains no $\bar{\mathbf4}$**, so a scalar in the fundamental forms no operator with one $\bar\xi$ and one $\xi$ at all.

| candidate $Ξ$ | $\bar\xi\,Ξ\,\xi$ | invariant? |
| --- | --- | --- |
| $\mathbf4$ | needs $\mathbf4\subset\mathbf4\otimes\mathbf4=\mathbf6\oplus\mathbf{10}$ | **no** |
| $\mathbf{15}\oplus\mathbf1=\mathbf4\otimes\bar{\mathbf4}$ | $\bar{\mathbf4}\otimes(\mathbf4\otimes\bar{\mathbf4})\otimes\mathbf4\to\mathbf1$ | yes |
| $\mathbf6$ | needs two conjugates, $\bar{\mathbf4}\otimes\bar{\mathbf4}\otimes\mathbf6$ | yes, but not with one $\xi$ |

**So the matrix is not a preference; it is forced by the existence of a mass term**, and its size is then fixed by the algebra and by nothing else.

## The Blocks Under the Residual Group

**Write the vacuum and the blocks follow.**

$$
Ξ=v_C\,D+\text{fluctuations},
\qquad
D=\operatorname{diag}(-3,1,1,1),
\qquad
\operatorname{tr}D=0 .
$$

**The stabiliser of $D$ is $\mathrm{U}(3)$ on the last three lines**, and the sixteen decompose under it by where the entries sit in the matrix.

$$
\mathbf{15}\oplus\mathbf1\;\longrightarrow\;\mathbf8_0\oplus\mathbf3_{+\frac43}\oplus\bar{\mathbf3}_{-\frac43}\oplus\mathbf1_0\oplus\mathbf1_0 .
$$

**The triplet's charge is positive**, $+\tfrac43$, because moving the lepton into a spatial slot raises $B-L$ by $\tfrac13-(-1)$; the antitriplet carries the minus. **Count the real components block by block, not by multiplying complex entries.**

| block | where it sits | real components | eaten | survivors |
| --- | --- | --- | --- | --- |
| $\mathbf8_0$ | the traceless $3\times3$ corner | $8$ | $0$ | $8$ |
| $\mathbf3\oplus\bar{\mathbf3}$ | the row and column through the fourth line | $6$ | $6$ | $0$ |
| $\mathbf1_0$ | the trace of the $3\times3$ corner | $1$ | $0$ | $1$ |
| $\mathbf1_0$ | the $(4,4)$ entry | $1$ | $0$ | $1$ |
| **total** | | $\mathbf{16}$ | $\mathbf{6}$ | $\mathbf{10}$ |

**The arithmetic of the rows.** A Hermitian $3\times3$ has nine real entries: eight traceless and one trace. The off-diagonal block — three entries in the fourth row, their three conjugates in the fourth column — is three complex numbers, so six real. The $(4,4)$ entry is one real. **$9+6+1=16$, and the four rows are the same sixteen.**

**Six is the count of broken generators, and the two routes agree.** Fifteen generators, nine of which commute with $D$, so six are broken; and the $\mathbf3\oplus\bar{\mathbf3}$ block has exactly six real components. **The Goldstone theorem is the statement that these are the same count**, and here it can be read off the matrix.

**The octet loses nothing.** The vacuum is a singlet, so no generator acting on the $\mathbf8_0$ block is broken, and all eight real octet components survive. **They are octets with $B-L=0$**, and they are heavy at $M_C$ because their mass is the condensate's scale.

**And the two singlets are one radial mode and one physical scalar.** The vacuum lies along one combination of the two singlet directions, and the mode along the vacuum is the radial excitation; the combination orthogonal to it is a physical scalar. **So the ten are $8+1+1$: an octet, a singlet, and the radial mode.**

## The Ledger

**One scale, one subtraction.**

$$
\underbrace{16}_{\Phi}=\underbrace{6}_{\text{eaten at }M_C}+\underbrace{10}_{\text{surviving}} .
$$

**The ten split as eight octet, one singlet, one radial.** No other scalar exists in the content at this scale, and any count that reports a different total has doubled an index that no generator acts on.

**The doublet is a different field.** The electroweak doublet $H$ that the weak sector uses is blind to the block, four real components, three of them eaten at $v$ and one the Higgs. **It is not part of this matrix and it is not counted here**; it is counted in [The Weak Sector Below $M_C$](the-weak-sector-below-m-c-three-neutrals-a-diagonal-charged-pair-and-the-bidoublet.html).

**Why the doublet cannot be a component of $Ξ$.** $Ξ$ carries two indices and no left index, so its survivors are octets and singlets, and **a singlet is neutral under the left factor**. The standard Higgs mechanism needs a field that transforms under the left factor and carries hypercharge, and no component of a spatial matrix does.

## What the Sixteen Cost

**The number is a liability and it is stated before the article's checks.**

- *A octet of eight real scalars.* It survives $M_C$ and couples to two gluons through the kinetic term. **Its mass is the condensate's scale times a quartic coefficient**, so it is heavy by construction; the model cannot say why beyond that, because the only scale available is $M_C$.
- *One extra singlet.* It mixes with the doublet below $v$, so the lightest neutral scalar is a mixture and not $H$ alone. **The corpus's "one doublet that waits" describes the breaking correctly and the spectrum only approximately.**
- *Proton decay.* The dangerous block is the $\mathbf3\oplus\bar{\mathbf3}$, and it is eaten at $M_C$. **The octet adds loop-level channels**, and none is computed here.

**What a smaller sector would need.** A singlet scalar would decouple from the strong sector entirely and could form no Yukawa operator for these fermions. **The sixteen is the price of the mass operator**, and it is paid here rather than in a later article.

## The Checks

| claim | check | result |
| --- | --- | --- |
| the dimension of the algebra | $4^{2}-1$ | $15$ |
| the count of $Ξ$ | $15+1$ | $16$ real |
| the blocks | $8+6+1+1$ | $16$ |
| the eaten count at $M_C$ | six of the $\mathbf3\oplus\bar{\mathbf3}$ | $6$ |
| the same from generators | $15-9$ | $6$ |
| the massless vectors at $M_C$ | $15-6$ | $9=\dim\mathfrak{u}(3)$ |
| the survivors | $16-6$ | $10$ |
| the block sum | $8+1+1$ | $10$ |
| the Yukawa | $\bar{\mathbf4}\otimes(\mathbf{15}\oplus\mathbf1)\otimes\mathbf4\supset\mathbf1$ | one contraction per block, so two operators |
| the scalar's effect on $b_0$ | $N_s=16$ real, weight $\tfrac16$ | scalar term $-\tfrac23$ |

**The two routes to six agreeing is the check that matters**, because one counts generators and the other counts real components. **They agree because the Goldstone theorem is the statement that the two counts are the same count**, and a census that has them disagree has multiplied something.

## Distinctions That Are Easy to Lose

A breaking is not a deletion. The six vectors eaten at $M_C$ are rotations of the condensate; the vectors that swallow them are what the rotations become (*The Breaking of the Primordial Force*).

A survivor is not a light field. All ten survivors of $Ξ$ are heavy at $M_C$, because their mass is the condensate's scale.

A Hermitian matrix is not half a complex one. $\mathbf{15}\oplus\mathbf1$ is sixteen real, and the sixteen is $15+1$, not $32$.

A count of components is not a count of particles. Sixteen real components are the scalar's degrees of freedom one for one; a fermion's sixteen Weyl fields are thirty-two states, and the two counts are not the same kind of count.

## Summary

**One Hermitian $4\times4$.** $\mathbf{15}\oplus\mathbf1$, sixteen real components, fifteen from the algebra and one from the trace. **The matrix index is forced by the mass operator**: $\bar\xiΞ\xi$ needs $Ξ\in\bar{\mathbf4}\otimes\mathbf4$, and $\mathbf4\otimes\mathbf4=\mathbf6\oplus\mathbf{10}$ contains no $\bar{\mathbf4}$.

**Six eaten, ten surviving.** The six are the $\mathbf3\oplus\bar{\mathbf3}$ block, one real component per broken generator; the ten are an octet, a singlet and the radial mode.

**The sixteen is also the number the running uses.** A scalar multiplet of sixteen real components contributes $-\tfrac23$ to $b_0$ — the real-scalar weight $\tfrac16$ on the adjoint Dynkin index $4$ — and that is the term [The Primordial Coupling](the-primordial-coupling.html) subtracts. **Each doubling of the count doubles that term**: thirty-two real components would give $-\tfrac43$ and $b_0=8$, and sixty-four would give $-\tfrac83$ and $b_0=\tfrac{20}{3}$. **The census and the running are therefore one statement and not two**, and the coupling article tabulates the three side by side.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $Ξ$ | the scalar, a Hermitian $4\times4$, $\mathbf{15}\oplus\mathbf1$ |
| $D$ | $\operatorname{diag}(-3,1,1,1)$, the vacuum's shape, traceless |
| $\mathbf8_0$ | the traceless $3\times3$ corner, eight real components |
| $\mathbf3\oplus\bar{\mathbf3}$ | the fourth row and column, six real, all eaten |
| the two $\mathbf1_0$ | the trace of the corner and the $(4,4)$ entry |
| $H$ | the electroweak doublet, four real, not part of $Ξ$ |

## Further Reading

- [The Breaking of the Primordial Force](the-breaking-of-the-primordial-force-and-the-mass-of-the-six-leptoquarks.html). The six, named, and the masses they give.
- [The Primordial Potential](the-primordial-potential-one-symmetric-minimum-above-m-c.html). The potential these sixteen components sit in.
- [The Scalar's Two Indices](the-scalars-two-indices-and-the-count-sixteen.html). The same count from the representation side.
- [The Primordial Coupling](the-primordial-coupling.html). The $b_0$ that needs $N_s=16$.
